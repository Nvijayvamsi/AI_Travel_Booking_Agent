from main import build_travel_plan


def test_demo_plan_contains_destination_and_day_structure():
    result = build_travel_plan("Plan a 3-day trip to Tokyo")
    final_response = result.get("final_response", "")

    assert "Tokyo" in final_response
    assert "3-day" in final_response or "3 days" in final_response
    assert "Day 1" in final_response
