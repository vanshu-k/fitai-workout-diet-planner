# app.py
import streamlit as st
import pandas as pd
from backend import *

st.set_page_config(page_title="FitAI Planner", page_icon="💪", layout="wide")

st.title("💪 FitAI - Personalized Workout & Diet Planner")
st.write("Your Smart Fitness Companion")

# ---------------- SIDEBAR ----------------
st.sidebar.header("Enter Your Details")

name = st.sidebar.text_input("Name")
age = st.sidebar.number_input("Age", 10, 100, 20)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
weight = st.sidebar.number_input("Weight (kg)", 30.0, 200.0, 60.0)
height = st.sidebar.number_input("Height (cm)", 120.0, 220.0, 170.0)

activity_level = st.sidebar.selectbox(
    "Activity Level",
    ["Low (Sedentary)", "Moderate (Active)", "High (Very Active)"]
)

goal = st.sidebar.selectbox(
    "Fitness Goal",
    ["Weight Loss", "Muscle Gain", "Stay Fit"]
)

equipment = st.sidebar.selectbox(
    "Available Equipment",
    ["No Equipment", "Dumbbells", "Full Gym"]
)

diet_pref = st.sidebar.selectbox(
    "Diet Preference",
    ["Vegetarian", "Vegan", "Non-Vegetarian"]
)

budget = st.sidebar.selectbox(
    "Monthly Food Budget",
    ["Low", "Medium", "High"]
)

generate = st.sidebar.button("Generate My Plan")

# ---------------- MAIN ----------------
if generate:

    bmi, bmi_category = calculate_bmi(weight, height)
    bmr = calculate_bmr(weight, height, age, gender)
    maintenance, target, message = calculate_daily_calories(bmr, activity_level, goal)
    carbs, protein, fats = calculate_macros(target)
    water = calculate_water_intake(weight)

    workout_plan = get_workout_plan(goal, equipment)
    diet_plan = get_diet_plan(diet_pref, budget)
    budget_estimate = estimate_budget(budget)

    st.success(f"Hello {name}! Here's your personalized plan 💪")

    col1, col2, col3 = st.columns(3)
    col1.metric("BMI", bmi)
    col2.metric("BMR", int(bmr))
    col3.metric("Target Calories", target)

    st.info(f"BMI Category: {bmi_category}")
    st.write(message)

    # Smart Recommendation
    st.subheader("🧠 Smart Recommendation")
    if bmi > 30:
        st.warning("BMI indicates obesity. Consider professional medical advice.")
    elif bmi < 18.5:
        st.info("You are underweight. Focus on healthy calorie surplus and strength training.")
    else:
        st.success("You are in a healthy BMI range. Maintain consistency!")

    # Water Intake
    st.info(f"💧 Recommended Daily Water Intake: {water} Liters")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["🏋 Workout", "🥗 Diet", "📊 Calories", "🍽 Macros", "📈 Progress"]
    )

    with tab1:
        st.table(pd.DataFrame(workout_plan))

    with tab2:
        st.table(pd.DataFrame(diet_plan))
        st.write(f"💰 Estimated Monthly Budget: {budget_estimate}")

    with tab3:
        chart_data = pd.DataFrame({
            "Type": ["Maintenance", "Target"],
            "Calories": [maintenance, target]
        })
        st.bar_chart(chart_data.set_index("Type"))

    with tab4:
        macro_data = {
            "Carbs (g)": carbs,
            "Protein (g)": protein,
            "Fats (g)": fats
        }
        st.bar_chart(macro_data)

    with tab5:
        st.subheader("Track Your Weekly Weight")
        weekly_weight = st.number_input("Enter Current Weight (kg)", 30.0, 200.0)
        if weekly_weight:
            st.line_chart([weight, weekly_weight])

else:
    st.image("https://images.unsplash.com/photo-1554284126-aa88f22d8b74", width=900)
    st.write("### Welcome to FitAI Planner!")
    st.write("Fill in your details and click Generate to begin.")