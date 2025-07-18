import streamlit as st
from langgraph_config import get_greenpath_graph

# Load the compiled LangGraph
graph = get_greenpath_graph()

# ------------------ Page Setup ------------------
st.set_page_config(page_title="GreenPath AI", page_icon="🌿", layout="centered")

st.markdown("<h1 style='text-align: center; color: #228B22;'>🌿 GreenPath AI</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Your Smart Lifestyle & Climate Advisor</h4>", unsafe_allow_html=True)
st.markdown("---")

# ------------------ Input Form ------------------
st.markdown("### 📝 Tell us about your day")

with st.form("daily_routine_form"):
    wake_time = st.text_input("⏰ What time did you wake up today?")
    breakfast = st.text_input("🍳 What did you eat for breakfast and when?")
    exercise = st.text_input("🏃 Did you exercise? What kind and for how long?")
    transport = st.text_input("🚗 What transport did you use and how far did you travel?")
    ac_usage = st.selectbox("❄️ Did you use air conditioning or heating today?", ["No", "Yes"])
    meals = st.text_input("🍱 What else did you eat (lunch, dinner, snacks)?")
    sleep_time = st.text_input("😴 What time did you go to sleep?")

    st.markdown("### 🧠 How are you feeling today?")
    mood = st.radio("Select your mood:", ["😊 Happy", "😐 Neutral", "😴 Tired", "😟 Anxious", "😔 Sad"], index=1)

    submitted = st.form_submit_button("🚀 Analyze My Day")

# ------------------ Run LangGraph ------------------
if submitted:
    # Combine answers into a full routine string
    routine = (
        f"Woke up at {wake_time}, "
        f"had {breakfast}, "
        f"did {exercise if exercise else 'no'} exercise, "
        f"used transport: {transport}, "
        f"{'used AC/heating' if ac_usage == 'Yes' else 'did not use AC'}, "
        f"ate {meals}, "
        f"went to bed at {sleep_time}."
    )

    st.markdown("---")
    st.info("Analyzing your routine with GreenPath AI agents...")

    with st.spinner("Please wait while we generate your personalized feedback..."):
        result = graph.invoke({"activities": routine, "mood": mood})

    st.success("✅ Your personalized insights are ready!")

    # ------------------ Output Sections ------------------
    st.markdown("### 🌍 Carbon Footprint Analysis")
    st.write(result.get("carbon_analysis", "No data"))

    st.markdown("### 💪 Health & Lifestyle Analysis")
    st.write(result.get("health_analysis", "No data"))

    st.markdown("### 🌱 Eco-friendly Suggestions")
    st.write(result.get("eco_suggestions", "No data"))

    st.markdown("### 🧘 Mental Wellness Tip")
    st.write(result.get("wellness_tip", "No data"))

    st.markdown("### 🎯 SMART Goals for This Week")
    st.write(result.get("smart_goals", "No data"))
