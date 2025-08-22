"""
Backward compatibility module for Blogus.
"""

from blogus.web import app

from blogus.core import (
    TargetLLMModel,
    JudgeLLMModel,
    analyze_prompt,
    generate_test,
    execute_prompt,
    infer_goal,
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
