# backend.py
# Core logic for the Personalized Workout & Diet Planner


# ---------------- BMI ----------------
def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = round(weight / (height_m ** 2), 1)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal Weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category


# ---------------- BMR ----------------
def calculate_bmr(weight, height, age, gender):
    if gender == "Male":
        return (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        return (10 * weight) + (6.25 * height) - (5 * age) - 161


# ---------------- CALORIES ----------------
def calculate_daily_calories(bmr, activity_level, goal):
    activity_multipliers = {
        "Low (Sedentary)": 1.2,
        "Moderate (Active)": 1.55,
        "High (Very Active)": 1.9
    }

    maintenance = bmr * activity_multipliers.get(activity_level, 1.2)

    if goal == "Weight Loss":
        target = maintenance - 500
        message = "You are in a calorie deficit to encourage weight loss."
    elif goal == "Muscle Gain":
        target = maintenance + 500
        message = "You are in a calorie surplus to support muscle growth."
    else:
        target = maintenance
        message = "You are at maintenance calories to stay fit."

    return round(maintenance), round(target), message


# ---------------- MACROS ----------------
def calculate_macros(target_calories):
    carbs_cal = target_calories * 0.5
    protein_cal = target_calories * 0.25
    fats_cal = target_calories * 0.25

    carbs_g = round(carbs_cal / 4)
    protein_g = round(protein_cal / 4)
    fats_g = round(fats_cal / 9)

    return carbs_g, protein_g, fats_g


# ---------------- WATER ----------------
def calculate_water_intake(weight):
    return round(weight * 0.033, 2)


# ---------------- WORKOUT ----------------
def get_workout_plan(goal, equipment):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if equipment == "No Equipment":
        routine = "Bodyweight HIIT & Core" if goal == "Weight Loss" else "Pushups, Squats, Lunges (3 sets)"
    elif equipment == "Dumbbells":
        routine = "Dumbbell Full Body Circuit"
    else:
        routine = "Gym-based Strength Training"

    plan = []
    for day in days:
        if day == "Sunday":
            plan.append({"Day": day, "Routine": "Rest & Recovery"})
        elif day == "Wednesday":
            plan.append({"Day": day, "Routine": "Active Recovery (Yoga/Walking)"})
        else:
            plan.append({"Day": day, "Routine": routine})

    return plan


# ---------------- DIET ----------------
def get_diet_plan(preference, budget):
    if preference == "Vegetarian":
        return [
            {"Meal": "Breakfast", "Suggestion": "Oatmeal with nuts and fruit"},
            {"Meal": "Lunch", "Suggestion": "Paneer/Tofu salad with brown rice"},
            {"Meal": "Snack", "Suggestion": "Greek yogurt or Roasted chickpeas"},
            {"Meal": "Dinner", "Suggestion": "Lentil soup (Dal) with 2 rotis"}
        ]
    elif preference == "Vegan":
        return [
            {"Meal": "Breakfast", "Suggestion": "Chia seed pudding with almond milk"},
            {"Meal": "Lunch", "Suggestion": "Quinoa and black bean bowl"},
            {"Meal": "Snack", "Suggestion": "Apple slices with peanut butter"},
            {"Meal": "Dinner", "Suggestion": "Chickpea curry with cauliflower rice"}
        ]
    else:
        return [
            {"Meal": "Breakfast", "Suggestion": "Scrambled eggs with whole grain toast"},
            {"Meal": "Lunch", "Suggestion": "Grilled chicken breast with broccoli"},
            {"Meal": "Snack", "Suggestion": "Protein shake or Almonds"},
            {"Meal": "Dinner", "Suggestion": "Baked fish with sweet potato"}
        ]


# ---------------- BUDGET ----------------
def estimate_budget(budget_level):
    estimates = {
        "Low": "$150 - $250",
        "Medium": "$300 - $500",
        "High": "$600+"
    }
    return estimates.get(budget_level, "N/A")