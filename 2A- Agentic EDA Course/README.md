# Design and Implementation of Production-Grade Multi-Agent Systems for Analog and Digital Electronic Design Automation: A Technical Master Guide

**TL;DR:** The EDA industry is shifting from traditional AI-assisted automation (AI4EDA) to **Agentic EDA**. As SoCs scale to hundreds of billions of transistors, manual scripts fail. This course is your technical master guide to building 2026-standard Multi-Agent Systems (MAS) specialized for analog circuit design.

---

## 🎯 The Paradigm Shift

The "Productivity Gap" is widening. Verification now consumes up to 70% of the design cycle.

*Note for AI Engineers: In 2026, your role is no longer coding, but **Agent Orchestration**. Mastery involves designing the "separation of concerns" where one agent generates and a separate "Critic Agent" judges the output to ensure trust and validation.*

### ⚖️ Annex: Foundations of AI for EDA vs. Agentic EDA

| Feature | AI-Assisted (AI4EDA) | Agentic EDA (2026 Standard) |
| :--- | :--- | :--- |
| **Orchestration** | Manual (Human Engineer) | Autonomous (MAS Supervisor) |
| **Logic Flow** | Static Tcl/Python Scripts | Dynamic Graphs (DAGs/Cycles) |
| **Memory** | None (Per-execution) | Stratified (Evolution/Evolutionary) |
| **Verification** | Final Check | Continuous Inner-Loop Feedback |
| **Outcome** | Assistant results | Self-correcting design closure |

---

## 🗺️ Master Guide Syllabus

1. **[Core Agentic Architectures and Mechanisms](./01_Core_Agentic_Architectures.md)**
   - Supervisor-Worker, Consensus-Based Reasoning, Handoff Patterns, and Stateful Graph Workflows.
2. **[Deep Dive: SOTA AI EDA Solutions](./02_Deep_Dive_SOTA_EDA.md)**
   - Exploring ChatEDA (AutoMage), RTLCoder, and EDAid (Divergent Thought Collaboration).
3. **[Specialized Agentic EDA for Analog Design](./03_Specialized_Analog_EDA.md)**
   - AnalogCoder/Pro, AnalogSAGE (Stratified Memory), GENIE-ASI, and Schemato.
4. **[The Physical Frontier: Challenges & Bottlenecks](./04_The_Physical_Frontier.md)**
   - The Feedback Loop Crisis, Layout Interdependency (WPE/STI), and the Data Wall.
5. **[Mastery Modules for AI Engineers](./05_Mastery_Modules.md)**
   - Model Context Protocol (MCP), LangGraph persistent checkpointing, and the 12 Pillars of Production MAS.
6. **[Pedagogical Project: Self-Evolving Analog Block Designer](./06_Pedagogical_Project.md)**
   - Build a complete agentic analog EDA system module-by-module (Stages A-D).

### 🛠️ Hands-On Jupyter Notebooks
- **[Stage A & B: Identification & Netlist Generator](./notebooks/01_Stage_AB_Netlist_Gen.ipynb)**
- **[Stage C & D: Multimodal Waveform Debugging & Layout](./notebooks/02_Stage_CD_Waveform_Layout.ipynb)**

---

**References:**
- *Multi-Agent Systems with LangGraph - Coursera (2026)*
- *[2502.10857] Divergent Thoughts toward One Goal: LLM-based Multi-Agent Collaboration System for Electronic Design Automation (2025)*
- *RTL-Coder: Fully Open-Source and Efficient Llm-Assisted RTL Code Generation Technique (2026)*
- *[AAAI 2025 Oral] AnalogCoder: Analog Circuit Design via Training-Free Code Generation*
- *AnalogCoder-Pro: Unifying Analog Circuit Generation and Optimization via Multi-modal LLMs (2025)*