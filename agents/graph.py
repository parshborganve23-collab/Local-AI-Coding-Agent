from typing import TypedDict

from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama


class CodingState(TypedDict):
    task: str
    plan: str
    code: str
    review: str
    tests: str


def build_graph():
    llm = ChatOllama(
        model="qwen2.5-coder:7b",
        base_url="http://localhost:11434",
        temperature=0.2,
    )

    def planner(state: CodingState):
        response = llm.invoke(
            "You are a software architect. Break this task into "
            "clear implementation steps:\n" + state["task"]
        )
        return {"plan": response.content}

    def developer(state: CodingState):
        response = llm.invoke(
            "You are a senior software developer. Implement this task.\n"
            f"Task: {state['task']}\n"
            f"Plan: {state['plan']}\n"
            "Provide complete, clearly labelled code."
        )
        return {"code": response.content}

    def reviewer(state: CodingState):
        response = llm.invoke(
            "You are a code reviewer. Identify bugs, security risks, "
            "missing requirements and improvements.\n"
            + state["code"]
        )
        return {"review": response.content}

    def tester(state: CodingState):
        response = llm.invoke(
            "You are a software testing engineer. Create test cases "
            "and suggested pytest tests for this implementation.\n"
            + state["code"]
        )
        return {"tests": response.content}

    workflow = StateGraph(CodingState)

    workflow.add_node("planner", planner)
    workflow.add_node("developer", developer)
    workflow.add_node("reviewer", reviewer)
    workflow.add_node("tester", tester)

    workflow.add_edge(START, "planner")
    workflow.add_edge("planner", "developer")
    workflow.add_edge("developer", "reviewer")
    workflow.add_edge("reviewer", "tester")
    workflow.add_edge("tester", END)

    return workflow.compile()