🕸️ Mastering LangGraph: From State Graphs to Time-Traveling Agents

Welcome to my LangGraph exploration repository! This project documents my comprehensive journey into building stateful, multi-actor Large Language Model (LLM) applications using LangGraph and LangChain.

To Recruiters and Engineering Managers: This repository is not just a collection of tutorials. It is a structured progression demonstrating my ability to build, debug, and productionize complex agentic workflows. By navigating through these files, you will see my progression from basic graph mechanics to advanced concepts like state persistence, human-in-the-loop (interrupts), and graph "time travel."

🎯 Key Competencies Demonstrated

Agentic Framework Architecture: Designing cyclic and acyclic graphs using StateGraph, START, and END nodes.

State Management: Utilizing Python TypedDict to robustly manage and mutate application state across multiple LLM interactions.

Advanced LangGraph Features: * Persistence & Checkpointing: Storing thread histories using in-memory and database-backed checkpointers.

Human-in-the-Loop: Suspending workflows using interrupts to wait for human permission before executing sensitive actions.

Time Travel: Querying get_state_history(), identifying specific checkpoint_ids, checking out historical states, and re-invoking or branching workflows from the past.

Full-Stack LLM Integration: Transitioning from Jupyter Notebook experiments to a structured full-stack Chatbot application (frontend.py + backend.py + SQLite).

Model Integration: Utilizing HuggingFaceEndpoint and ChatHuggingFace via LangChain for efficient open-source model inference.

📂 Repository Architecture & Learning Path

My learning approach was highly iterative. The repository is divided into conceptual workflows (Jupyter Notebooks) and applied projects (Folders).

Phase 1: Core Graph Mechanics & State

workflow1.ipynb - The Basics: Introduction to creating nodes, defining edges, and basic state passing.

workflow2-bmi.ipynb - Logic & Tooling: Building a deterministic BMI calculator workflow. Demonstrates the ability to route logic and pass typed data between non-LLM Python functions within a graph.

workflow3-simple-llm.ipynb - Injecting Intelligence: Integrating langchain_huggingface. Created a graph where an LLM node receives state, processes a prompt, and mutates the state with its response.

Phase 2: Agentic Loops & Memory

workflow4-Iterative.ipynb - Cyclic Graphs: Breaking away from simple linear chains. Implemented iterative loops (agentic behavior) where the graph can dynamically decide whether to loop back to a node or proceed to END based on conditional edges.

workflow5-chatbot_with_persistance.ipynb - Short-Term Memory: Introduced checkpointers to give the agent "memory." Handled conversational context across multiple turns using thread_ids.

Phase 3: Advanced LangGraph Engineering (The "Hard" Stuff)

workflow6-persistance-depth.ipynb & workflow7-test.ipynb: Deep dive into the internal mechanics of LangGraph's state machine.

Interrupts: Programmed the graph to pause execution and wait for external input/permission, mimicking real-world authorization flows.

Time Travel API: Implemented logic to traverse the graph's history:

Used workflow.get_state_history(config) to fetch the state trajectory.

Extracted specific checkpoint_ids.

Explored checking out past states using workflow.get_state({"configurable": {"thread_id": 1, "checkpoint_id": "..."}}).

Replayed the workflow from that exact historical node using workflow.invoke().

Phase 4: Productionizing the Agent

📁 Chatbot/ - Full-Stack Implementation: I translated the notebook concepts into a modular, deployable architecture.

backend.py: Contains the LangGraph definition, state configuration, and LLM integrations.

frontend.py: The user interface (designed for interaction and displaying the agent's thought process).

chat_history.db: A persistent SQLite database handling long-term thread memory, proving I can bridge LangGraph's in-memory concepts with persistent storage.

📁 JawabAI/: A specialized, localized QA agent implementation showcasing custom prompt engineering and specific domain routing.

🛠️ Technology Stack

Frameworks: LangGraph, LangChain

Language: Python 3.10+

LLM Providers: HuggingFace Inference Endpoints (via .env secrets)

State / Data: Python TypedDict, SQLite (chat_history.db)

Environment: Jupyter Notebooks (for prototyping), Standard Python scripts (for the app)

🚀 Getting Started

To run the code in this repository locally:

Clone the repository:

git clone [https://github.com/yourusername/Learning-LangGraph.git](https://github.com/yourusername/Learning-LangGraph.git)
cd Learning-LangGraph


Install Dependencies:

pip install -r requirement.txt


Set up Environment Variables:
Create a .env file in the root directory and add your HuggingFace API key:

HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here


Run the Chatbot App:

cd Chatbot
# Depending on your frontend framework (e.g., Streamlit or Gradio)
streamlit run frontend.py  # or python frontend.py


I highly recommend looking at the Chatbot/backend.py file to see my graph architecture, and workflow6-persistance-depth.ipynb to see my handling of graph Time Travel and Interrupts.
