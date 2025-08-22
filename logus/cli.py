"""
Command-line interface for Logus.
"""

import click
from logus.core import (
    LLMModel,
    analyze_prompt,
    analyze_fragments,
    analyze_logs,
    generate_test,
    execute_prompt,
    infer_goal,
)


@click.group()
def cli():
    """Logus: A tool for crafting, analyzing, and perfecting AI prompts."""
    pass


@cli.command()
@click.argument("prompt", type=str)
@click.option(
    "--model",
    type=click.Choice([m.value for m in LLMModel]),
    default=LLMModel.GPT_4,
    help="LLM model to use",
)
@click.option(
    "--goal",
    type=str,
    default=None,
    help="Goal for the prompt (will be inferred if not provided)",
)
def analyze(prompt, model, goal):
    """Analyze a prompt for effectiveness and alignment with a goal."""
    model = LLMModel(model)

    click.echo(f"Analyzing prompt with {model.value}...")

    # Perform analysis
    analysis = analyze_prompt(prompt, model, goal)

    click.echo("\nPrompt Analysis Results:")
    click.echo("=" * 50)
    click.echo(f"Overall Goal Alignment: {analysis.overall_goal_alignment}/10")
    click.echo(f"Estimated Effectiveness: {analysis.estimated_effectiveness}/10")

    if analysis.is_goal_inferred:
        click.echo(f"Inferred Goal: {analysis.inferred_goal}")

    click.echo("\nSuggested Improvements:")
    for i, improvement in enumerate(analysis.suggested_improvements, 1):
        click.echo(f"  {i}. {improvement}")


@cli.command()
@click.argument("prompt", type=str)
@click.option(
    "--model",
    type=click.Choice([m.value for m in LLMModel]),
    default=LLMModel.GPT_4,
    help="LLM model to use",
)
@click.option(
    "--goal",
    type=str,
    default=None,
    help="Goal for the prompt (will be inferred if not provided)",
)
def fragments(prompt, model, goal):
    """Analyze prompt fragments for goal alignment."""
    model = LLMModel(model)

    click.echo(f"Analyzing prompt fragments with {model.value}...")

    # Analyze fragments
    fragments = analyze_fragments(prompt, model, goal)

    click.echo("\nFragment Analysis Results:")
    click.echo("=" * 50)
    for i, fragment in enumerate(fragments, 1):
        click.echo(f"\nFragment {i}:")
        click.echo(f"  Text: {fragment.text}")
        click.echo(f"  Type: {fragment.type}")
        click.echo(f"  Goal Alignment: {fragment.goal_alignment}/5")
        click.echo(f"  Improvement Suggestion: {fragment.improvement_suggestion}")


@cli.command()
@click.argument("prompt", type=str)
@click.option(
    "--model",
    type=click.Choice([m.value for m in LLMModel]),
    default=LLMModel.GPT_4,
    help="LLM model to use",
)
@click.option(
    "--goal",
    type=str,
    default=None,
    help="Goal for the prompt (will be inferred if not provided)",
)
def logs(prompt, model, goal):
    """Generate logs for a prompt."""
    model = LLMModel(model)

    click.echo(f"Generating logs with {model.value}...")

    # Generate logs
    logs = analyze_logs(prompt, model, goal)

    click.echo("\nPrompt Logs:")
    click.echo("=" * 50)
    for log in logs:
        click.echo(f"[{log.type.upper()}] {log.message}")


@cli.command()
@click.argument("prompt", type=str)
@click.option(
    "--model",
    type=click.Choice([m.value for m in LLMModel]),
    default=LLMModel.GPT_4,
    help="LLM model to use",
)
@click.option(
    "--goal",
    type=str,
    default=None,
    help="Goal for the prompt (will be inferred if not provided)",
)
def test(prompt, model, goal):
    """Generate a test case for a prompt."""
    model = LLMModel(model)

    click.echo(f"Generating test case with {model.value}...")

    # Generate test
    test_case = generate_test(prompt, model, goal)

    click.echo("\nGenerated Test Case:")
    click.echo("=" * 50)
    click.echo("Input:")
    for key, value in test_case.input.items():
        click.echo(f"  {key}: {value}")
    click.echo(f"\nExpected Output: {test_case.expected_output}")
    click.echo(f"Goal Relevance: {test_case.goal_relevance}/5")


@cli.command()
@click.argument("prompt", type=str)
@click.option(
    "--model",
    type=click.Choice([m.value for m in LLMModel]),
    default=LLMModel.GPT_4,
    help="LLM model to use",
)
def execute(prompt, model):
    """Execute a prompt with the specified LLM."""
    model = LLMModel(model)

    click.echo(f"Executing prompt with {model.value}...")

    # Execute prompt
    result = execute_prompt(prompt, model)

    click.echo("\nExecution Result:")
    click.echo("=" * 50)
    click.echo(result)


@cli.command()
@click.argument("prompt", type=str)
@click.option(
    "--model",
    type=click.Choice([m.value for m in LLMModel]),
    default=LLMModel.GPT_4,
    help="LLM model to use",
)
def goal(prompt, model):
    """Infer the goal of a prompt."""
    model = LLMModel(model)

    click.echo(f"Inferring goal with {model.value}...")

    # Infer goal
    inferred_goal = infer_goal(prompt, model)

    click.echo("\nInferred Goal:")
    click.echo("=" * 50)
    click.echo(inferred_goal)


if __name__ == "__main__":
    cli()
