# Web Interface

Blogus provides a web-based interface for interactive prompt engineering with a rich user experience.

## Starting the Web Interface

To start the web interface:

```bash
# If installed with web extras
blogus-web

# Or directly with Python
python -m blogus.web
```

The web interface will be available at `http://localhost:8000`.

## Interface Overview

The web interface consists of several key components:

### 1. Prompt Editor

A rich text editor for creating and modifying prompts with:
- Syntax highlighting
- Real-time analysis feedback
- Variable detection
- Auto-save functionality

### 2. Analysis Panel

Comprehensive analysis results displayed in an easy-to-read format:
- Overall goal alignment score
- Effectiveness estimates
- Improvement suggestions
- Fragment breakdown

### 3. Test Case Manager

Tools for generating, viewing, and managing test cases:
- Automatic test case generation
- Test case editing
- Bulk operations
- Export functionality

### 4. Execution Environment

A sandbox for testing prompts with different models:
- Model selection dropdown
- Variable input forms
- Response visualization
- Comparison tools

### 5. History and Versioning

Track prompt evolution over time:
- Version history
- Diff views
- Rollback capability
- Annotation support

## Key Features

### Real-time Analysis

As you type in the prompt editor, Blogus provides real-time feedback:
- Syntax validation
- Variable detection
- Preliminary alignment scoring

### Interactive Fragment Analysis

Click on any fragment to see detailed analysis:
- Type identification
- Alignment scoring
- Improvement suggestions
- Impact assessment

### Test Case Generation

Generate test cases with a single click:
- Automatic variable detection
- Smart value generation
- Relevance scoring
- One-click execution

### Cross-Model Testing

Test your prompt across multiple models simultaneously:
- Side-by-side comparison
- Consistency checking
- Performance metrics
- Cost estimation

### Collaboration Tools

Share your work with team members:
- Export to various formats
- Shareable links
- Commenting system
- Version comparison

## API Endpoints

The web interface is built on a RESTful API that you can also use directly:

### Prompt Analysis
```
POST /api/analyze-prompt
{
  "prompt": "Your prompt here",
  "target_model": "gpt-4o",
  "judge_model": "claude-3-opus-20240229",
  "goal": "Optional explicit goal"
}
```

### Fragment Analysis
```
POST /api/analyze-fragments
{
  "prompt": "Your prompt here",
  "target_model": "gpt-4o",
  "judge_model": "claude-3-opus-20240229",
  "goal": "Optional explicit goal"
}
```

### Test Generation
```
POST /api/generate-test
{
  "prompt": "Your prompt here",
  "target_model": "gpt-4o",
  "judge_model": "claude-3-opus-20240229",
  "goal": "Optional explicit goal"
}
```

### Prompt Execution
```
POST /api/execute-prompt
{
  "prompt": "Your prompt here",
  "target_model": "gpt-4o"
}
```

### Goal Inference
```
POST /api/infer-goal
{
  "prompt": "Your prompt here",
  "judge_model": "claude-3-opus-20240229"
}
```

## Customization

### Themes

The web interface supports multiple themes:
- Light mode
- Dark mode
- High contrast mode

### Layout Options

Customize the interface layout:
- Editor position (left/right)
- Panel visibility
- Split ratios
- Font sizes

### Keyboard Shortcuts

Common keyboard shortcuts:
- `Ctrl+S`: Save current prompt
- `Ctrl+Enter`: Execute prompt
- `Ctrl+Shift+A`: Analyze prompt
- `Ctrl+T`: Generate test case

## Best Practices

1. **Use Real-time Feedback**: Take advantage of the immediate analysis as you type
2. **Leverage Fragment Analysis**: Drill down into specific parts of complex prompts
3. **Generate Comprehensive Tests**: Create diverse test cases to validate prompt robustness
4. **Compare Across Models**: Ensure consistent performance across different target models
5. **Track Version History**: Keep detailed records of prompt evolution
6. **Collaborate Effectively**: Use sharing features to get feedback from team members

The web interface provides a powerful, intuitive environment for all your prompt engineering needs.