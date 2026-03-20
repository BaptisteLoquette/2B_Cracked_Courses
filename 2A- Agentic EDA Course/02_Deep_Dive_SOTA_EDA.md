# 2. Deep Dive: SOTA AI EDA Solutions 🔬

**TL;DR:** Modern agentic systems leverage **domain-specialized models** to outperform general-purpose LLMs. We analyze ChatEDA, RTLCoder, and EDAid.

---

## 1. ChatEDA and the AutoMage Controller 🤖

**Architecture:** A three-stage pipeline consisting of task decomposition, script generation (Python/Tcl), and task execution.

**Controller (AutoMage):** Uses an expert model fine-tuned on Llama 2 using a *"self-instruction"* paradigm where GPT-4 generated a 10K-tuple dataset of `<requirement, decomposition, script>`.

- **Key Strength:** Maps natural language directly to physical design tool commands (e.g., OpenROAD).

---

## 2. RTLCoder: Lightweight Verifiable Synthesis 💻

**Implementation:** A 7B parameter model (RTLCoder-Deepseek or Mistral) that can run locally on 4GB of memory.
- **Why it matters:** It addresses IP privacy concerns. Corporations cannot send proprietary HDL to OpenAI.

**Mechanism:** Employs a **Quality-Based Training Scheme** that uses feedback from Icarus Verilog syntax checks and functional simulations to reward "synthesizable" code over merely "plausible" code.

---

## 3. EDAid: Divergent Thought Collaboration 🧠

**System:** Multiple agents powered by **ChipLlama** converge on a common goal.

**Divergent Thinking:** Uses different few-shot **Chain-of-Thought (CoT)** prompts for each agent to prevent the system from getting stuck in an erroneous planning pathway.

```mermaid
graph LR
    A[Task: "Optimize PPA"] --> B(ChipLlama Agent 1: Power Focus)
    A --> C(ChipLlama Agent 2: Area Focus)
    A --> D(ChipLlama Agent 3: Speed Focus)
    B --> E{Arbiter Agent}
    C --> E
    D --> E
    E -->|Selects Best Path| F[Final Solution]
```

**Next:** We transition from the digital domain to the continuous nightmare of analog design in [Section 3: Specialized Agentic EDA for Analog Design](./03_Specialized_Analog_EDA.md).