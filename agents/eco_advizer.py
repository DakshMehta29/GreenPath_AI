from openrouter_setup import openai

def eco_advisor_agent(data: dict) -> dict:
    routine = data.get("activities", "")
    prompt = (
        "You're an eco-lifestyle advisor. Suggest 2 personalized, eco-friendly alternatives or improvements "
        "to reduce the carbon footprint based on this user's routine:\n\n"
        f"{routine}"
    )
    try:
        response = openai.ChatCompletion.create(
            model="openai/gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        data["eco_suggestions"] = response.choices[0].message.content
    except Exception as e:
        data["eco_suggestions"] = f"Eco advisor error: {str(e)}"
    return data
