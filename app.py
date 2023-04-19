import streamlit as st

def largest_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

st.title("Find the Largest Number")

num1 = st.number_input("Enter the first number", value=0, step=1)
num2 = st.number_input("Enter the second number", value=0, step=1)
num3 = st.number_input("Enter the third number", value=0, step=1)

if st.button("Find Largest Number"):
    if isinstance(num1, int) and isinstance(num2, int) and isinstance(num3, int):
        result = largest_number(num1, num2, num3)
        st.success(f"The largest number is: {result}")
    else:
        st.warning("Please enter integer values for all three numbers.")
