# 💪 Personalized Workout & Diet Planner using AI

A smart, rule-based fitness and nutrition planning application built with **Python** and **Streamlit**. This tool calculates key health metrics and generates a customized 7-day roadmap for users based on their physical profile, goals, and lifestyle.

## 🚀 Features

- **Personalized Metrics**: Calculates BMI (Body Mass Index) and BMR (Basal Metabolic Rate).
- **Calorie Targeting**: Uses the **Mifflin-St Jeor Formula** to determine daily maintenance and goal-specific calorie needs.
- **7-Day Workout Plan**: Dynamically generates routines based on available equipment (No Equipment, Dumbbells, or Full Gym).
- **Custom Diet Plan**: Tailors meal suggestions to food preferences (Vegetarian, Vegan, Non-Veg) and budget levels.
- **Interactive UI**: Features a clean sidebar for data entry and a dashboard with metrics, tables, and charts.

## 🛠️ Technologies Used

- **Python**: Core programming language.
- **Streamlit**: For the interactive web interface.
- **Pandas**: For data handling and table formatting.
- **Rule-Based AI**: Custom logic for personalized recommendations.

## 📂 Project Structure

- `app.py`: The main Streamlit application (UI/UX).
- `backend.py`: Core logic, formulas, and recommendation engine.
- `requirements.txt`: List of dependencies.
- `README.md`: Project documentation.

## 🏁 Getting Started

### Prerequisites
- Python 3.8 or higher installed.

### Installation
1. Clone or download this project folder.
2. Open your terminal/command prompt in the project directory.
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App
Launch the application by running:
```bash
streamlit run app.py
```

## 🧪 How It Works (The Science)

1. **BMR Calculation**: We use the **Mifflin-St Jeor Formula**, which is considered the most accurate for estimating resting energy expenditure.
   - *Male*: `(10 * weight) + (6.25 * height) - (5 * age) + 5`
   - *Female*: `(10 * weight) + (6.25 * height) - (5 * age) - 161`
2. **TDEE (Total Daily Energy Expenditure)**: BMR is multiplied by an activity factor (1.2 to 1.9) to find maintenance calories.
3. **Goal Adjustment**: 
   - Weight Loss: Maintenance - 500 kcal
   - Muscle Gain: Maintenance + 500 kcal
4. **Logic Engine**: A rule-based system maps your equipment and preferences to a curated database of exercises and meals.

## 🌟 Future Scope
- Integration with wearable devices (Fitbit/Apple Watch).
- Real-time progress tracking with a database.
- Advanced AI integration using LLMs for more conversational advice.

---
**Built for Academic Submission • 2026**
