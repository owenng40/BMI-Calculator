# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bkFgKlO_6u0zfTmmi3qE6sMnULZVHdnn
"""

import streamlit as st
st.title("BMI Calculator")
mass = st.number_input("Enter weight in kg", step = 0.1)
height = st.number_input("Enter your height in metres", step = 0.01)
button = st.button("Calculate BMI")
if button:
  bmi = mass/(height)**2
  st.success(f"Your BMI is {bmi}.")
  if bmi > 18.5 and bmi < 23:
    st.success("You are AT LOW RISK for obesity-related diseases.")
  if bmi >= 23 and bmi < 27.5:
    st.success("You are AT MODERATE RISK for obesity-related diseases.")
  if bmi >= 27.5:
    st.success("You are AT HIGH RISK for obesity-related diseases.")
  if bmi <= 18.5:
    st.success("You are at risk nutritional deficiency diseases and osteoporosis.")
