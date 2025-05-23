import streamlit as st
import pandas as pd

def recidiv10cleanup():
    st.title("RECIDIV10 – Data Cleanup Overview")

    df = pd.read_csv("Data/CleanedRecidiv10.csv")
    df2 = pd.read_csv("Data/EncodedRecidiv10.csv")

    st.markdown("""
    <div style="border: 1px color: white; solid #ccc; padding: 15px; border-radius: 8px; background-color: black;">
    <h3>📊 What We Did</h3>

    This page explains how we prepared the <strong>RECIDIV10</strong> dataset for analysis.

    ---

    ### 🔄 Key Steps

    1. **Loaded raw CSV** with no headers (from Statistics Denmark)
    2. **Renamed columns** based on:
    - Recidivism event codes
    - Prior convictions
    - Sentence duration until reoffense
    - Gender and age group
    - Time period (e.g., 2009–2011, 2010–2012, etc.)
    3. **Melted** the data from wide to long format (for each time period and demographic group)
    4. **Mapped codes to labels**:
    - E.g., `"106"` → `"Ingen tilbagefald"`, `"3"` → `"3 Tidligere domme"`, etc.
    5. **Converted values** to numeric types where necessary (e.g., number of people)
    6. **Exported** two files:
    - `CleanedRecidiv10.csv`: labeled, readable data
    - `EncodedRecidiv10.csv`: label-encoded version for ML use

    ---

    ### 🎯 Goal

    The goal was to turn a raw official dataset into a clean, readable, and structured format that is:
    - Easy to visualize
    - Suitable for group-by analysis
    - Ready for modeling

    </div>
    """, unsafe_allow_html=True)

    # Show preview of cleaned data
    st.subheader("🧾 Preview of Cleaned Data")
    st.dataframe(df.head(10))

    st.subheader("🧾 Preview of Encoded Data")
    st.dataframe(df2.head(10))