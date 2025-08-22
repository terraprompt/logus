"""
Example usage of the Logus library.
"""

from logus.core import LLMModel, analyze_prompt, generate_test

# Example prompt
prompt = """
You are an AI assistant that helps people find information.
Answer the following question based on the provided context.

Context: {context}
Question: {question}

Please provide a concise and accurate answer.
"""

# Example usage of prompt analysis
print("Analyzing prompt...")
analysis = analyze_prompt(prompt, LLMModel.GPT_4)
print(f"Overall goal alignment: {analysis.overall_goal_alignment}/10")
print(f"Estimated effectiveness: {analysis.estimated_effectiveness}/10")
print("Suggested improvements:")
for i, improvement in enumerate(analysis.suggested_improvements, 1):
    print(f"  {i}. {improvement}")

# Example usage of test generation
print("\nGenerating test case...")
test_case = generate_test(prompt, LLMModel.GPT_4)
print("Generated test case:")
print(f"Input: {test_case.input}")
print(f"Expected output: {test_case.expected_output}")
print(f"Goal relevance: {test_case.goal_relevance}/5")
