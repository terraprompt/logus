# Web Module API

This document provides detailed API documentation for the `logus.web` module.

## Module Overview

The `web` module provides the web interface for Logus using FastAPI.

```python
from logus import web
```

## FastAPI Application

### app

The main FastAPI application instance.

```python
app = FastAPI()
```

## Request Models

### FragmentAnalysisRequest

Request model for fragment analysis endpoint.

```python
class FragmentAnalysisRequest(BaseModel):
    prompt: str
    target_model: TargetLLMModel
    judge_model: JudgeLLMModel
    goal: Optional[str] = None
```

### FragmentResponse

Response model for fragment analysis endpoint.

```python
class FragmentResponse(BaseModel):
    text: str
    type: str
    goal_alignment: int
    improvement_suggestion: str
```

### LogResponse

Response model for log analysis endpoint.

```python
class LogResponse(BaseModel):
    type: str
    message: str
```

### PromptAnalysisRequest

Request model for prompt analysis endpoint.

```python
class PromptAnalysisRequest(BaseModel):
    prompt: str
    target_model: TargetLLMModel
    judge_model: JudgeLLMModel
    goal: Optional[str] = None
```

### PromptAnalysisResponse

Response model for prompt analysis endpoint.

```python
class PromptAnalysisResponse(BaseModel):
    overall_goal_alignment: int
    suggested_improvements: List[str]
    estimated_effectiveness: int
    inferred_goal: Optional[str] = None
    is_goal_inferred: bool
```

### TestGenerationRequest

Request model for test generation endpoint.

```python
class TestGenerationRequest(BaseModel):
    prompt: str
    target_model: TargetLLMModel
    judge_model: JudgeLLMModel
    goal: Optional[str] = None
```

### TestResponse

Response model for test generation endpoint.

```python
class TestResponse(BaseModel):
    input: Dict[str, str]
    expected_output: str
    goal_relevance: int
```

### PromptExecutionRequest

Request model for prompt execution endpoint.

```python
class PromptExecutionRequest(BaseModel):
    prompt: str
    target_model: TargetLLMModel
```

### GoalInferenceRequest

Request model for goal inference endpoint.

```python
class GoalInferenceRequest(BaseModel):
    prompt: str
    judge_model: JudgeLLMModel
```

## API Endpoints

### POST /api/infer-goal

Infer the goal of a prompt.

```python
@app.post("/api/infer-goal", response_model=str)
async def infer_goal_endpoint(request: GoalInferenceRequest)
```

**Request Body:**
```json
{
  "prompt": "string",
  "judge_model": "string"
}
```

**Response:**
```json
"string"
```

**Example Request:**
```json
{
  "prompt": "You are a Python programming tutor",
  "judge_model": "gpt-4o"
}
```

**Example Response:**
```json
"Teach Python programming concepts effectively"
```

### POST /api/analyze-fragments

Analyze prompt fragments for goal alignment.

```python
@app.post("/api/analyze-fragments", response_model=List[FragmentResponse])
async def analyze_fragments_endpoint(request: FragmentAnalysisRequest)
```

**Request Body:**
```json
{
  "prompt": "string",
  "target_model": "string",
  "judge_model": "string",
  "goal": "string (optional)"
}
```

**Response:**
```json
[
  {
    "text": "string",
    "type": "string",
    "goal_alignment": 0,
    "improvement_suggestion": "string"
  }
]
```

**Example Request:**
```json
{
  "prompt": "You are a helpful assistant. Always be polite.",
  "target_model": "gpt-4o",
  "judge_model": "claude-3-opus-20240229"
}
```

**Example Response:**
```json
[
  {
    "text": "You are a helpful assistant.",
    "type": "instruction",
    "goal_alignment": 5,
    "improvement_suggestion": "Consider specifying what constitutes helpful behavior"
  },
  {
    "text": "Always be polite.",
    "type": "constraint",
    "goal_alignment": 4,
    "improvement_suggestion": "Define what politeness means in this context"
  }
]
```

### POST /api/analyze-logs

Generate logs for a prompt.

```python
@app.post("/api/analyze-logs", response_model=List[LogResponse])
async def analyze_logs_endpoint(request: PromptAnalysisRequest)
```

**Request Body:**
```json
{
  "prompt": "string",
  "target_model": "string",
  "judge_model": "string",
  "goal": "string (optional)"
}
```

**Response:**
```json
[
  {
    "type": "string",
    "message": "string"
  }
]
```

**Example Request:**
```json
{
  "prompt": "You are a helpful assistant.",
  "target_model": "gpt-4o",
  "judge_model": "claude-3-opus-20240229"
}
```

**Example Response:**
```json
[
  {
    "type": "warning",
    "message": "The prompt is very brief and may not provide sufficient guidance"
  },
  {
    "type": "info",
    "message": "Consider adding specific examples of desired response formats"
  }
]
```

### POST /api/analyze-prompt

Perform a comprehensive analysis of a prompt.

```python
@app.post("/api/analyze-prompt", response_model=PromptAnalysisResponse)
async def analyze_prompt_endpoint(request: PromptAnalysisRequest)
```

**Request Body:**
```json
{
  "prompt": "string",
  "target_model": "string",
  "judge_model": "string",
  "goal": "string (optional)"
}
```

**Response:**
```json
{
  "overall_goal_alignment": 0,
  "suggested_improvements": ["string"],
  "estimated_effectiveness": 0,
  "inferred_goal": "string (optional)",
  "is_goal_inferred": true
}
```

**Example Request:**
```json
{
  "prompt": "You are a helpful assistant.",
  "target_model": "gpt-4o",
  "judge_model": "claude-3-opus-20240229"
}
```

**Example Response:**
```json
{
  "overall_goal_alignment": 6,
  "suggested_improvements": [
    "Specify the type of assistance you provide",
    "Add examples of desired response formats",
    "Include constraints on behavior"
  ],
  "estimated_effectiveness": 5,
  "inferred_goal": "Provide helpful responses to user queries",
  "is_goal_inferred": true
}
```

### POST /api/generate-test

Generate a test case for a prompt.

```python
@app.post("/api/generate-test", response_model=TestResponse)
async def generate_test_endpoint(request: TestGenerationRequest)
```

**Request Body:**
```json
{
  "prompt": "string",
  "target_model": "string",
  "judge_model": "string",
  "goal": "string (optional)"
}
```

**Response:**
```json
{
  "input": {
    "string": "string"
  },
  "expected_output": "string",
  "goal_relevance": 0
}
```

**Example Request:**
```json
{
  "prompt": "Translate {text} to {language}",
  "target_model": "gpt-4o",
  "judge_model": "claude-3-opus-20240229"
}
```

**Example Response:**
```json
{
  "input": {
    "text": "Hello, how are you?",
    "language": "French"
  },
  "expected_output": "Bonjour, comment allez-vous?",
  "goal_relevance": 5
}
```

### POST /api/execute-prompt

Execute a prompt using the specified target LLM.

```python
@app.post("/api/execute-prompt", response_model=str)
async def execute_prompt_endpoint(request: PromptExecutionRequest)
```

**Request Body:**
```json
{
  "prompt": "string",
  "target_model": "string"
}
```

**Response:**
```json
"string"
```

**Example Request:**
```json
{
  "prompt": "Explain quantum computing in simple terms.",
  "target_model": "gpt-4o"
}
```

**Example Response:**
```json
"Quantum computing is a type of computing that uses quantum bits..."
```

### GET /

Serve the main web interface.

```python
@app.get("/")
async def index(request: Request)
```

**Response:**
- Renders the main index.html template
- Returns JSON message if templates are not available

### GET /agent

Serve the agent interface.

```python
@app.get("/agent")
async def agent(request: Request)
```

**Response:**
- Renders the agent.html template
- Returns JSON message if templates are not available

## Usage Examples

### Python Client Example

```python
import requests

# Analyze a prompt
response = requests.post(
    "http://localhost:8000/api/analyze-prompt",
    json={
        "prompt": "You are a helpful assistant.",
        "target_model": "gpt-4o",
        "judge_model": "claude-3-opus-20240229"
    }
)

analysis = response.json()
print(f"Alignment: {analysis['overall_goal_alignment']}/10")
```

### JavaScript Client Example

```javascript
// Generate a test case
fetch('http://localhost:8000/api/generate-test', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    prompt: 'Translate {text} to {language}',
    target_model: 'gpt-4o',
    judge_model: 'claude-3-opus-20240229'
  }),
})
.then(response => response.json())
.then(data => {
  console.log('Test case:', data);
});
```

The web module provides a RESTful API for integrating Logus functionality into web applications.