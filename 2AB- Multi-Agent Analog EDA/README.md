# Production-Grade Multi-Agent Systems for Analog Electronic Design Automation

## A PhD-Level Interactive Course

> *"In 2026, your role is no longer coding, but Agent Orchestration."*

---

### Course Overview

This course provides a **comprehensive, PhD-level** exploration of designing and implementing **production-grade Multi-Agent Systems (MAS)** for **Analog Electronic Design Automation (EDA)**. As SoC complexity scales to hundreds of billions of transistors, traditional script-based EDA flows have become insufficient. This course bridges the gap between AI-assisted EDA (AI4EDA) and the emerging paradigm of **Agentic EDA**, where autonomous agents collaborate to achieve design closure.

### Prerequisites

- Strong foundation in **circuit theory** and **analog IC design**
- Proficiency in **Python** (advanced level)
- Familiarity with **SPICE simulation** and **PDK concepts**
- Understanding of **LLM architectures** and **prompt engineering**
- Basic knowledge of **graph theory** and **optimization**

### Course Architecture

| Chapter | Title | Focus |
|---------|-------|-------|
| **01** | Foundations: AI4EDA to Agentic EDA | Historical evolution, productivity gap, paradigm shift |
| **02** | Core Agentic Architectures | Supervisor-Worker, Consensus, Handoff, Stateful Graphs |
| **03** | Stateful Graph Workflows with LangGraph | Checkpointing, conditional routing, time-travel debugging |
| **04** | SOTA AI EDA Solutions Deep Dive | ChatEDA, RTLCoder, EDAid, ACE-RTL architectures |
| **05** | Analog Circuit Design Fundamentals | SPICE simulation, SKY130 PDK, circuit primitives |
| **06** | Specialized Agentic EDA for Analog | AnalogCoder, AnalogSAGE, GENIE-ASI, Schemato |
| **07** | The Physical Design Frontier | Layout parasitics, feedback loops, data wall |
| **08** | Model Context Protocol (MCP) Mastery | MCP architecture, Ngspice server implementation |
| **09** | The Twelve Pillars of Production MAS | Enterprise-grade agent infrastructure |
| **10A** | Project: Identification Agent | NLP-to-component parsing |
| **10B** | Project: Netlist Generator | Feedback-enhanced SPICE generation |
| **10C** | Project: Multimodal Waveform Debugger | Vision-based circuit debugging |
| **10D** | Project: Autonomous Layout Synthesis | Physical design automation |
| **11** | Capstone: Full System Integration | End-to-end autonomous analog design |

### Key Technical Differentiators

- **Interactive Jupyter Notebooks** with executable code and real-time visualizations
- **Production-grade code patterns** — not toy examples
- **Physics-grounded reasoning** — agents that understand semiconductor physics
- **Stratified memory architectures** — Evolution, Introspective, and Fusion memory layers
- **Full MCP server implementation** for simulator integration
- **SKY130 PDK-based examples** using open-source toolchains

### Technology Stack

| Layer | Technologies |
|-------|-------------|
| **LLM Backbone** | GPT-5.2, Claude 4.5, Llama 3.1, ChipLlama |
| **Agent Framework** | LangGraph, LangChain, Custom MAS |
| **Simulation** | Ngspice, PySpice, Icarus Verilog |
| **Layout** | ALIGN, OpenROAD |
| **PDK** | SkyWater SKY130 |
| **Visualization** | Matplotlib, Plotly, Schemdraw |
| **Infrastructure** | Docker, FastAPI, MCP |

### Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter lab
```

### References

1. Multi-Agent Systems with LangGraph — Coursera
2. Divergent Thoughts toward One Goal (arXiv:2502.10857)
3. ChatEDA: LLM-Powered Autonomous Agent for EDA — CUHK
4. RTLCoder: Open-Source LLM-Assisted RTL Code Generation
5. The Dawn of Agentic EDA (arXiv:2512.23189)
6. AnalogCoder: Analog Circuit Design via Code Generation — AAAI 2025
7. AnalogCoder-Pro: Multi-modal LLMs for Analog (arXiv:2508.02518)
8. LayoutCopilot: LLM-powered Analog Layout Design
9. The Blueprint for Production-Grade Agentic Architecture — Artiquare
10. The Definitive Blueprint for Enterprise Agentic AI — Medium

---

*Part of the 2B Cracked Courses series — Building market-defining engineering skills.*
