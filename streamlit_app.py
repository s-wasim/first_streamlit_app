import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError 

streamlit.title("My Parent's New Healthy Diner")
streamlit.header("Breakfast Menu")

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

fruits_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
selected_fruits = streamlit.multiselect('Pick some fruits: ', list(fruits_list['Fruit']))

fruits_list = fruits_list.set_index('Fruit')
fruits_to_show = fruits_list.loc[list(selected_fruits)]
streamlit.dataframe(fruits_to_show if len(fruits_to_show) > 0 else fruits_list)

streamlit.header('Fruityvice Fruit Advice!')
advice_fruit = streamlit.text_input('What food would you like information about?: ')
response_advice = requests.get(f"https://www.fruityvice.com/api/fruit/{advice_fruit if len(advice_fruit) > 0 else 'watermelon'}")
streamlit.dataframe(pd.json_normalize(response_advice.json()).set_index('name'))


streamlit.stop()
# Getting data from SF
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute('SELECT FRUIT_NAME FROM PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST')
res_set = my_cur.fetchall()

# Appending data to SF
new_fruit = streamlit.text_input(label='Add fruits: ')
if len(new_fruit) > 0:
    my_cur.execute(f"INSERT INTO PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST VALUES ('{new_fruit}')")

streamlit.dataframe(res_set)
