#!/usr/bin/env python3
"""
Creates an Anthropic Managed Agent (Data analyst) with Amplitude MCP integration,
then creates an environment and demonstrates starting a session.
"""

import os
import anthropic

SYSTEM_PROMPT = """You analyze data. Given a dataset (file path, URL, or query) and a question:

1. Load the data and print its shape, column names, dtypes, and a small sample. Always look before you compute.
2. Clean obvious issues — nulls, duplicates, type mismatches — and note what you changed.
3. Answer the question with code. Prefer pandas/polars for tabular work, matplotlib/plotly for charts. Show intermediate results so your reasoning is checkable.
4. For product-analytics questions, query Amplitude directly — event funnels, retention cohorts, property breakdowns — and link the chart.
5. Save any charts or derived tables to /mnt/session/outputs/ and summarize findings in plain language, including caveats (sample size, missing data, correlation-vs-causation).

Default to simple, readable analysis over clever one-liners. A clear bar chart usually beats a dense heatmap."""


def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable is required")

    client = anthropic.Anthropic(api_key=api_key)

    print("Creating Data analyst agent...")
    agent = client.beta.agents.create(
        name="Data analyst",
        model="claude-sonnet-4-6",
        system=SYSTEM_PROMPT,
        tools=[
            {"type": "agent_toolset_20260401"},
            {"type": "mcp_toolset", "mcp_server_name": "amplitude"},
        ],
        mcp_servers=[
            {
                "type": "url",
                "name": "amplitude",
                "url": "https://mcp.amplitude.com/mcp",
            }
        ],
        betas=["managed-agents-2026-04-01"],
    )
    print(f"Agent created: id={agent.id}, name={agent.name}")

    print("\nCreating environment...")
    env = client.beta.environments.create(
        agent_id=agent.id,
        name="data-analyst-env",
        betas=["managed-agents-2026-04-01"],
    )
    print(f"Environment created: id={env.id}")

    print("\nAgent setup complete.")
    print(f"  Agent ID:      {agent.id}")
    print(f"  Environment ID: {env.id}")
    print("\nTo start a session:")
    print(f'  session = client.beta.sessions.create(agent_id="{agent.id}", environment_id="{env.id}")')

    return agent, env


if __name__ == "__main__":
    main()
