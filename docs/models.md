# Model Selection

Choosing the right models is crucial for effective prompt engineering with Logus.

## Understanding Target vs Judge Models

Logus distinguishes between two types of models:

### Target Models

Target models are used to **execute** prompts - they're the models that will actually respond to your prompts in production.

**When to use Target Models:**
- Testing prompt performance
- Generating actual responses
- Cost-sensitive production environments
- Comparing model outputs

### Judge Models

Judge models are used to **analyze and evaluate** prompts. They're typically more capable models that can provide insightful feedback.

**When to use Judge Models:**
- Prompt analysis and evaluation
- Fragment analysis
- Test case generation
- Goal inference
- Log generation

## Available Models

### OpenAI Models

| Model | Type | Description | Best For |
|-------|------|-------------|----------|
| `gpt-4o` | Both | OpenAI's latest multimodal model | Complex analysis, high-quality responses |
| `gpt-4-turbo` | Both | Previous generation high-performance model | Balance of capability and cost |
| `gpt-3.5-turbo` | Target | Cost-effective general purpose model | Simple tasks, cost-sensitive applications |

### Anthropic Models

| Model | Type | Description | Best For |
|-------|------|-------------|----------|
| `claude-3-opus-20240229` | Judge | Most capable Claude model | Detailed analysis, complex reasoning |
| `claude-3-sonnet-20240229` | Both | Balance of intelligence and speed | General purpose tasks |
| `claude-3-haiku-20240307` | Target | Fastest and most compact model | Quick responses, simple tasks |

### Groq Models

| Model | Type | Description | Best For |
|-------|------|-------------|----------|
| `groq/llama3-70b-8192` | Both | Meta's Llama 3 70B | High-quality responses at speed |
| `groq/mixtral-8x7b-32768` | Target | Mixture of Experts model | Cost-effective inference |
| `groq/gemma-7b-it` | Target | Google's Gemma model | Lightweight tasks |

## Model Selection Strategy

### For Analysis (Judge Models)

1. **Prioritize Capability Over Cost**: Choose the most capable model available for analysis
2. **Claude-3 Opus**: Best for detailed, nuanced analysis
3. **GPT-4**: Excellent alternative with different analytical strengths
4. **Llama 3 70B**: Good balance of capability and availability

### For Execution (Target Models)

1. **Consider Cost**: Balance performance with budget constraints
2. **Match Task Complexity**: 
   - Simple tasks: GPT-3.5 Turbo, Mixtral, Gemma
   - Complex tasks: GPT-4, Claude-3 Sonnet, Llama 3 70B
3. **Speed Requirements**: Haiku and Groq models for fast responses
4. **Specialized Needs**: Claude for reasoning, GPT-4 for creativity

## Recommended Combinations

### Cost-Effective Analysis
- Judge: `claude-3-opus-20240229`
- Target: `groq/mixtral-8x7b-32768`

### High-Performance Analysis
- Judge: `claude-3-opus-20240229`
- Target: `gpt-4o`

### Speed-Focused Execution
- Judge: `claude-3-sonnet-20240229`
- Target: `groq/llama3-70b-8192`

### Balanced Approach
- Judge: `gpt-4o`
- Target: `claude-3-sonnet-20240229`

## Performance Considerations

### Latency

1. **Groq Models**: Generally fastest due to dedicated hardware
2. **Anthropic Models**: Moderate latency
3. **OpenAI Models**: Variable based on current load

### Cost

1. **Gemma 7B**: Least expensive
2. **Mixtral 8x7B**: Low cost, good performance
3. **GPT-3.5 Turbo**: Moderate cost
4. **Claude-3 Haiku**: Moderate cost
5. **Claude-3 Sonnet**: Higher cost
6. **Llama 3 70B**: Higher cost
7. **GPT-4 Series**: High cost
8. **Claude-3 Opus**: Highest cost

### Context Length

1. **Gemma 7B**: 8K tokens
2. **Mixtral 8x7B**: 32K tokens
3. **Claude-3 Haiku**: 200K tokens
4. **GPT-3.5 Turbo**: 16K tokens
5. **Claude-3 Sonnet**: 200K tokens
6. **GPT-4 Series**: 128K tokens
7. **Claude-3 Opus**: 200K tokens
8. **Llama 3 70B**: 8K tokens

## Best Practices

### 1. Match Model to Task
```python
# For detailed analysis, use a capable judge model
analysis = analyze_prompt(prompt, JudgeLLMModel.CLAUDE_3_OPUS)

# For cost-effective execution, use a lighter target model
response = execute_prompt(prompt, TargetLLMModel.GROQ_MIXTRAL_8X7B)
```

### 2. Test Across Models
```python
# Compare responses across different target models
models_to_test = [
    TargetLLMModel.GPT_3_5_TURBO,
    TargetLLMModel.GROQ_MIXTRAL_8X7B,
    TargetLLMModel.CLAUDE_3_HAIKU
]

for model in models_to_test:
    response = execute_prompt(prompt, model)
    # Compare and evaluate responses
```

### 3. Use Powerful Models for Analysis
```python
# Even if using a simple target model, use a powerful judge
response = execute_prompt(prompt, TargetLLMModel.GROQ_GEMMA_7B)
analysis = analyze_prompt(prompt, JudgeLLMModel.GPT_4)  # More capable for analysis
```

### 4. Consider Context Requirements
```python
# For prompts requiring long context, choose models with sufficient context windows
if len(prompt) > 10000:  # Characters, approximating tokens
    target_model = TargetLLMModel.CLAUDE_3_SONNET  # 200K context
else:
    target_model = TargetLLMModel.GPT_3_5_TURBO  # 16K context
```

Choosing the right models for your specific use case is key to getting the most value from Logus.