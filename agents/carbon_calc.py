from openrouter_setup import openai

def carbon_calc_agent(data: dict) -> dict:
    routine = data.get("activities", "")
    prompt = (
        "You're a sustainability expert. Analyze this routine and give a carbon score from 1 to 10 (higher = worse), "
        "then briefly explain in 2 bullet points why:\n\n"
        f"{routine}"
    )
    try:
        response = openai.ChatCompletion.create(
            model="openai/gpt-3.5-turbo",  # Can also use "anthropic/claude-3-haiku"
            messages=[{"role": "user", "content": prompt}],
        )
        data["carbon_analysis"] = response.choices[0].message.content
    except Exception as e:
        data["carbon_analysis"] = f"Carbon analysis error: {str(e)}"
    return data
