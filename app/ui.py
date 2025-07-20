# app/ui.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from app.converter import convert_sql_to_python, init_vertex_ai

# Init Gemini / Vertex AI once
init_vertex_ai()

st.set_page_config(page_title="SQL to Python Converter", layout="centered")
st.title("SQL ➜ Python Converter with Gemini")

st.markdown("""
This app uses Google Gemini (via Vertex AI) to convert legacy SQL queries into Python code using Pandas or PySpark.

Upload a SQL file or paste your SQL below.
""")

# Upload SQL file or paste
sql_code = ""
uploaded_file = st.file_uploader("Upload .sql file", type=["sql"])
if uploaded_file:
    sql_code = uploaded_file.read().decode("utf-8")
else:
    sql_code = st.text_area("Paste your SQL here", height=200)

# Target framework
framework = st.selectbox("Target Python Framework", ["pandas", "pyspark"])

# Convert Button
if st.button("Convert to Python"):
    if not sql_code.strip():
        st.warning("Please upload or paste some SQL code first.")
    else:
        with st.spinner("Calling Gemini..."):
            try:
                python_code = convert_sql_to_python(sql_code, target_framework=framework)
                st.success("Conversion complete!")
                st.code(python_code, language='python')

                # Allow download
                st.download_button(
                    label="⬇ Download Python Code",
                    data=python_code,
                    file_name="converted_sql.py",
                    mime="text/x-python"
                )
            except Exception as e:
                st.error(f"Error during conversion: {e}")