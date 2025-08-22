# Core Concepts

Understanding the core concepts of Logus will help you make the most of its features.

## Target vs Judge Models

One of the key innovations in Logus is the separation of **target models** and **judge models**:

### Target Models

Target models are used to **execute** prompts - they're the models that will actually respond to your prompts in production. Examples include:
- GPT-4 for generating text responses
- Claude for complex reasoning tasks
- Mixtral for cost-effective inference

### Judge Models

Judge models are used to **analyze and evaluate** prompts. They're typically more capable models that can provide insightful feedback. Examples include:
- Claude-3 Opus for detailed analysis
- GPT-4 for comprehensive evaluation

### Benefits of Separation

1. **Cost Optimization**: Use cheaper models for execution, more capable (and expensive) models for analysis
2. **Specialization**: Choose models optimized for their specific roles
3. **Flexibility**: Test prompts on multiple target models while using a consistent judge
4. **Accuracy**: Get better analysis from more capable models

## Prompt Analysis

Logus provides several types of prompt analysis:

### Overall Analysis

A comprehensive evaluation including:
- Goal alignment scoring
- Effectiveness estimates
- Improvement suggestions

### Fragment Analysis

Granular analysis of prompt components:
- Identification of instruction, context, example, and constraint fragments
- Individual fragment alignment scoring
- Specific improvement suggestions per fragment

### Log Generation

Structured feedback in the form of:
- Informational messages about prompt design
- Warnings about potential issues
- Errors that will likely impact performance

## Test Case Generation

Logus can automatically generate test cases for your prompts:
- Variable identification and value generation
- Expected output prediction
- Goal relevance scoring

## Goal Inference

When you don't explicitly specify a prompt's goal, Logus can infer it:
- Automatic goal determination
- Integration with all analysis functions
- Clear indication when goals are inferred vs. provided

## The Prompt Development Lifecycle

Logus supports the complete prompt engineering workflow:
1. Initial creation
2. Analysis and evaluation
3. Iterative enhancement
4. Cross-model validation
5. Test dataset generation
6. Performance monitoring

Understanding these concepts will help you leverage Logus effectively in your prompt engineering practice.