import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict
import anthropic
import openai
import groq
from enum import Enum
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles
import json
import re

load_dotenv()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Load API keys from environment variables
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

anthropic_client = anthropic.Client(api_key=ANTHROPIC_API_KEY)
openai.api_key = OPENAI_API_KEY
groq_client = groq.Client(api_key=GROQ_API_KEY)

class LLMModel(str, Enum):
    CLAUDE_3_OPUS = "claude-3-opus-20240229"
    GPT_4 = "gpt-4o"
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GROQ_LLM = "mixtral-8x7b-32768"

class FragmentAnalysisRequest(BaseModel):
    prompt: str
    model: LLMModel
    goal: Optional[str] = None

class Fragment(BaseModel):
    text: str
    type: str
    goal_alignment: int
    improvement_suggestion: str

class Log(BaseModel):
    type: str
    message: str

class PromptAnalysisRequest(BaseModel):
    prompt: str
    model: LLMModel
    goal: Optional[str] = None

class PromptAnalysisResponse(BaseModel):
    overall_goal_alignment: int
    suggested_improvements: List[str]
    estimated_effectiveness: int
    inferred_goal: Optional[str] = None
    is_goal_inferred: bool

class TestGenerationRequest(BaseModel):
    prompt: str
    model: LLMModel
    goal: Optional[str] = None

class Test(BaseModel):
    input: Dict[str, str]
    expected_output: str
    goal_relevance: int

class PromptExecutionRequest(BaseModel):
    prompt: str
    model: LLMModel

def get_llm_response(model: LLMModel, prompt: str, max_tokens: int = 1000, response_format={"type": "json_object"}) -> str:
    if model == LLMModel.CLAUDE_3_OPUS:
        response = anthropic_client.completions.create(
            model=model,
            prompt=prompt,
            max_tokens_to_sample=max_tokens,
            response_format=response_format,
        )
        return response.completion
    elif model in [LLMModel.GPT_4, LLMModel.GPT_3_5_TURBO]:
        response = openai.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            response_format=response_format,
        )
        return response.choices[0].message.content
    elif model == LLMModel.GROQ_LLM:
        response = groq_client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            response_format=response_format,
        )
        return response.choices[0].message.content
    else:
        raise ValueError(f"Unsupported model: {model}")

def infer_goal(prompt: str, model: LLMModel) -> str:
    inference_prompt = f"""Given the following prompt, infer the likely goal or intention of the user:

Prompt: {prompt}

Provide a concise statement of the inferred goal in one sentence as a JSON dictionnary with the key "goal" and the value being the inferred goal.
"""
    return json.loads(get_llm_response(model, inference_prompt))["goal"]

class GoalInferenceRequest(BaseModel):
    prompt: str
    model: LLMModel

@app.post("/api/infer-goal", response_model=str)
async def infer_goal_endpoint(request: GoalInferenceRequest):
    try:
        return infer_goal(request.prompt, request.model).strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/analyze-fragments", response_model=List[Fragment])
async def analyze_fragments(request: FragmentAnalysisRequest):
    try:
        if request.goal is None:
            request.goal = infer_goal(request.prompt, request.model)

        llm_prompt = f"""Analyze the following prompt for an LLM, keeping in mind the goal:

Prompt: {request.prompt}

Goal: {request.goal}

Divide the prompt into fragments and analyze each fragment. For each fragment, determine:
1. The type (instruction, context, example, or constraint)
2. How well it aligns with the goal (1-5, where 5 is perfectly aligned)
3. A suggestion for improvement to better align with the goal

Provide your analysis in the following JSON format without any other text:
{{
  "fragments": [
    {{
      "text": "fragment text",
      "type": "fragment type",
      "goal_alignment": alignment_score,
      "improvement_suggestion": "suggestion to better align with goal"
    }},
    ...
  ]
}}
"""

        analysis = json.loads(get_llm_response(request.model, llm_prompt))
        return [Fragment(**fragment) for fragment in analysis["fragments"]]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/analyze-logs", response_model=List[Log])
async def analyze_logs(request: PromptAnalysisRequest):
    try:
        if request.goal is None:
            request.goal = infer_goal(request.prompt, request.model)

        llm_prompt = f"""Analyze the following prompt for an LLM, keeping in mind the goal:

Prompt: {request.prompt}

Goal: {request.goal}

Generate a list of logs (info, warnings, or errors) based on the changes being made to the prompt. Focus on aspects that are relevant to achieving the goal.

Provide your analysis in the following JSON format without any other text:
{{
  "logs": [
    {{
      "type": "info/warning/error",
      "message": "log message relevant to achieving the goal"
    }},
    ...
  ]
}}
"""

        analysis = json.loads(get_llm_response(request.model, llm_prompt))
        return [Log(**log) for log in analysis["logs"]]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/analyze-prompt", response_model=PromptAnalysisResponse)
async def analyze_prompt(request: PromptAnalysisRequest):
    try:
        is_goal_inferred = False
        if request.goal is None:
            request.goal = infer_goal(request.prompt, request.model)
            is_goal_inferred = True

        llm_prompt = f"""Analyze the following prompt for an LLM, keeping in mind the {'inferred' if is_goal_inferred else 'provided'} goal:

Prompt: {request.prompt}

{'Inferred' if is_goal_inferred else 'Provided'} Goal: {request.goal}

Provide an overall analysis including:
1. Overall alignment of the prompt with the goal (1-10)
2. List of suggested improvements to better achieve the goal
3. Estimated effectiveness of the prompt in achieving the goal (1-10)

Provide your analysis in the following JSON format without any other text:
{{
  "overall_goal_alignment": overall_alignment_score,
  "suggested_improvements": ["improvement1", "improvement2", ...],
  "estimated_effectiveness": effectiveness_score,
  "inferred_goal": "{request.goal if is_goal_inferred else None}",
  "is_goal_inferred": {str(is_goal_inferred).lower()}
}}
"""

        analysis = PromptAnalysisResponse(**json.loads(get_llm_response(request.model, llm_prompt)))    
        return analysis

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/generate-test", response_model=Test)
async def generate_test(request: TestGenerationRequest):
    try:
        if request.goal is None:
            request.goal = infer_goal(request.prompt, request.model)

        variables = re.findall(r'\{([^}]+)\}', request.prompt)
        
        llm_prompt = f"""Generate a test case for the following LLM prompt, keeping in mind the goal:

Prompt: {request.prompt}

Goal: {request.goal}

Variables found in the prompt: {', '.join(variables)}

Provide a test case that is relevant to achieving the goal. Use the following JSON format:
{{
  "input": {{
    "variable1": "value1",
    "variable2": "value2",
    ...
  }},
  "expected_output": "expected output for the test case",
  "goal_relevance": relevance_score
}}

The input should include values for all variables found in the prompt.
The goal_relevance score should be from 1-5, where 5 means the test case is highly relevant to achieving the goal.
"""

        test = Test(**json.loads(get_llm_response(request.model, llm_prompt)))
        return test

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/execute-prompt", response_model=str)
async def execute_prompt(request: PromptExecutionRequest):
    try:
        return get_llm_response(request.model, request.prompt)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
