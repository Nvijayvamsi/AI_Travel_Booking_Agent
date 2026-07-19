import os
from dotenv import load_dotenv

load_dotenv()

try:
    from tavily import TavilyClient
except Exception:  # pragma: no cover
    TavilyClient = None

API_KEY = os.getenv("TAVILY_API_KEY")
client = TavilyClient(API_KEY) if TavilyClient and API_KEY else None


def tavily_search(query):
    if client is None:
        return (
            f"Demo hotel suggestions for {query}:\n"
            "- Hotel: Grand View Resort\n"
            "- Rating: 4.8/5\n"
            "- Nearby attractions: City museum, waterfront, nightlife"
        )

    response = client.search(query=query, max_results=5)
    results = []

    for i, r in enumerate(response.get("results", []), 1):
        title = r.get("title", "Unknown")
        url = r.get("url", "")
        snippet = r.get("content", "").strip()
        if len(snippet) > 300:
            snippet = snippet[:300].rsplit(" ", 1)[0] + "..."
        results.append(f"{i}. **{title}**\n   {url}\n   {snippet}")

    return "\n\n".join(results) if results else f"No hotel results found for {query}."