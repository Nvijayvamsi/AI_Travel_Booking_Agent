import os
from typing import Annotated, TypedDict
import operator

from dotenv import load_dotenv
from langchain_core.messages import AnyMessage, HumanMessage, AIMessage, SystemMessage
from langgraph.graph import StateGraph, START, END

load_dotenv()

try:
    import psycopg
    from langgraph.checkpoint.postgres import PostgresSaver
except Exception:
    psycopg = None
    PostgresSaver = None

try:
    from langchain_groq import ChatGroq
except Exception:  # pragma: no cover
    ChatGroq = None

from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights

DEMO_MODE = os.getenv("DEMO_MODE", "false").strip().lower() in {"1", "true", "yes", "on"}
DATABASE_URL = os.getenv("DATABASE_URL")


def create_llm():
    if DEMO_MODE or ChatGroq is None:
        return None
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return None
    return ChatGroq(model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"), api_key=api_key)


llm = create_llm()


class TravelState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    user_query: str
    flight_results: str
    hotel_results: str
    itinerary: str
    final_response: str
    llm_calls: int


def flight_agent(state: TravelState):
    query = state["user_query"]
    flight_data = search_flights(query)
    return {
        "flight_results": flight_data,
        "messages": [AIMessage(content="Flight results fetched")],
        "llm_calls": state.get("llm_calls", 0) + 1,
    }


def hotel_agent(state: TravelState):
    query = f"Best hotels for {state['user_query']}"
    hotel_results = tavily_search(query)
    return {
        "hotel_results": hotel_results,
        "messages": [AIMessage(content="Hotel information fetched")],
        "llm_calls": state.get("llm_calls", 0) + 1,
    }


def _llm_response(prompt: str):
    if llm is None:
        return AIMessage(content="Demo travel plan: a polished itinerary overview with suggested flights and hotels based on your preferences.")
    response = llm.invoke([
        SystemMessage(content="You are an expert travel planner."),
        HumanMessage(content=prompt),
    ])
    return response


def itinerary_agent(state: TravelState):
    prompt = f"""
    Create a concise travel itinerary for the user.
    User Query:
    {state['user_query']}

    Flight Results:
    {state['flight_results']}

    Hotel Results:
    {state['hotel_results']}
    """
    response = _llm_response(prompt)
    return {
        "itinerary": response.content,
        "messages": [response],
        "llm_calls": state.get("llm_calls", 0) + 1,
    }


def final_agent(state: TravelState):
    final_prompt = f"""
    Create a polished final travel response.

    Flights:
    {state['flight_results']}

    Hotels:
    {state['hotel_results']}

    Itinerary:
    {state['itinerary']}
    """
    response = _llm_response(final_prompt)
    return {
        "final_response": response.content,
        "messages": [response],
        "llm_calls": state.get("llm_calls", 0) + 1,
    }


graph = StateGraph(TravelState)

graph.add_node("flight_agent", flight_agent)
graph.add_node("hotel_agent", hotel_agent)
graph.add_node("itinerary_agent", itinerary_agent)
graph.add_node("final_agent", final_agent)

graph.add_edge(START, "flight_agent")
graph.add_edge("flight_agent", "hotel_agent")
graph.add_edge("hotel_agent", "itinerary_agent")
graph.add_edge("itinerary_agent", "final_agent")
graph.add_edge("final_agent", END)

checkpointer = None
if DATABASE_URL and psycopg and PostgresSaver:
    try:
        _conn = psycopg.connect(DATABASE_URL, autocommit=True)
        checkpointer = PostgresSaver(_conn)
        checkpointer.setup()
    except Exception:
        checkpointer = None

app = graph.compile(checkpointer=checkpointer) if checkpointer is not None else graph.compile()


def build_travel_plan(user_query: str, thread_id: str = "demo_user"):
    config = {"configurable": {"thread_id": thread_id}}
    result = app.invoke(
        {
            "messages": [HumanMessage(content=user_query)],
            "user_query": user_query,
            "flight_results": "",
            "hotel_results": "",
            "itinerary": "",
            "final_response": "",
            "llm_calls": 0,
        },
        config=config,
    )
    return result


if __name__ == "__main__":
    user_input = input("Enter travel request: ").strip() or "Plan a 5-day trip to Tokyo"
    result = build_travel_plan(user_input)
    print("\nFINAL RESPONSE:\n")
    print(result.get("final_response", ""))