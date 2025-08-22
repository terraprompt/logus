#!/usr/bin/env python3
"""
Example: Test case generation for parameterized prompts
"""

from blogus.core import (
    generate_test,
    JudgeLLMModel
)
import json

def main():
    # Define a parameterized prompt template
    prompt_template = "Translate the following {source_language} text to {target_language}: {text}"
    
    print("=== Test Case Generation Example ===")
    print(f"Prompt Template: {prompt_template}")
    print()
    
    # Generate multiple test cases
    print("Generating test cases...")
    test_cases = []
    
    for i in range(3):
        print(f"Generating test case {i+1}...")
        test_case = generate_test(prompt_template, JudgeLLMModel.GPT_4)
        
        test_cases.append({
            'id': i + 1,
            'input': test_case.input,
            'expected_output': test_case.expected_output,
            'goal_relevance': test_case.goal_relevance
        })
        
        print(f"  Input: {test_case.input}")
        print(f"  Expected Output: {test_case.expected_output}")
        print(f"  Goal Relevance: {test_case.goal_relevance}/5")
        print()
    
    # Save test cases to a JSON file
    test_dataset = {
        'prompt_template': prompt_template,
        'test_cases': test_cases
    }
    
    with open('translation_tests.json', 'w') as f:
        json.dump(test_dataset, f, indent=2)
    
    print(f"Saved {len(test_cases)} test cases to translation_tests.json")

if __name__ == "__main__":
    main()