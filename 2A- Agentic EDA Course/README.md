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

## 📚 References & Source Material

- Multi-Agent Systems with LangGraph - Coursera, https://www.coursera.org/learn/multi-agent-systems-with-langgraph
- [2502.10857] Divergent Thoughts toward One Goal: LLM-based Multi-Agent Collaboration System for Electronic Design Automation - arXiv.org, https://arxiv.org/abs/2502.10857
- Multi-agent - Docs by LangChain, https://docs.langchain.com/oss/python/langchain/multi-agent
- Rtlcoder: Fully Open-Source and Efficient Llm-Assisted RTL Code Generation Technique | PDF - Scribd, https://www.scribd.com/document/899354028/2312-08617v4
- ChatEDA: A Large Language Model Powered Autonomous Agent for EDA - CUHK CSE, https://www.cse.cuhk.edu.hk/~byu/papers/J115-TCAD2024-ChatEDA.pdf
- Building multi-agent systems with LangGraph - CWAN, https://cwan.com/resources/blog/building-multi-agent-systems-with-langgraph/
- hkust-zhiyao/RTL-Coder: A new LLM solution for RTL code generation, achieving state-of-the-art performance in non-commercial solutions and outperforming GPT-3.5. - GitHub, https://github.com/hkust-zhiyao/RTL-Coder
- The Blueprint for Production-Grade Agentic Architecture, https://www.artiquare.com/production-grade-agentic-architecture-blueprint/
- Top 10 Agentic AI Frameworks In 2026 For Developers - Aitude, https://www.aitude.com/top-agentic-ai-frameworks-2026/
- Top Agentic LLM Models & Frameworks for 2026 | Adaline, https://www.adaline.ai/blog/top-agentic-llm-models-frameworks-for-2026
- THE DEFINITIVE BLUEPRINT FOR ENTERPRISE AGENTIC AI ARCHITECTURE | by Mohammed Brückner | CodeToDeploy | Feb, 2026 | Medium, https://medium.com/codetodeploy/the-definitive-blueprint-for-enterprise-agentic-ai-architecture-a1b7b0c384b3
- Cadence and NVIDIA Unveil Accelerated Engineering Solutions for Agentic AI Chip and System Design - HPCwire, https://www.hpcwire.com/off-the-wire/cadence-and-nvidia-unveil-accelerated-engineering-solutions-for-agentic-ai-chip-and-system-design/
- FareedKhan-dev/production-grade-agentic-system - GitHub, https://github.com/FareedKhan-dev/production-grade-agentic-system
- ChatEDA: A Large Language Model Powered Autonomous Agent for EDA - ResearchGate, https://www.researchgate.net/publication/379427483_ChatEDA_A_Large_Language_Model_Powered_Autonomous_Agent_for_EDA
- ChatEDA: A Large Language Model Powered Autonomous Agent for EDA - CUHK CSE, https://www.cse.cuhk.edu.hk/~byu/papers/C177-MLCAD2023-ChatEDA.pdf
- The Dawn of Agentic EDA: A Survey of Autonomous Digital Chip Design - arXiv, https://arxiv.org/html/2512.23189v1
- ACE-RTL: When Agentic Context Evolution Meets RTL-Specialized LLMs - arXiv, https://arxiv.org/html/2602.10218v1
- [AAAI 2025 Oral] AnalogCoder: Analog Circuit Design via Training-Free Code Generation - GitHub, https://github.com/laiyao1/AnalogCoder
- AnalogCoder-Pro: Unifying Analog Circuit Generation and Optimization via Multi-modal LLMs - arXiv.org, https://arxiv.org/html/2508.02518v1
- LayoutCopilot: An LLM-powered Multi-agent Collaborative Framework for Interactive Analog Layout Design - ResearchGate, https://www.researchgate.net/publication/381770577_LayoutCopilot_An_LLM-powered_Multi-agent_Collaborative_Framework_for_Interactive_Analog_Layout_Design
- A brief history and future perspectives on sizing and layout synthesis of analog/RF integrated circuits - ResearchGate, https://www.researchgate.net/publication/395078134_A_brief_history_and_future_perspectives_on_sizing_and_layout_synthesis_of_analogRF_integrated_circuits