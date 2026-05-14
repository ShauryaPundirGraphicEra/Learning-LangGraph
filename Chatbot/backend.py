from turtle import st

from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Annotated
from langchain_core.messages import HumanMessage,SystemMessage,BaseMessage
from dotenv import load_dotenv
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.sqlite import SqliteSaver
import os
from langgraph.graph.message import add_messages
import sqlite3

load_dotenv()

from langchain_cerebras import ChatCerebras

llm = ChatCerebras(
    model="qwen-3-235b-a22b-instruct-2507",
    api_key=os.getenv("CEREBRAS_API_KEY"),
    temperature=0.7,
    max_tokens=600 
)

chat=llm


class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages] # means this BaseMessage contains all type of messages like HumanMessage,SystemMessage,AIMessage and we can use add_messages(as a reducer by langraph instaead of langchain operator) to add messages to the list


def chat_node(state:ChatState)->ChatState:
    message=state['messages']
    
    response=chat.invoke(message)
    
    return {'messages':[response]}

conn=sqlite3.connect(database='chat_history.db',check_same_thread=False)

# checkpointer=InMemorySaver()
checkpointer=SqliteSaver(conn)

graph=StateGraph(ChatState)

graph.add_node('chat_node',chat_node)

graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)

chatbot=graph.compile(checkpointer=checkpointer)


# CONFIG = {'configurable': {'thread_id': 1}}
 
# result=chatbot.invoke({"messages": [HumanMessage(content="Hi there")]},config=CONFIG )

# print(result)

def get_all_threads():
    all_threads = set()
    for c in checkpointer.list(None):
        tid = c.config['configurable'].get('thread_id')

        if isinstance(tid, str):
            all_threads.add(tid)
    return list(all_threads)