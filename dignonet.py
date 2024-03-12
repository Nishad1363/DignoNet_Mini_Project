import streamlit as st

# Title
st.title('My Streamlit Web App')

# Header
st.header('Welcome to My Web App')

# Subheader
st.subheader('Here, you can do cool stuff!')

# Text
st.write('This is a Streamlit web application.')

# Button
if st.button('Click me'):
    st.write('You clicked the button!')

# Slider
slider_value = st.slider('Select a value', 0, 100, 50)
st.write('Slider value:', slider_value)

# Plot
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)

# HTML and CSS
st.markdown("""
    <style>
        .custom-text {
            color: blue;
            font-size: 20px;
            font-weight: bold;
        }
        .custom-button {
            background-color: orange;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            border: none;
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)

# Custom HTML and CSS
st.markdown("""
    <p class="custom-text">This is a custom-styled text using HTML and CSS.</p>
    <button class="custom-button">Custom Button</button>
""", unsafe_allow_html=True)
