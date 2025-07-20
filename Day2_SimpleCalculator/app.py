# app.py

import streamlit as st

st.title("🧮 Simple Calculator - Day 2")
st.subheader("Basic Arithmetic Operations using Streamlit")

st.markdown("""
**Enter two numbers and select the operation:**
""")

# Input fields
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# Calculate button
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"Result: {num1} + {num2} = {result}")

    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"Result: {num1} - {num2} = {result}")

    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"Result: {num1} × {num2} = {result}")

    elif operation == "Division":
        if num2 == 0:
            st.error("❌ Cannot divide by zero.")
        else:
            result = num1 / num2
            st.success(f"Result: {num1} ÷ {num2} = {result}")
