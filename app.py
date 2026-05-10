import streamlit as st
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(page_title="Mechanical Unit Converter", layout="centered")

# --- 1. IMMEDIATE IDENTIFICATION SECTION ---
# This replaces the sidebar and shows up at the very top of the page
st.markdown(f"""
    <div style="background-color:#f0f2f6; padding:20px; border-radius:10px; border-left: 5px solid #ff4b4b;">
        <h2 style="margin:0;">Developer Identification</h2>
        <p style="margin:0; font-size:18px;"><b>Name:</b> HUZAIFA AHMED</p>
        <p style="margin:0; font-size:18px;"><b>Roll Number:</b> 25-ME-68</p>
    </div>
    """, unsafe_allow_html=True)

st.title("Mechanical Unit Converter & Material Density Checker")
st.write("---")

# --- 2. UNIT CONVERTER ---
st.header("1. Mechanical Unit Converter")

col1, col2, col3 = st.columns(3)
with col1:
    value = st.number_input("Enter Value:", value=1.0)
with col2:
    cat = st.selectbox("Category:", ["Pressure", "Power", "Length"])
with col3:
    if cat == "Pressure":
        units = st.selectbox("To:", ["Pascal to PSI", "PSI to Pascal"])
    elif cat == "Power":
        units = st.selectbox("To:", ["HP to Watts", "Watts to HP"])
    else:
        units = st.selectbox("To:", ["Inches to mm", "mm to Inches"])

# Logic
result = 0
if units == "Pascal to PSI": result = value * 0.000145
elif units == "PSI to Pascal": result = value * 6894.76
elif units == "HP to Watts": result = value * 745.7
elif units == "Watts to HP": result = value / 745.7
elif units == "Inches to mm": result = value * 25.4
elif units == "mm to Inches": result = value / 25.4

st.success(f"**Result:** {result:.4f}")
st.write("---")

# --- 3. MATERIAL DENSITY CHECKER ---
st.header("2. Material Density Checker")

material_data = {
    "Material": ["Steel", "Aluminum", "Copper", "Cast Iron", "Titanium"],
    "Density (kg/m³)": [7850, 2700, 8960, 7200, 4500]
}
df = pd.DataFrame(material_data)

selected_material = st.selectbox("Select a Material:", df["Material"])
density_val = df[df["Material"] == selected_material]["Density (kg/m³)"].values[0]

st.info(f"The density of **{selected_material}** is **{density_val} kg/m³**.")
st.table(df)
