"""
Backward compatibility module for Logus.
"""

# For backward compatibility, import the main FastAPI app
from logus.web import app

# Also import core functionality
from logus.core import (
    LLMModel,
    Fragment,
    Log,
    Test,
    PromptAnalysis,
    get_llm_response,
    infer_goal,
    analyze_fragments,
    analyze_logs,
    analyze_prompt,
    generate_test,
    execute_prompt,
)

__all__ = [
    "app",
    "LLMModel",
    "Fragment",
    "Log",
    "Test",
    "PromptAnalysis",
    "get_llm_response",
    "infer_goal",
    "analyze_fragments",
    "analyze_logs",
    "analyze_prompt",
    "generate_test",
    "execute_prompt",
]
