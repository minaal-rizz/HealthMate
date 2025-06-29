import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Diet & Nutrition Guide", layout="centered")

# Title
st.title("🥗 Diet & Nutrition Guide")
st.markdown("Welcome to the Diet & Nutrition Guide! This site helps you calculate your daily nutritional needs based on your age, weight, and fitness goals.")
st.markdown("#### An 🍎 a day keeps the doctor away!")


# Sidebar
st.sidebar.header("Your Info")
age = st.sidebar.slider("Select your age", 10, 80, 25)
weight = st.sidebar.number_input("Enter your weight (kg)", 30, 200, 65)
goal = st.sidebar.selectbox("Your goal", ["Maintain Weight", "Lose Weight", "Gain Muscle"])

# Image 
try:
    img = Image.open("food.jpg")
    st.image(img, caption="Healthy Food", width=400)
except FileNotFoundError:
    st.warning("⚠️ 'food.jpeg' not found. Please add the image to the same directory.")



# Nutrition Calculation
st.header(" Recommended Daily Nutrition")

if goal == "Maintain Weight":
    calories = weight * 30
elif goal == "Lose Weight":
    calories = weight * 25
else:
    calories = weight * 35

protein = weight * 1.6
carbs = (calories * 0.5) / 4
fats = (calories * 0.3) / 9

st.markdown(f"""
- **Calories:** {int(calories)} kcal/day  
- **Protein:** {int(protein)} g/day  
- **Carbohydrates:** {int(carbs)} g/day  
- **Fats:** {int(fats)} g/day  
""")

# Meal Plan
st.header("🥣 Sample Meal Plan")
st.markdown("""
**Breakfast:** Oats + Banana + Boiled Eggs  
**Lunch:** Grilled Chicken + Brown Rice + Veggies  
**Snack:** Greek Yogurt + Nuts  
**Dinner:** Baked Fish + Quinoa + Salad  
""")
#bmi calculator
height = st.sidebar.number_input("Enter your height (cm)", 100, 250, 170)
bmi = weight / ((height / 100) ** 2)
st.sidebar.markdown(f"**BMI:** {bmi:.1f}")
if bmi < 18.5:
    st.sidebar.warning("Underweight")
elif bmi < 25:
    st.sidebar.success("Normal weight")
elif bmi < 30:
    st.sidebar.warning("Overweight")
else:
    st.sidebar.error("Obese")

#chart
labels = ['Carbs', 'Protein', 'Fats']
values = [carbs, protein, fats]
fig, ax = plt.subplots()
ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=50)
ax.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
st.subheader("Nutrient Distribution")
st.markdown("Here's a pie chart showing the distribution of your daily nutrients:")
st.pyplot(fig)

#tips
st.subheader("Tips for a Healthy Lifestyle")
with st.expander("💡 Click for tips"):
    st.markdown("""
    - Drink at least 2L of water daily  
    - Avoid sugary drinks  
    - Eat whole, unprocessed foods  
    - Don't skip breakfast  
    - Workout for atleast 30 minutes a day  
    - Get enough sleep (7-8 hours)
    - Consult a nutritionist for personalized advice
    """)

#rating 
feedback = st.slider("How helpful was this app?", 1,  3, 5)

# Footer
st.markdown("---")
st.markdown("Made using Streamlit")
