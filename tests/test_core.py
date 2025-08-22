"""
Tests for the core functionality of Logus.
"""

import pytest
from unittest.mock import patch, MagicMock
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

# Test data
SAMPLE_PROMPT = "You are an AI assistant that helps people find information."
SAMPLE_GOAL = "Help users find information"


@pytest.fixture
def mock_llm_response():
    """Mock LLM response for testing."""
    return "This is a mock LLM response"


def test_llm_model_enum():
    """Test that LLMModel enum has the correct values."""
    assert LLMModel.CLAUDE_3_OPUS == "claude-3-opus-20240229"
    assert LLMModel.GPT_4 == "gpt-4o"
    assert LLMModel.GPT_3_5_TURBO == "gpt-3.5-turbo"
    assert LLMModel.GROQ_LLM == "mixtral-8x7b-32768"


def test_fragment_creation():
    """Test Fragment class creation."""
    fragment = Fragment(
        text="Sample text",
        type="instruction",
        goal_alignment=5,
        improvement_suggestion="Improve clarity",
    )
    assert fragment.text == "Sample text"
    assert fragment.type == "instruction"
    assert fragment.goal_alignment == 5
    assert fragment.improvement_suggestion == "Improve clarity"


def test_log_creation():
    """Test Log class creation."""
    log = Log(type="info", message="Test message")
    assert log.type == "info"
    assert log.message == "Test message"


def test_test_creation():
    """Test Test class creation."""
    test = Test(
        input={"question": "What is AI?"},
        expected_output="AI is artificial intelligence",
        goal_relevance=5,
    )
    assert test.input == {"question": "What is AI?"}
    assert test.expected_output == "AI is artificial intelligence"
    assert test.goal_relevance == 5


def test_prompt_analysis_creation():
    """Test PromptAnalysis class creation."""
    analysis = PromptAnalysis(
        overall_goal_alignment=8,
        suggested_improvements=["Add more context", "Clarify instructions"],
        estimated_effectiveness=7,
        inferred_goal="Help users understand AI",
        is_goal_inferred=True,
    )
    assert analysis.overall_goal_alignment == 8
    assert analysis.suggested_improvements == [
        "Add more context",
        "Clarify instructions",
    ]
    assert analysis.estimated_effectiveness == 7
    assert analysis.inferred_goal == "Help users understand AI"
    assert analysis.is_goal_inferred == True


@patch("logus.core.anthropic_client")
def test_get_llm_response_claude(mock_anthropic_client):
    """Test get_llm_response with Claude model."""
    mock_response = MagicMock()
    mock_response.completion = "Claude response"
    mock_anthropic_client.completions.create.return_value = mock_response

    result = get_llm_response(LLMModel.CLAUDE_3_OPUS, "Test prompt")
    assert result == "Claude response"


@patch("logus.core.openai")
def test_get_llm_response_gpt(mock_openai):
    """Test get_llm_response with GPT model."""
    mock_choice = MagicMock()
    mock_choice.message.content = "GPT response"
    mock_response = MagicMock()
    mock_response.choices = [mock_choice]
    mock_openai.chat.completions.create.return_value = mock_response

    result = get_llm_response(LLMModel.GPT_4, "Test prompt")
    assert result == "GPT response"


@patch("logus.core.groq_client")
def test_get_llm_response_groq(mock_groq_client):
    """Test get_llm_response with Groq model."""
    mock_choice = MagicMock()
    mock_choice.message.content = "Groq response"
    mock_response = MagicMock()
    mock_response.choices = [mock_choice]
    mock_groq_client.chat.completions.create.return_value = mock_response

    result = get_llm_response(LLMModel.GROQ_LLM, "Test prompt")
    assert result == "Groq response"


@patch("logus.core.get_llm_response")
def test_infer_goal(mock_get_llm_response):
    """Test infer_goal function."""
    mock_get_llm_response.return_value = '{"goal": "Help users find information"}'

    result = infer_goal(SAMPLE_PROMPT, LLMModel.GPT_4)
    assert result == "Help users find information"


@patch("logus.core.get_llm_response")
def test_analyze_fragments(mock_get_llm_response):
    """Test analyze_fragments function."""
    mock_get_llm_response.return_value = '{"fragments": [{"text": "Sample text", "type": "instruction", "goal_alignment": 5, "improvement_suggestion": "Improve clarity"}]}'

    fragments = analyze_fragments(SAMPLE_PROMPT, LLMModel.GPT_4, SAMPLE_GOAL)
    assert len(fragments) == 1
    assert isinstance(fragments[0], Fragment)


@patch("logus.core.get_llm_response")
def test_analyze_logs(mock_get_llm_response):
    """Test analyze_logs function."""
    mock_get_llm_response.return_value = (
        '{"logs": [{"type": "info", "message": "Test log message"}]}'
    )

    logs = analyze_logs(SAMPLE_PROMPT, LLMModel.GPT_4, SAMPLE_GOAL)
    assert len(logs) == 1
    assert isinstance(logs[0], Log)


@patch("logus.core.get_llm_response")
def test_analyze_prompt(mock_get_llm_response):
    """Test analyze_prompt function."""
    mock_get_llm_response.return_value = '{"overall_goal_alignment": 8, "suggested_improvements": ["Add more context"], "estimated_effectiveness": 7, "inferred_goal": "", "is_goal_inferred": false}'

    analysis = analyze_prompt(SAMPLE_PROMPT, LLMModel.GPT_4, SAMPLE_GOAL)
    assert isinstance(analysis, PromptAnalysis)
    assert analysis.overall_goal_alignment == 8


@patch("logus.core.get_llm_response")
def test_generate_test(mock_get_llm_response):
    """Test generate_test function."""
    mock_get_llm_response.return_value = '{"input": {"question": "What is AI?"}, "expected_output": "AI is artificial intelligence", "goal_relevance": 5}'

    test_case = generate_test(SAMPLE_PROMPT, LLMModel.GPT_4, SAMPLE_GOAL)
    assert isinstance(test_case, Test)
    assert test_case.input == {"question": "What is AI?"}


@patch("logus.core.get_llm_response")
def test_execute_prompt(mock_get_llm_response):
    """Test execute_prompt function."""
    mock_get_llm_response.return_value = "This is a test response"

    result = execute_prompt(SAMPLE_PROMPT, LLMModel.GPT_4)
    assert result == "This is a test response"
