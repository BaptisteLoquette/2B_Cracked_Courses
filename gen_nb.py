#!/usr/bin/env python3
"""Generate Chapter 03 notebook from cell files."""
import json, uuid, os, glob

def uid():
    return uuid.uuid4().hex[:8]

cells_dir = "/workspace/_cells"
cell_files = sorted(glob.glob(os.path.join(cells_dir, "*.txt")))

cells = []
for cf in cell_files:
    with open(cf, "r") as f:
        first_line = f.readline().strip()
        content = f.read()

    cell_type = first_line  # "markdown" or "code"
    lines = content.split("\n")
    source = [line + "\n" for line in lines[:-1]] + [lines[-1]]

    cell = {
        "cell_type": cell_type,
        "metadata": {},
        "source": source,
        "id": uid(),
    }
    if cell_type == "code":
        cell["execution_count"] = None
        cell["outputs"] = []

    cells.append(cell)

notebook = {
    "nbformat": 4,
    "nbformat_minor": 5,
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3 (ipykernel)",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {"name": "ipython", "version": 3},
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.11.0"
        }
    },
    "cells": cells,
}

out = "/workspace/2AB- Multi-Agent Analog EDA/Chapter 03 - Stateful Graph Workflows LangGraph/03_langgraph_workflows.ipynb"
with open(out, "w") as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)

print(f"Written {len(cells)} cells to notebook.")
print(f"  Markdown: {sum(1 for c in cells if c['cell_type'] == 'markdown')}")
print(f"  Code: {sum(1 for c in cells if c['cell_type'] == 'code')}")
