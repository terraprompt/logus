"""
Test LiteLLM integration with separate target and judge models.
"""

import pytest
from blogus.core import (
    TargetLLMModel,
    JudgeLLMModel,
    get_llm_response,
    execute_prompt,
    infer_goal,
)


def test_get_llm_response():
    """Test that we can get a response from an LLM via LiteLLM."""
    # This test requires API keys to be set in the environment
    # It's marked as slow since it makes actual API calls
    pytest.skip("Skipping API-dependent test")


def test_execute_prompt():
    """Test that we can execute a prompt with a target model."""
    # This test requires API keys to be set in the environment
    # It's marked as slow since it makes actual API calls
    pytest.skip("Skipping API-dependent test")


def test_infer_goal():
    """Test that we can infer a goal with a judge model."""
    # This test requires API keys to be set in the environment
    # It's marked as slow since it makes actual API calls
    pytest.skip("Skipping API-dependent test")


def test_target_and_judge_model_enums():
    """Test that our model enums are properly defined."""
    # Check that we have some models defined
    assert len(list(TargetLLMModel)) > 0
    assert len(list(JudgeLLMModel)) > 0
    
    # Check that common models are present
    assert "gpt-4o" in [m.value for m in TargetLLMModel]
    assert "gpt-4o" in [m.value for m in JudgeLLMModel]
    assert "claude-3-opus-20240229" in [m.value for m in TargetLLMModel]
    assert "claude-3-opus-20240229" in [m.value for m in JudgeLLMModel]