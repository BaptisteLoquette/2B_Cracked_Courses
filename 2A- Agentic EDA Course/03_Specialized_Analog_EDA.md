# 3. Specialized Agentic EDA for Analog Design ⚡

**TL;DR:** Analog design remains the "final frontier" due to its continuous-valued signals and extreme sensitivity to layout parasitics. 2026-standard models are using Python generation and multimodal vision to crack it.

---

## 🔬 SOTA Analog Frameworks

### 1. AnalogCoder & AnalogCoder-Pro
**Concept:** Formulates analog design as **Python code generation**. The LLM doesn't write SPICE strings directly; it writes Python scripts that *wrap* SPICE optimization loops (like PySpice).
**The "Pro" Version:** Utilizes multimodal LLMs (like GPT-4o or Claude 4.5 Vision) to "look" at circuit waveforms. It literally identifies clipping, distortion, or phase margin instability visually, just like a human engineer looking at an oscilloscope.

### 2. AnalogSAGE (Stratified Memory)
**Concept:** A self-evolving framework using a **Stratified Memory Hierarchy**. It splits context into three distinct layers to prevent token overflow:
1. **Evolution Layer:** Stores cross-task insights ("*Cascode mirrors always increase output resistance*").
2. **Introspective Layer:** Within-task failure reflections ("*My last W/L sizing caused the PMOS to drop out of saturation*").
3. **Fusion Layer:** Compressed reasoning traces.

### 3. GENIE-ASI (Sony AI)
**Concept:** A **training-free method** for subcircuit identification.
**Mechanism:** It generates Python code from few-shot examples to detect functional blocks (current mirrors, differential pairs) hidden inside massive, unannotated SPICE netlists.

### 4. Schemato
**Concept:** A fine-tuned Llama 3.1-8B model that bridges the visualization gap.
**Mechanism:** It converts flat, text-based SPICE netlists into human-readable `LTSpice (.asc)` schematic files. This is critical for human-in-the-loop verification, as designers cannot read raw netlists effectively.

---

**Next:** Why is generating the schematic the easy part? We look at physical layout in [Section 4: The Physical Frontier](./04_The_Physical_Frontier.md).