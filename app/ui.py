
import streamlit as st
from app.converter import convert_sql_to_python, init_vertex_ai
from app.validator import run_sql_on_data, run_python_on_data, compare_outputs
import os

# Initialize Gemini
init_vertex_ai()

# Session state initialization
if "python_code" not in st.session_state:
    st.session_state.python_code = None
if "sql_code" not in st.session_state:
    st.session_state.sql_code = None
if "converted" not in st.session_state:
    st.session_state.converted = False

# Streamlit UI
st.set_page_config(page_title="SQL to Python Converter", layout="centered")
st.title("🧠 SQL ➜ Python Converter using Gemini")

st.markdown("Upload a SQL file or paste your SQL code below.")

# Input SQL
sql_input = ""
uploaded_file = st.file_uploader("Upload .sql file", type=["sql"])
if uploaded_file:
    sql_input = uploaded_file.read().decode("utf-8")
else:
    sql_input = st.text_area("Paste your SQL here", height=200)

# Framework selector
framework = st.selectbox("Target Python Framework", ["pandas", "pyspark"])

# Convert button
if st.button("Convert to Python"):
    if not sql_input.strip():
        st.warning("Please upload or paste SQL code.")
    else:
        with st.spinner("Calling Gemini..."):
            try:
                python_code = convert_sql_to_python(sql_input, target_framework=framework)
                st.session_state.python_code = python_code
                st.session_state.sql_code = sql_input
                st.session_state.converted = True
                st.success("Conversion complete.")
            except Exception as e:
                st.error(f"Error during conversion: {e}")
                st.session_state.converted = False

# Display result and validation
if st.session_state.converted:
    st.subheader("Generated Python Code")
    st.code(st.session_state.python_code, language='python')

    st.download_button(
        label="⬇ Download Python Code",
        data=st.session_state.python_code,
        file_name="converted_sql.py",
        mime="text/x-python"
    )

    st.markdown("---")
    if st.checkbox("✅ Validate Output Against Sample Data"):
        sample_csv = os.path.join("data", "sample_data.csv")
        if not os.path.exists(sample_csv):
            st.error("Sample data not found at /data/sample_data.csv")
        else:
            with st.spinner("Running validation..."):
                sql_df = run_sql_on_data(st.session_state.sql_code, sample_csv)
                py_df = run_python_on_data(st.session_state.python_code, sample_csv)

                if sql_df is not None and py_df is not None:
                    if compare_outputs(sql_df, py_df):
                        st.success("✅ Validation passed. SQL and Python outputs match.")
                    else:
                        st.error("❌ Validation failed. Outputs are different.")
                else:
                    st.warning("⚠️ One or both executions failed.")
