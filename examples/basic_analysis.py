#!/usr/bin/env python3
"""
Example: Basic prompt analysis and execution
"""

from blogus.core import (
    analyze_prompt,
    execute_prompt,
    TargetLLMModel,
    JudgeLLMModel
)

def main():
    # Define a prompt to analyze
    prompt = "You are a helpful assistant that provides concise and accurate responses."
    
    print("=== Prompt Analysis Example ===")
    print(f"Prompt: {prompt}")
    print()
    
    # Analyze the prompt
    analysis = analyze_prompt(prompt, JudgeLLMModel.GPT_4)
    
    print(f"Overall Goal Alignment: {analysis.overall_goal_alignment}/10")
    print(f"Estimated Effectiveness: {analysis.estimated_effectiveness}/10")
    
    if analysis.is_goal_inferred:
        print(f"Inferred Goal: {analysis.inferred_goal}")
    
    print("\nSuggested Improvements:")
    for i, suggestion in enumerate(analysis.suggested_improvements, 1):
        print(f"  {i}. {suggestion}")
    
    print("\n=== Prompt Execution Example ===")
    
    # Execute the prompt with a test question
    test_question = "What is the capital of France?"
    full_prompt = f"{prompt}\n\nUser: {test_question}"
    
    response = execute_prompt(full_prompt, TargetLLMModel.GPT_3_5_TURBO)
    
    print(f"Question: {test_question}")
    print(f"Response: {response}")

if __name__ == "__main__":
    main()