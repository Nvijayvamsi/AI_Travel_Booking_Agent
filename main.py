import os
import sys
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

DEMO_MODE = os.getenv("DEMO_MODE", "true").strip().lower() in {"1", "true", "yes", "on"}
ENABLE_LLM = os.getenv("ENABLE_LLM", "false").strip().lower() in {"1", "true", "yes", "on"}
USE_LLM = ENABLE_LLM and not DEMO_MODE
DATABASE_URL = os.getenv("DATABASE_URL")


def create_llm():
    if DEMO_MODE or not USE_LLM or ChatGroq is None:
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
        return AIMessage(content="Demo travel plan: a short, practical itinerary with simple flight and hotel suggestions.")
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


def run_streamlit_app():
    import streamlit as st

    st.set_page_config(page_title="AI Travel Booking System", page_icon="✈️", layout="wide")
    st.title("AI Travel Booking System")
    st.caption("This deployment uses a low-token demo path so it stays fast and stable.")

    user_query = st.text_area("Trip request", value="Plan a 3-day trip to Tokyo", height=120)
    if st.button("Generate travel plan"):
        with st.spinner("Planning your trip..."):
            result = build_travel_plan(user_query, thread_id="streamlit_user")
        st.subheader("Final plan")
        st.write(result.get("final_response", ""))
        st.info("Set ENABLE_LLM=true and DEMO_MODE=false to use live LLM output.")


if __name__ == "__main__":
    if os.getenv("STREAMLIT_SERVER_PORT") or os.getenv("STREAMLIT_BROWSER_GATHER_USAGE_STATS") is not None:
        run_streamlit_app()
    elif sys.stdin.isatty():
        user_input = input("Enter travel request: ").strip() or "Plan a 5-day trip to Tokyo"
        result = build_travel_plan(user_input)
        print("\nFINAL RESPONSE:\n")
        print(result.get("final_response", ""))
    else:
        result = build_travel_plan("Plan a 5-day trip to Tokyo")
        print(result.get("final_response", ""))