import streamlit as st
import pandas as pd

st.write('# Streamlit calculator')
number1= st.number_input('number 1')
number2 = st.number_input('number 2')
num3 = number1+number2
st.write('# Answer is ',num3)

name=st.text_input("Enter the your name")
Age=st.text_input("Enter the your age")
if st.button("Submit"):
    st.write(f"welcom to your platform {name} and your age is {Age}")

data={"Names":["umar",'Sahil','Raju'],
      "Place":["Bangalore","Delhi",'Chennai']
      }
df=pd.DataFrame(data)
st.write(df)


st.title("BMI Calculator")
weight = st.number_input("Enter your weight (kg):", min_value=1, max_value=500, value=70)
height = st.number_input("Enter your height (m):", min_value=0.5, max_value=3.0, value=1.75)
if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")
    if bmi < 18.5:
        st.write("Category: Underweight")
    elif 18.5 <= bmi < 24.9:
        st.write("Category: Normal weight")
    elif 25 <= bmi < 29.9:
        st.write("Category: Overweight")
    else:
        st.write("Category: Obese")
