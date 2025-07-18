#venv\Scripts\activate
# This is a Python script that activates a virtual environment
# and runs a Python script within that environment.
#deactivate
from langgraph_config import get_greenpath_graph

# Initialize the LangGraph
graph = get_greenpath_graph()

# ----------------------------
# 💬 Ask user questions
# ----------------------------
print("\n🌿 Welcome to GreenPath AI – Your Smart Lifestyle & Climate Advisor\n")

print("📝 Please answer the following questions about your daily routine:")

wake_time = input("1. ⏰ What time did you wake up today? ")
breakfast = input("2. 🍳 What did you eat for breakfast and when? ")
exercise = input("3. 🏃 Did you exercise today? What kind and for how long? ")
transport = input("4. 🚗 What transport did you use and how far did you travel? ")
ac_usage = input("5. ❄️ Did you use air conditioning or heating today? (Yes/No) ")
meals = input("6. 🍱 What else did you eat throughout the day (lunch, dinner, snacks)? ")
sleep_time = input("7. 😴 What time did you go to sleep? ")

# ----------------------------
# 😌 Mood check
# ----------------------------
print("\n🧠 How are you feeling today?")
mood_options = ["1. 😊 Happy", "2. 😐 Neutral", "3. 😴 Tired", "4. 😟 Anxious", "5. 😔 Sad"]
for option in mood_options:
    print(option)

mood_map = {
    "1": "Happy", "2": "Neutral", "3": "Tired", "4": "Anxious", "5": "Sad"
}
mood_choice = input("Choose your mood (1-5): ").strip()
mood = mood_map.get(mood_choice, "Neutral")

# ----------------------------
# 🧠 Combine to create routine
# ----------------------------
routine = (
    f"Woke up at {wake_time}, "
    f"had {breakfast}, "
    f"did {exercise if exercise else 'no'} exercise, "
    f"used transport: {transport}, "
    f"{'used AC/heating' if ac_usage.lower() == 'yes' else 'did not use AC'}, "
    f"ate {meals}, "
    f"went to bed at {sleep_time}."
)

# ----------------------------
# 🧪 Run AI agent graph
# ----------------------------
print("\n🚀 Analyzing your day using GreenPath AI...\n")
result = graph.invoke({"activities": routine, "mood": mood})

# ----------------------------
# ✅ Final Report
# ----------------------------
print("📘 GreenPath AI – Personalized Lifestyle Report\n" + "-" * 50)

if "carbon_analysis" in result:
    print(f"🌍 Carbon Footprint Analysis:\n{result['carbon_analysis']}\n")

if "health_analysis" in result:
    print(f"💪 Health & Lifestyle Analysis:\n{result['health_analysis']}\n")

if "eco_suggestions" in result:
    print(f"🌱 Eco-friendly Suggestions:\n{result['eco_suggestions']}\n")

if "wellness_tip" in result:
    print(f"🧘 Mental Wellness Tip:\n{result['wellness_tip']}\n")

if "smart_goals" in result:
    print(f"🎯 SMART Goals for This Week:\n{result['smart_goals']}\n")

print("-" * 50)
print("✅ Thank you for using GreenPath AI!")

