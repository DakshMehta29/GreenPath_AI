from openrouter_setup import openai

def health_analyzer_agent(data: dict) -> dict:
    routine = data.get("activities", "")
    prompt = (
        "You're a fitness and health expert. Based on the user's routine, give a 1-10 health score "
        "and explain why in 2 short bullet points. Focus on sleep, exercise, food, and habits.\n\n"
        f"{routine}"
    )
    try:
        response = openai.ChatCompletion.create(
            model="openai/gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        data["health_analysis"] = response.choices[0].message.content
    except Exception as e:
        data["health_analysis"] = f"Health analysis error: {str(e)}"
    return data
