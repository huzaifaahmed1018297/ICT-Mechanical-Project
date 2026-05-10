import streamlit as st
import pandas as pd

# --- APP CONFIGURATION ---
st.set_page_config(page_title="Mechanical Unit Converter", layout="centered")

# --- USER IDENTIFICATION (Required) ---
st.sidebar.markdown(f"""
    ## Developer Info
    **Name:** HUZAIFA AHMED  
    **Roll Number:** 25-ME-68
""")

st.title("Mechanical Unit Converter & Material Density Checker")
st.write("---")

# --- SECTION 1: UNIT CONVERTER ---
st.header("1. Mechanical Unit Converter")

col1, col2, col3 = st.columns(3)

with col1:
    value = st.number_input("Enter Value:", value=1.0)

with col2:
    conversion_type = st.selectbox("Category:", ["Pressure", "Power", "Length"])

with col3:
    if conversion_type == "Pressure":
        units = st.selectbox("To:", ["Pascal to PSI", "PSI to Pascal", "Bar to Pascal"])
    elif conversion_type == "Power":
        units = st.selectbox("To:", ["HP to Watts", "Watts to HP"])
    else:
        units = st.selectbox("To:", ["Inches to mm", "mm to Inches"])

# Conversion Logic
result = 0
if units == "Pascal to PSI":
    result = value * 0.000145038
elif units == "PSI to Pascal":
    result = value * 6894.76
elif units == "Bar to Pascal":
    result = value * 100000
elif units == "HP to Watts":
    result = value * 745.7
elif units == "Watts to HP":
    result = value / 745.7
elif units == "Inches to mm":
    result = value * 25.4
elif units == "mm to Inches":
    result = value / 25.4

st.success(f"**Result:** {result:.4f}")

st.write("---")

# --- SECTION 2: MATERIAL DENSITY CHECKER ---
st.header("2. Material Density Checker")

# Density Database (kg/m^3)
material_data = {
    "Material": ["Steel", "Aluminum", "Copper", "Cast Iron", "Titanium", "PVC", "Concrete", "Water"],
    "Density (kg/m³)": [7850, 2700, 8960, 7200, 4500, 1380, 2400, 1000]
}
df = pd.DataFrame(material_data)

selected_material = st.selectbox("Select a Material:", df["Material"])
density_val = df[df["Material"] == selected_material]["Density (kg/m³)"].values[0]

st.info(f"The density of **{selected_material}** is **{density_val} kg/m³**.")

# Display Table
with st.expander("View Full Density Table"):
    st.table(df)

# --- FOOTER ---
st.write("---")
st.caption(f"Developed by HUZAIFA AHMED | Roll No: 25-ME-68")
