import streamlit as st  # Import Streamlit for UI
from PIL import Image  # Import for displaying images/icons

# Function to convert units
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000,
    }

    key = f"{unit_from}_{unit_to}"
    if key in conversions:
        return value * conversions[key]
    elif unit_from == unit_to:
        return value  # Same unit, no conversion needed
    else:
        return None  # Unsupported conversion


# Streamlit UI setup
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# Custom CSS to make UI look better
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        border-radius: 8px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display app title with an emoji
st.title("🔄 Simple & Stylish Unit Converter")

# Add a cool image/icon (optional)
st.image("https://cdn-icons-png.flaticon.com/512/189/189665.png", width=100)

# User input section
st.markdown("### Enter the value you want to convert:")
value = st.number_input("🔢 Value:", min_value=1.0, step=1.0)

# Unit selection
col1, col2 = st.columns(2)
with col1:
    unit_from = st.selectbox("📏 Convert from:", ["meters", "kilometers", "grams", "kilograms"])
with col2:
    unit_to = st.selectbox("🎯 Convert to:", ["meters", "kilometers", "grams", "kilograms"])

# Conversion button with improved design
if st.button("🚀 Convert Now!"):
    result = convert_units(value, unit_from, unit_to)
    
    if result is not None:
        st.success(f"✅ **Converted Value:** {value} **{unit_from}** = **{result} {unit_to}**")
    else:
        st.error("❌ Conversion not supported. Please choose valid units.")

# Footer
st.markdown("---")
st.markdown("🎉 **Enjoy effortless conversions with this sleek tool!**")