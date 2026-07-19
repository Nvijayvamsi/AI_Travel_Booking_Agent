import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AVIATIONSTACK_API_KEY")


def search_flights(query):
    if not API_KEY:
        return (
            f"Demo flight options for {query}:\n"
            "- Airline: SkyJet\n"
            "- Departure: City Center Airport\n"
            "- Arrival: Destination Airport\n"
            "- Status: Scheduled"
        )

    url = "http://api.aviationstack.com/v1/flights"
    params = {"access_key": API_KEY, "limit": 5}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except Exception:
        return f"Unable to fetch live flights for {query}; please check the API key."

    flights = []
    if "data" in data:
        for flight in data["data"][:5]:
            airline = flight.get("airline", {}).get("name", "Unknown")
            departure = flight.get("departure", {}).get("airport", "Unknown")
            arrival = flight.get("arrival", {}).get("airport", "Unknown")
            status = flight.get("flight_status", "Unknown")
            flights.append(
                f"Airline: {airline}\nDeparture: {departure}\nArrival: {arrival}\nStatus: {status}"
            )

    return "\n\n".join(flights) if flights else f"No flight data found for {query}."