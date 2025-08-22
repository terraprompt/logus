"""
Core module for prompt engineering functionality.
"""

import os
import json
import re
from typing import List, Optional, Dict, Any
from enum import Enum
import anthropic
import openai
import groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load API keys from environment variables
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize clients
anthropic_client = (
    anthropic.Client(api_key=ANTHROPIC_API_KEY) if ANTHROPIC_API_KEY else None
)
openai.api_key = OPENAI_API_KEY if OPENAI_API_KEY else None
groq_client = groq.Client(api_key=GROQ_API_KEY) if GROQ_API_KEY else None


class LLMModel(str, Enum):
    CLAUDE_3_OPUS = "claude-3-opus-20240229"
    GPT_4 = "gpt-4o"
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GROQ_LLM = "mixtral-8x7b-32768"


class Fragment:
    def __init__(
        self, text: str, type: str, goal_alignment: int, improvement_suggestion: str
    ):
        self.text = text
        self.type = type
        self.goal_alignment = goal_alignment
        self.improvement_suggestion = improvement_suggestion


class Log:
    def __init__(self, type: str, message: str):
        self.type = type
        self.message = message


class Test:
    def __init__(
        self, input: Dict[str, str], expected_output: str, goal_relevance: int
    ):
        self.input = input
        self.expected_output = expected_output
        self.goal_relevance = goal_relevance


class PromptAnalysis:
    def __init__(
        self,
        overall_goal_alignment: int,
        suggested_improvements: List[str],
        estimated_effectiveness: int,
        inferred_goal: Optional[str] = None,
        is_goal_inferred: bool = False,
    ):
        self.overall_goal_alignment = overall_goal_alignment
        self.suggested_improvements = suggested_improvements
        self.estimated_effectiveness = estimated_effectiveness
        self.inferred_goal = inferred_goal
        self.is_goal_inferred = is_goal_inferred


def get_llm_response(model: LLMModel, prompt: str, max_tokens: int = 1000) -> str:
    """
    Get a response from the specified LLM.

    Args:
        model: The LLM model to use
        prompt: The prompt to send to the model
        max_tokens: Maximum number of tokens to generate

    Returns:
        The response from the LLM as a string

    Raises:
        ValueError: If the model is not supported or if API keys are missing
    """
    if model == LLMModel.CLAUDE_3_OPUS:
        if not anthropic_client:
            raise ValueError("Anthropic API key not found")
        response = anthropic_client.completions.create(
            model=model,
            prompt=prompt,
            max_tokens_to_sample=max_tokens,
        )
        return response.completion
    elif model in [LLMModel.GPT_4, LLMModel.GPT_3_5_TURBO]:
        if not openai.api_key:
            raise ValueError("OpenAI API key not found")
        response = openai.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content
    elif model == LLMModel.GROQ_LLM:
        if not groq_client:
            raise ValueError("Groq API key not found")
        response = groq_client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content
    else:
        raise ValueError(f"Unsupported model: {model}")


def infer_goal(prompt: str, model: LLMModel) -> str:
    """
    Infer the goal of a prompt using an LLM.

    Args:
        prompt: The prompt to analyze
        model: The LLM model to use for inference

    Returns:
        The inferred goal as a string
    """
    inference_prompt = f"""Given the following prompt, infer the likely goal or intention of the user:

Prompt: {prompt}

Provide a concise statement of the inferred goal in one sentence as a JSON dictionary with the key "goal" and the value being the inferred goal.
"""
    response = get_llm_response(model, inference_prompt)
    try:
        return json.loads(response)["goal"]
    except (json.JSONDecodeError, KeyError):
        # Fallback if JSON parsing fails
        return response.strip()


def analyze_fragments(
    prompt: str, model: LLMModel, goal: Optional[str] = None
) -> List[Fragment]:
    """
    Analyze prompt fragments for goal alignment.

    Args:
        prompt: The prompt to analyze
        model: The LLM model to use for analysis
        goal: The goal of the prompt (will be inferred if not provided)

    Returns:
        A list of Fragment objects with analysis results
    """
    if goal is None:
        goal = infer_goal(prompt, model)

    llm_prompt = f"""Analyze the following prompt for an LLM, keeping in mind the goal:

Prompt: {prompt}

Goal: {goal}

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

    response = get_llm_response(model, llm_prompt)
    try:
        analysis = json.loads(response)
        return [Fragment(**fragment) for fragment in analysis["fragments"]]
    except (json.JSONDecodeError, KeyError) as e:
        raise ValueError(f"Failed to parse fragment analysis: {e}")


def analyze_logs(prompt: str, model: LLMModel, goal: Optional[str] = None) -> List[Log]:
    """
    Analyze prompt for potential issues and generate logs.

    Args:
        prompt: The prompt to analyze
        model: The LLM model to use for analysis
        goal: The goal of the prompt (will be inferred if not provided)

    Returns:
        A list of Log objects with analysis results
    """
    if goal is None:
        goal = infer_goal(prompt, model)

    llm_prompt = f"""Analyze the following prompt for an LLM, keeping in mind the goal:

Prompt: {prompt}

Goal: {goal}

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

    response = get_llm_response(model, llm_prompt)
    try:
        analysis = json.loads(response)
        return [Log(**log) for log in analysis["logs"]]
    except (json.JSONDecodeError, KeyError) as e:
        raise ValueError(f"Failed to parse log analysis: {e}")


def analyze_prompt(
    prompt: str, model: LLMModel, goal: Optional[str] = None
) -> PromptAnalysis:
    """
    Perform a comprehensive analysis of a prompt.

    Args:
        prompt: The prompt to analyze
        model: The LLM model to use for analysis
        goal: The goal of the prompt (will be inferred if not provided)

    Returns:
        A PromptAnalysis object with analysis results
    """
    is_goal_inferred = False
    if goal is None:
        goal = infer_goal(prompt, model)
        is_goal_inferred = True

    llm_prompt = f"""Analyze the following prompt for an LLM, keeping in mind the {'inferred' if is_goal_inferred else 'provided'} goal:

Prompt: {prompt}

{'Inferred' if is_goal_inferred else 'Provided'} Goal: {goal}

Provide an overall analysis including:
1. Overall alignment of the prompt with the goal (1-10)
2. List of suggested improvements to better achieve the goal
3. Estimated effectiveness of the prompt in achieving the goal (1-10)

Provide your analysis in the following JSON format without any other text:
{{
  "overall_goal_alignment": overall_alignment_score,
  "suggested_improvements": ["improvement1", "improvement2", ...],
  "estimated_effectiveness": effectiveness_score,
  "inferred_goal": "{goal if is_goal_inferred else ''}",
  "is_goal_inferred": {str(is_goal_inferred).lower()}
}}
"""

    response = get_llm_response(model, llm_prompt)
    try:
        analysis = json.loads(response)
        return PromptAnalysis(**analysis)
    except (json.JSONDecodeError, KeyError) as e:
        raise ValueError(f"Failed to parse prompt analysis: {e}")


def generate_test(prompt: str, model: LLMModel, goal: Optional[str] = None) -> Test:
    """
    Generate a test case for a prompt.

    Args:
        prompt: The prompt to generate a test for
        model: The LLM model to use for test generation
        goal: The goal of the prompt (will be inferred if not provided)

    Returns:
        A Test object with the generated test case
    """
    if goal is None:
        goal = infer_goal(prompt, model)

    variables = re.findall(r"\{([^}]+)\}", prompt)

    llm_prompt = f"""Generate a test case for the following LLM prompt, keeping in mind the goal:

Prompt: {prompt}

Goal: {goal}

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

    response = get_llm_response(model, llm_prompt)
    try:
        test_data = json.loads(response)
        return Test(**test_data)
    except (json.JSONDecodeError, KeyError) as e:
        raise ValueError(f"Failed to parse test generation: {e}")


def execute_prompt(prompt: str, model: LLMModel) -> str:
    """
    Execute a prompt using the specified LLM.

    Args:
        prompt: The prompt to execute
        model: The LLM model to use for execution

    Returns:
        The response from the LLM as a string
    """
    return get_llm_response(model, prompt)
