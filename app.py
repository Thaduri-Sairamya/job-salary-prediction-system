import streamlit as st
import joblib
from pathlib import Path

st.set_page_config(
    page_title="Job Salary Prediction",
    page_icon="💼"
)

st.title("💼 Job Salary Prediction")

st.write("Application started successfully.")

model_path = Path(__file__).parent / "ai_job_salary_model_compressed.pkl"

if not model_path.exists():
    st.error("❌ Model file was not found.")
else:
    st.success("✅ Model file found.")

    st.write("Loading model...")

    try:
        model = joblib.load(model_path)

        st.success("✅ Model loaded successfully!")

        st.write("Your salary prediction model is ready.")

    except Exception as e:
        st.error("❌ Model loading failed.")
        st.exception(e)

