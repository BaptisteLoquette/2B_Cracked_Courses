# Module 1: Introduction to Agentic EDA & The Digital Landscape 🖥️

**TL;DR:** Before we tackle Analog design (which is super hard), we need to see what AI has already accomplished in Digital design (which is slightly easier). Models like **ChatEDA** and **RTLCoder** have paved the way by turning text (English) into Verilog code and automating synthesis tools.

---

## 🤯 The Shift: From Copilot to Agent

Most people use AI as a *Copilot*—you ask it a question, it writes code, you copy-paste it.

An **Agent** is different. An agent has:
1. **A Goal:** "Design a 4-bit adder."
2. **Tools:** It can run compilers, simulators, and linters.
3. **Memory:** It remembers what worked and what failed.
4. **Autonomy:** It writes the code, compiles it, sees an error, and *fixes it itself* until it works.

---

## 🛠️ The Digital SOTA (State of the Art)

Digital Electronic Design Automation (EDA) relies on distinct, text-based languages like Verilog or VHDL. Since LLMs are amazing at text, they are amazing at Digital EDA. Let's look at the two big open-source players.

### 1. ChatEDA 💬
**Goal:** Automate the entire digital flow (RTL to GDSII) using Natural Language.

**How it works:**
Instead of learning complex Tool Command Language (TCL) scripts for tools like OpenROAD or Yosys, you just tell ChatEDA what you want in English. ChatEDA uses a fine-tuned LLM (AutoMage) to convert your intent into the correct TCL commands.

```mermaid
graph TD
    A[User Prompt: "Run synthesis and floorplan for my RISC-V core"] --> B(ChatEDA Agent)
    B --> C{Task Planner}
    C -->|Sub-task 1| D[Generate Yosys TCL script]
    C -->|Sub-task 2| E[Generate OpenROAD TCL script]
    D --> F[Execute Tool]
    E --> F
    F --> G[Extract Logs/Metrics]
    G --> H{Did it succeed?}
    H -- Yes --> I[Return Results to User]
    H -- No --> J[Analyze Errors & Retry Planner]
    J --> C
```

**Key Takeaways from ChatEDA:**
- **Tool-Use is King:** LLMs don't need to know how to place standard cells; they just need to know how to talk to a tool (like OpenROAD) that does.
- **Feedback Loops:** If Yosys throws a syntax error, the agent reads the log and patches the script.

---

### 2. RTLCoder 💻
**Goal:** Generate flawless, synthesizeable Verilog code.

**How it works:**
Writing perfect Verilog on the first try is rare. RTLCoder uses a pipeline where the code is compiled, and the *compiler errors are fed back into the LLM*. It learns from its mistakes.

```mermaid
sequenceDiagram
    participant User
    participant RTLCoder
    participant Simulator (e.g., Verilator)

    User->>RTLCoder: "Write a UART Transmitter in Verilog"
    RTLCoder->>Simulator: Submit v1.0 code
    Simulator-->>RTLCoder: Error: Missing semicolon on line 42
    RTLCoder->>Simulator: Submit v1.1 code (fixed)
    Simulator-->>RTLCoder: Success! Waveform generated.
    RTLCoder->>User: "Here is your working Verilog."
```

**Key Takeaways from RTLCoder:**
- **Compilation as Ground Truth:** Text is subjective. Code compilation is absolute. If it synthesizes, it's good.
- **Iterative Refinement:** You don't need a massive GPT-4 size model if you have a fast feedback loop. A smaller open-source model running thousands of iterations often beats a giant model on one shot.
- **Formal Equivalence:** In advanced digital agentic flows, simulation is not enough. Agents write SystemVerilog Assertions (SVA) and run formal verification tools (like SymbiYosys) to mathematically prove the RTL state machine cannot enter an illegal state. The solver's counter-example trace is then fed back to the LLM to patch the logic error.

---

## ⚖️ Why can't we just use this for Analog?

If it works so well for digital, why is Analog EDA lagging behind?

**Digital is Discrete.** A signal is a `1` or a `0`. Code is text. The flow is logical and deterministic.

**Analog is Continuous.** A signal is `1.34V`. The performance depends on layout, parasitics, temperature, matching, and physics. You can't just write "Verilog for an Op-Amp" and compile it. You have to size transistors, run a SPICE simulation, check the phase margin, adjust the sizing by $0.1\mu m$, and run it again.

👉 **Next Step:** We dive into the nightmare of Analog EDA in [Module 2](./02_Analog_EDA_Challenges.md).