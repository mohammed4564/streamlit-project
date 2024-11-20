import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train a Random Forest model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# User input for prediction
st.title("Iris Flower Prediction")

sepal_length = st.slider("Sepal Length", 4.0, 8.0, 5.5)
sepal_width = st.slider("Sepal Width", 2.0, 5.0, 3.0)
petal_length = st.slider("Petal Length", 1.0, 7.0, 4.0)
petal_width = st.slider("Petal Width", 0.1, 2.5, 1.5)

features = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = model.predict(features)
st.write(f"Predicted Class: {iris.target_names[prediction][0]}")

st.write('# Streamlit calculator')
number1= st.number_input('number 1')
number2 = st.number_input('number 2')
num3 = number1+number2
st.write('# Answer is ',num3)

name=st.text_input("Enter the your name")
Age=st.text_input("Enter the your age")
if st.button("Submit"):
    st.write(f"welcom to your platform {name} and your age is {Age}")

data={"Names":["khan",'Sahil','Raju'],
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
