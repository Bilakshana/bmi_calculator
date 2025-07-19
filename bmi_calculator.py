import streamlit as st

st.title("🩺📊 BMI Calculator")

# Taking inputs
age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)
weight = st.number_input("Please enter your weight (in KG):", min_value=0.0, format="%.2f")
feet = st.number_input("Enter your height (feet):", min_value=0, step=1)
inches = st.number_input("Enter your height (inches):", min_value=0, max_value=11, step=1)

# Creating button
if st.button("Calculate BMI"):

    # Stop execution if age less than 18
    if age < 18:
        st.info("BMI calculation is not provided for children under 18 years old.")
        st.stop()  # stop program here

    # Validate inputs
    if weight == 0 or (feet == 0 and inches == 0):
        st.warning("Please enter valid weight and height.")
        st.stop()

    # Calculate BMI
    total_inches = feet * 12 + inches
    height_in_meters = total_inches * 0.0254
    BMI = weight / (height_in_meters ** 2)
    bmi = round(BMI, 2)

    # Display result
    st.success(f"Your BMI is {bmi}")

    # BMI categories for adults (18+)
    if bmi < 16:
        st.error("You are severely underweight. Please consult a doctor.")
    elif 16 <= bmi < 18.5:
        st.warning("You are underweight. Consider a balanced diet.")
    elif 18.5 <= bmi < 25:
        st.success("You have a healthy BMI. Keep it up!")
    elif 25 <= bmi < 30:
        st.info("You are overweight. Some lifestyle changes may help.")
    else:  
        st.error("You are obese. Please consult a healthcare provider.")
