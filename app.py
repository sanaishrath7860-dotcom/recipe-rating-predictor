import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load('recipe_model.pkl')

st.title("🍽️ Recipe Rating Predictor")
st.write("Enter recipe details to predict if it will be highly rated!")

minutes = st.slider("Cooking Time (minutes)", 5, 300, 30)
n_steps = st.slider("Number of Steps", 1, 30, 10)
n_ingredients = st.slider("Number of Ingredients", 1, 30, 8)
calories = st.number_input("Calories", 50, 2000, 300)
protein = st.number_input("Protein (PDV%)", 0, 100, 20)

if st.button("Predict Rating"):
    input_data = pd.DataFrame([[minutes, n_steps, n_ingredients, 
                                0, 0, calories, 0, 0, 0, protein, 0, 0]],
        columns=['minutes','n_steps','n_ingredients_actual',
                 'steps_per_ingredient','rating_count','calories',
                 'total_fat_pdv','sugar_pdv','sodium_pdv',
                 'protein_pdv','sat_fat_pdv','carbs_pdv'])
    
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.success("⭐ This recipe is predicted to be HIGHLY RATED!")
    else:
        st.warning("This recipe may receive a lower rating.")
