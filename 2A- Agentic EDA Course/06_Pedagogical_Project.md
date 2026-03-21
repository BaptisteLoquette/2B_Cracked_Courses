# 6. Pedagogical Project: Self-Evolving Analog Block Designer 🛠️

**TL;DR:** This chronological project allows you to build a complete agentic analog EDA system module-by-module. Open the accompanying Jupyter Notebooks to write the LangGraph code.

---

## 🏗️ Stage A: The Identification Agent

**Objective:** Build a module that parses natural language specs into a structured JSON component list.
- **Tools:** Named Entity Recognition (NER) on hardware categories using Pydantic.
- **Outcome:** A "Component Inventory" JSON specifying the required analog blocks (e.g., Op-Amps, Current Mirrors).

---

## 🔄 Stage B: Feedback-Enhanced Netlist Generator

**Objective:** Build a cyclic loop that generates a SPICE netlist using AnalogCoder principles.
- **Tools:** Python-based netlist generation (`PySpice` or raw Python f-strings), domain-specific prompts, and `ngspice` simulation tools.
- **Outcome:** A synthesizable netlist grounded in open-source PDK rules (like SKY130).

👉 **[Run the Stage A & B Notebook](./notebooks/01_Stage_AB_Netlist_Gen.ipynb)**

---

## 👁️ Stage C: Multimodal Waveform Debugger

**Objective:** Implement an agent that "looks" at output waveforms instead of just parsing raw numbers.
- **Tools:** Multimodal LLMs (like GPT-4o, Gemini 1.5 Pro, or Claude 3.5 Sonnet Vision).
- **Action:** The simulation agent generates a `.png` of the gain/phase plot. The Vision agent identifies "instability" or "ringing" in the transient response and suggests new bias currents or compensation capacitors.

---

## 📏 Stage D: Autonomous Layout Synthesis

**Objective:** Final physical design automation.
- **Tools:** `ALIGN`, `OpenROAD`, or `Magic VLSI`.
- **Action:** The agent writes the layout TCL commands and then uses a "proofreading strategy" to parse DRC (Design Rule Check) and LVS (Layout vs Schematic) errors, iteratively adjusting placement to achieve sign-off.

👉 **[Run the Stage C & D Notebook](./notebooks/02_Stage_CD_Waveform_Layout.ipynb)**