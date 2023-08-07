import streamlit
import pandas as pd

streamlit.title("My Parent's New Healthy Diner")
streamlit.header("Breakfast Menu")

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
fruits_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
fruits_list.set_index('Fruits')

streamlit.multiselect("Select some fruits: ", list(fruits_list['Fruits']))
streamlit.dataframe(fruits_list)