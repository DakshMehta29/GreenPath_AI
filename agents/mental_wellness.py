from openrouter_setup import openai

def mental_wellness_agent(data: dict) -> dict:
    mood = data.get("mood", "Neutral")
    prompt = (
        f"The user feels {mood}. Suggest one calming or mood-lifting daily wellness habit "
        "that's also eco-conscious (e.g., walk in nature, digital detox, meditation)."
    )
    try:
        response = openai.ChatCompletion.create(
            model="openai/gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        data["wellness_tip"] = response.choices[0].message.content
    except Exception as e:
        data["wellness_tip"] = f"Mental wellness error: {str(e)}"
    return data
