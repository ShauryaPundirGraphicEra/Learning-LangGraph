
# 🕸️ Mastering LangGraph: From State Graphs to Time-Traveling Agents

Welcome to my **LangGraph exploration repository**. This project documents a structured journey into building **stateful, multi-actor Large Language Model (LLM) applications** using LangGraph and LangChain.

---

## 📌 NOTE

This is not a random collection of tutorials.

This repository demonstrates my ability to:

- Design and implement **agentic workflows**
- Manage complex **state transitions**
- Debug and trace LLM systems
- Transition from experimentation → **production-ready applications**

You’ll see a clear progression:
> Basic Graphs → Agent Loops → Persistence → Human-in-the-Loop → Time Travel → Full Stack Deployment

---

## 🎯 Key Competencies Demonstrated

### 🧠 Agentic Framework Architecture
- Designed cyclic & acyclic workflows using `StateGraph`, `START`, and `END`
- Built multi-step reasoning pipelines

### 🔄 State Management
- Used `TypedDict` for structured and safe state mutation
- Managed state across multiple LLM interactions

### ⚙️ Advanced LangGraph Features

#### ✔️ Persistence & Checkpointing
- Implemented memory using:
  - In-memory checkpointers
  - SQLite-backed persistence

#### ✔️ Human-in-the-Loop
- Introduced `interrupts` for controlled execution
- Enabled approval-based workflows

#### ✔️ Time Travel (Advanced)
- Queried graph history using:
  - `get_state_history()`
- Extracted `checkpoint_id`
- Restored historical states
- Replayed workflows from past states

#### ✔️ Observability
- Integrated **LangSmith** for:
  - Execution tracing
  - Debugging
  - Graph visualization

### 🌐 Full-Stack LLM Integration
- Converted notebook experiments → full-stack chatbot
- Built modular architecture (`frontend + backend + DB`)

### 🤖 Model Integration
- Used:
  - HuggingFace Endpoints
  - ChatHuggingFace
  - Cerebras API

---

## 📂 Repository Architecture & Learning Path

### 🔹 Phase 1: Core Graph Mechanics

- **workflow1.ipynb**  
  → Basic nodes, edges, and state flow  

- **workflow2-bmi.ipynb**  
  → Deterministic logic system (BMI calculator)  
  → Demonstrates non-LLM workflows inside graphs  

- **workflow3-simple-llm.ipynb**  
  → First LLM integration using LangChain  

---

### 🔹 Phase 2: Agentic Behavior & Memory

- **workflow4-Iterative.ipynb**  
  → Introduced loops (agent-like behavior)  
  → Conditional edges for decision-making  

- **workflow5-chatbot_with_persistence.ipynb**  
  → Short-term memory with `thread_id`  
  → Multi-turn conversations  

---

### 🔹 Phase 3: Advanced LangGraph Engineering

- **workflow6-persistance-depth.ipynb**  
- **workflow7-test.ipynb**

Key concepts:

#### ⏸ Interrupts
- Paused execution for external input
- Simulated real-world approval flows

#### 🕰 Time Travel API
- Traversed graph history
- Restored checkpoints
- Re-executed workflows from past states

---

### 🔹 Phase 4: Productionizing the Agent

#### 📁 Chatbot/
Full-stack implementation:

- **backend.py**
  - LangGraph workflow
  - State + LLM orchestration

- **frontend.py**
  - User interaction layer

- **chat_history.db**
  - Persistent SQLite memory

---

#### 📁 JawabAI/
- Domain-specific QA agent
- Custom prompt engineering
- Structured routing logic
- link:- https://github.com/ShauryaPundirGraphicEra/JawabAI

---

## 🛠️ Technology Stack

### 🔧 Frameworks
- LangGraph
- LangChain
- LangSmith (observability)

### 💻 Language
- Python 3.10+

### 🤖 LLM Providers
- HuggingFace Inference API
- Cerebras

### 🗄️ State & Storage
- Python TypedDict
- SQLite

### 🧪 Environment
- Jupyter Notebooks (prototyping)
- Python Scripts (production)

---

## 🚀 Getting Started

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/Learning-LangGraph.git
cd Learning-LangGraph
````

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Setup Environment Variables

Create a `.env` file:

```env
HUGGINGFACEHUB_API_TOKEN=your_token
CEREBRAS_API_KEY=your_key
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=your_key
LANGSMITH_PROJECT=LangGraph-Project
```

⚠️ **Important:** Never commit `.env` files or API keys.

---

### 4. Run Chatbot

```bash
cd Chatbot
streamlit run frontend.py
```

---

# 🔍 Important Concepts That I Covered 


1. **Chatbot/backend.py**
   → Core LangGraph architecture

2. **workflow6-persistance-depth.ipynb**
   → Advanced features (Time Travel + Interrupts)

3. **Chatbot + SQLite integration**
   → Production readiness

---


# This repository demonstrates:

* Strong understanding of **agentic systems**
* Ability to move from **concept → implementation → deployment**
* Hands-on experience with **real-world LLM engineering challenges**

---

