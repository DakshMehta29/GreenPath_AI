from openrouter_setup import openai

def goal_planner_agent(data: dict) -> dict:
    summary = (
        f"Carbon: {data.get('carbon_analysis', '')}\n"
        f"Health: {data.get('health_analysis', '')}\n"
        f"Eco Advice: {data.get('eco_suggestions', '')}\n"
        f"Mood Tip: {data.get('wellness_tip', '')}\n"
    )
    prompt = (
        "Based on the above summaries, create 3 SMART weekly goals for the user. "
        "One should improve health, one reduce carbon, and one support mental wellness. Keep it short."
    )
    try:
        response = openai.ChatCompletion.create(
            model="openai/gpt-3.5-turbo",
            messages=[{"role": "user", "content": summary + prompt}],
        )
        data["smart_goals"] = response.choices[0].message.content
    except Exception as e:
        data["smart_goals"] = f"Goal planner error: {str(e)}"
    return data
