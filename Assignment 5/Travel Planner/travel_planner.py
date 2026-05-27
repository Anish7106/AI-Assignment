"""
AI Based Travel Planner using simple reusable knowledge bases.

Knowledge bases reused:
1. Tourist places KB
2. Food recommendation KB
3. Wine pairing KB
4. Cost estimation KB
5. Personalized tour rule base

"""


TOURIST_PLACES = {
    "Paris": [
        {"name": "Eiffel Tower", "type": "landmark", "time_hours": 2, "cost": 30},
        {"name": "Louvre Museum", "type": "museum", "time_hours": 4, "cost": 25},
        {"name": "Seine River Walk", "type": "nature", "time_hours": 2, "cost": 0},
        {"name": "Montmartre", "type": "culture", "time_hours": 3, "cost": 10}
    ],
    "Rome": [
        {"name": "Colosseum", "type": "history", "time_hours": 3, "cost": 20},
        {"name": "Vatican Museums", "type": "museum", "time_hours": 4, "cost": 25},
        {"name": "Trevi Fountain", "type": "landmark", "time_hours": 1, "cost": 0},
        {"name": "Trastevere", "type": "food", "time_hours": 3, "cost": 15}
    ],
    "Hyderabad": [
        {"name": "Charminar", "type": "history", "time_hours": 2, "cost": 5},
        {"name": "Golconda Fort", "type": "history", "time_hours": 3, "cost": 10},
        {"name": "Hussain Sagar", "type": "nature", "time_hours": 2, "cost": 5},
        {"name": "Ramoji Film City", "type": "entertainment", "time_hours": 6, "cost": 40}
    ]
}


FOOD_KB = {
    "Paris": ["Croissant", "Ratatouille", "Crepes", "Macarons"],
    "Rome": ["Pasta Carbonara", "Pizza Margherita", "Gelato", "Tiramisu"],
    "Hyderabad": ["Hyderabadi Biryani", "Haleem", "Dosa", "Irani Chai"]
}


WINE_KB = {
    "Croissant": "Champagne",
    "Ratatouille": "Pinot Noir",
    "Pasta Carbonara": "Frascati",
    "Pizza Margherita": "Chianti",

    "Hyderabadi Biryani": "Sweet Lassi",
    "Haleem": "Rose Milk",
    "Dosa": "Filter Coffee",
    "Irani Chai": "Osmania Biscuits and Tea"
}


DAILY_BASE_COST = {
    "budget": 40,
    "standard": 80,
    "luxury": 180
}


def recommend_places(city, interests, available_hours):
    places = TOURIST_PLACES.get(city, [])

    scored_places = []
    for place in places:
        score = 0

        if place["type"] in interests:
            score += 10

        if place["cost"] == 0:
            score += 2

        if place["time_hours"] <= available_hours:
            score += 3

        scored_places.append((score, place))

    scored_places.sort(reverse=True, key=lambda x: x[0])

    plan = []
    used_hours = 0
    for score, place in scored_places:
        if used_hours + place["time_hours"] <= available_hours:
            plan.append(place)
            used_hours += place["time_hours"]

    return plan


def recommend_food(city):
    foods = FOOD_KB.get(city, [])
    result = []

    for food in foods:
        pairing = WINE_KB.get(food, "Local drink")
        result.append({"food": food, "drink_pairing": pairing})

    return result


def estimate_cost(city, days, travel_style, selected_places):
    base = DAILY_BASE_COST.get(travel_style, 80) * days
    attraction_cost = sum(place["cost"] for place in selected_places)
    food_cost = 25 * days if travel_style == "budget" else 50 * days
    total = base + attraction_cost + food_cost

    return {
        "stay_transport_cost": base,
        "attraction_cost": attraction_cost,
        "food_cost": food_cost,
        "estimated_total": total
    }


def build_travel_plan(user):
    city = user["city"]
    days = user["days"]
    interests = user["interests"]
    travel_style = user["travel_style"]

    total_available_hours = days * 8

    places = recommend_places(city, interests, total_available_hours)
    food = recommend_food(city)
    cost = estimate_cost(city, days, travel_style, places)

    return {
        "city": city,
        "days": days,
        "selected_places": places,
        "food_recommendations": food,
        "cost_estimate": cost
    }


def print_plan(plan):
    print("\nAI TRAVEL PLAN")
    print("City:", plan["city"])
    print("Days:", plan["days"])

    print("\nPlaces:")
    for place in plan["selected_places"]:
        print("-", place["name"], "| Type:", place["type"], "| Time:", place["time_hours"], "hrs | Cost:", place["cost"])

    print("\nFood and Drink Recommendations:")
    for item in plan["food_recommendations"]:
        print("-", item["food"], "->", item["drink_pairing"])

    print("\nCost Estimate:")
    for k, v in plan["cost_estimate"].items():
        print("-", k, ":", v)


if __name__ == "__main__":
    user_profile = {
        "city": "Hyderabad",
        "days": 2,
        "interests": ["history", "food", "nature"],
        "travel_style": "budget"
    }

    plan = build_travel_plan(user_profile)
    print_plan(plan)
