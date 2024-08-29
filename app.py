import streamlit as st
import pandas as pd
import numpy as np

# Set the title of the web app
st.title("Ravi demo app")

# Add a text input widget
user_name = st.text_input("Enter your name:", "Ravi")

# Add a slider widget
slider_value = st.slider("Select a number:", 0, 100, 50)

# Display the input and slider values
st.write(f"Hello, {user_name}! You selected {slider_value}.")

# Create some random data and display a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.line_chart(chart_data)
