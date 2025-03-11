
import streamlit as st

# Conversion Type Selection
conversion_type = st.selectbox("🔧 Select conversion type:" , ["📏 Length", "⚖️ Weight", "🌡 Temperature", "💱 Currency to PKR"])

# Input Value
value = st.number_input("✏️ Enter value:", min_value=0.0)

# Conversion Functions
def length_conversion(value, from_unit, to_unit):
    conversion_factors = {"meters": 1, "kilometers": 0.001, "miles": 0.000621371, "feet": 3.28084}
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def weight_conversion(value, from_unit, to_unit):
    conversion_factors = {"grams": 1, "kilograms": 0.001, "pounds": 0.00220462}
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    return value

def currency_conversion_to_pkr(value, from_unit):
    conversion_rates = {
        "US Dollar (USD)": 280.5, "Euro (EUR)": 307.15, "British Pound (GBP)": 360.20,
        "Indian Rupee (INR)": 3.38, "Pakistani Rupee (PKR)": 1, "Australian Dollar (AUD)": 182.45,
        "Canadian Dollar (CAD)": 207.50, "Japanese Yen (JPY)": 1.86, "Chinese Yuan (CNY)": 39.45
    }
    return value * conversion_rates[from_unit]

# Conversion Logic
if conversion_type == "📏 Length":
    from_unit = st.selectbox("📍 From Unit:", ["meters", "kilometers", "miles", "feet"])
    to_unit = st.selectbox("📍 To Unit:", ["meters", "kilometers", "miles", "feet"])
    result = length_conversion(value, from_unit, to_unit)

elif conversion_type == "⚖️ Weight":
    from_unit = st.selectbox("⚖️ From Unit:", ["grams", "kilograms", "pounds"])
    to_unit = st.selectbox("⚖️ To Unit:", ["grams", "kilograms", "pounds"])
    result = weight_conversion(value, from_unit, to_unit)

elif conversion_type == "🌡 Temperature":
    from_unit = st.selectbox("🌡 From Unit:", ["Celsius", "Fahrenheit"])
    to_unit = st.selectbox("🌡 To Unit:", ["Celsius", "Fahrenheit"])
    result = temperature_conversion(value, from_unit, to_unit)

elif conversion_type == "💱 Currency to PKR":
    from_unit = st.selectbox("💵 From Currency:", ["US Dollar (USD)", "Euro (EUR)", "British Pound (GBP)", "Indian Rupee (INR)", "Australian Dollar (AUD)", "Canadian Dollar (CAD)", "Japanese Yen (JPY)", "Chinese Yuan (CNY)"])
    result = currency_conversion_to_pkr(value, from_unit)

# Display Result with Emoji
st.write(f"✅ **Converted Value:** `{result}` 🎯")

