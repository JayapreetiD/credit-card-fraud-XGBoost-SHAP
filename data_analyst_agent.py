#!/usr/bin/env python3
"""
Data analyst agent powered by xAI Grok.
Answers data analysis questions using the grok-3 model.
"""

import os
from openai import OpenAI

SYSTEM_PROMPT = """You analyze data. Given a dataset (file path, URL, or query) and a question:

1. Load the data and print its shape, column names, dtypes, and a small sample. Always look before you compute.
2. Clean obvious issues — nulls, duplicates, type mismatches — and note what you changed.
3. Answer the question with code. Prefer pandas/polars for tabular work, matplotlib/plotly for charts. Show intermediate results so your reasoning is checkable.
4. For product-analytics questions, describe event funnels, retention cohorts, and property breakdowns clearly.
5. Summarize findings in plain language, including caveats (sample size, missing data, correlation-vs-causation).

Default to simple, readable analysis over clever one-liners. A clear bar chart usually beats a dense heatmap."""

XAI_API_KEY = os.environ.get("XAI_API_KEY")
if not XAI_API_KEY:
    raise ValueError("Set the XAI_API_KEY environment variable before running.")

client = OpenAI(
    api_key=XAI_API_KEY,
    base_url="https://api.x.ai/v1",
)


def ask(question: str) -> str:
    response = client.chat.completions.create(
        model="grok-3",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question},
        ],
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    print("Data Analyst Agent (powered by xAI Grok)")
    print("Type your question, or 'quit' to exit.\n")
    while True:
        question = input("You: ").strip()
        if question.lower() in ("quit", "exit", "q"):
            break
        if not question:
            continue
        print("\nAgent:", ask(question), "\n")
