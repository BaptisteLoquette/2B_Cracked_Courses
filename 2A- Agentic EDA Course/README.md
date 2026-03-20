# 🚀 The Ultimate Guide: State-of-the-Art Agentic EDA for Analog

**TL;DR:** Welcome to your ADHD-friendly, highly visual, and hands-on journey into the bleeding edge of Electronic Design Automation (EDA). We're taking Large Language Models (LLMs), giving them tools (Agents), and teaching them how to design computer chips—with a massive focus on the dark art of **Analog Design**.

---

## 🎯 What is this course?

Most tutorials online show you how to use AI to write a Python script. But what happens when you need an AI to design an Op-Amp, run a SPICE simulation, read the waveforms, realize the gain is too low, and tweak the transistor sizing?

That's **Agentic Analog EDA**.

This course breaks down the theory, the state-of-the-art (SOTA) research, and gives you runnable Python code (Jupyter Notebooks) to build these systems yourself using open-source tools.

---

## 🧠 How to use this course (ADHD Edition)

- **Skip the fluff:** Look for the **TL;DR** at the top of every page.
- **Visuals first:** We use a lot of diagrams and interactive HTML/SVG files. Look at them before reading the text.
- **Hands-on immediately:** Don't just read. Open the Jupyter Notebooks and run the code. Break it. Fix it.
- **Bite-sized:** Each module is focused on one specific concept.

---

## 🗺️ Syllabus

### 📖 Theory & State of the Art
1. **[Module 1: The Digital Baseline - ChatEDA, RTLCoder & Beyond](./01_Intro_and_Digital_EDA.md)**
   - How LLMs are conquering Digital RTL.
   - What we can learn from digital success.
2. **[Module 2: The Analog EDA Nightmare](./02_Analog_EDA_Challenges.md)**
   - Why Analog is 100x harder than Digital for AI.
   - Continuous variables, parasitics, and the "black magic" of layout.
3. **[Module 3: SOTA Multi-Agent Architecture for Analog](./03_Multi_Agent_Architecture.md)**
   - Designing a production-grade system using **LangGraph**.
   - The Roles: Planner, Coder, Simulator, Critic.
   - *Includes interactive HTML visualization!*
4. **[Module 6: Existing Architectures Deep Dive](./06_Existing_Architectures_DeepDive.md)**
   - An extensive analysis of SOTA Agentic EDA (AutoChip, ChatEDA, ChipNeMo).
   - How they structure memory, tools, and feedback loops.
5. **[Module 7: The Realistic Assessment](./07_Realistic_Assessment.md)**
   - No hype. What actually works today?
   - What are the hard bottlenecks? What is unsolvable?

### 🛠️ Hands-On Projects (Jupyter Notebooks)
*Note: These require a working Python environment and open-source EDA tools installed (like ngspice).*

6. **[Module 4: Agentic SPICE Simulation](./notebooks/04_HandsOn_Agentic_Ngspice.ipynb)**
   - Build a LangGraph agent that writes a netlist, runs `ngspice`, and optimizes a circuit to hit a target spec.
7. **[Module 5: Agentic Layout & DRC](./notebooks/05_HandsOn_Agentic_Layout.ipynb)**
   - How an agent generates a layout script (e.g., Magic VLSI) and fixes Design Rule Check (DRC) errors autonomously.

---

## 🛠️ Prerequisites

To get the most out of the hands-on sections, you should have:
- Basic understanding of Python (we use LangGraph/LangChain).
- Basic understanding of Analog circuit concepts (transistors, SPICE netlists).
- An environment with `ngspice` installed.

Let's build the future of chip design. 🚀