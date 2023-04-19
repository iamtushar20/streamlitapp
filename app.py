import streamlit as st

def largest_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

st.title("Find the largest among the 3 given numbers")
st.write("Enter the three numbers below:")

a = st.number_input("Enter the first number")
b = st.number_input("Enter the second number")
c = st.number_input("Enter the third number")

if st.button("Find the largest number"):
    result = largest_number(a, b, c)
    st.write(f"The largest number is {result}")
