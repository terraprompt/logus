#!/usr/bin/env python3
"""
Example: Cross-model comparison
"""

from blogus.core import (
    execute_prompt,
    TargetLLMModel
)

def main():
    # Define a prompt to test
    prompt = "Explain the concept of photosynthesis in simple terms."
    
    print("=== Cross-Model Comparison Example ===")
    print(f"Prompt: {prompt}")
    print()
    
    # List of models to test
    models = [
        TargetLLMModel.GPT_3_5_TURBO,
        TargetLLMModel.GROQ_MIXTRAL_8X7B,
        TargetLLMModel.CLAUDE_3_HAIKU
    ]
    
    # Execute prompt on each model
    for model in models:
        print(f"--- Response from {model.value} ---")
        try:
            response = execute_prompt(prompt, model)
            # Truncate long responses for display
            truncated_response = response[:300] + "..." if len(response) > 300 else response
            print(truncated_response)
        except Exception as e:
            print(f"Error: {e}")
        print()

if __name__ == "__main__":
    main()