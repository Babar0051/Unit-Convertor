import streamlit as st

# Dictionary of unit conversion factors
conversion_factors = {
    "Length": {
        "Metre": 1,
        "Centimetre": 100,
        "Millimetre": 1000,
        "Kilometre": 0.001,
        "Inch": 39.3701,
        "Foot": 3.28084,
        "Yard": 1.09361,
        "Mile": 0.000621371
    },
    "Weight": {
        "Kilogram": 1,
        "Gram": 1000,
        "Milligram": 1e6,
        "Pound": 2.20462,
        "Ounce": 35.274
    },
    "Temperature": {
        "Celsius": "C",
        "Fahrenheit": "F",
        "Kelvin": "K"
    }
}

# Streamlit UI
st.title("Unit Converter")

# Dropdown for selecting measurement type
unit_type = st.selectbox("Select measurement type:", list(conversion_factors.keys()))

# Dropdowns for selecting units
from_unit = st.selectbox("From:", list(conversion_factors[unit_type].keys()))
to_unit = st.selectbox("To:", list(conversion_factors[unit_type].keys()))

# Input for value to convert
value = st.number_input("Enter value:", value=1.0, step=0.1)

# Conversion logic
def convert(value, from_unit, to_unit, unit_type):
    if unit_type == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        return value  # Same unit case
    else:
        return value * (conversion_factors[unit_type][to_unit] / conversion_factors[unit_type][from_unit])

# Convert button
if st.button("Convert"):
    result = convert(value, from_unit, to_unit, unit_type)
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
