import streamlit as st
import joblib
import numpy as np

# ---- PAGE CONFIGURATION ----
st.set_page_config(
    page_title="Employee Salary Predictor",
    page_icon="💼",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---- LOAD MACHINE LEARNING MODEL ----
try:
    model = joblib.load("Linearmodel.pkl")
    st.success("✅ Prediction model loaded successfully!")
except FileNotFoundError:
    st.error("❌ Error: 'Linearmodel.pkl' not found. Please ensure the model file is placed in the same directory as this application script.")
    st.stop()
except Exception as e:
    st.error(f"❌ An unexpected error occurred while loading the prediction model: {e}")
    st.stop()

# ---- CUSTOM CSS STYLING ----
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800;900&display=swap');

    html, body, [class*="stApp"] {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #a8edea, #fed6e3);
        color: #333333;
    }

    .main-title {
        font-size: 4.5rem !important;
        text-align: center;
        color: #000000;
        font-weight: 900;
        margin-bottom: 0.4em;
        letter-spacing: 1.5px;
        animation: fadeInDown 1s ease-out;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.2);
    }

    .sub-title {
        text-align: center;
        color: #444;
        font-size: 1.5rem;
        margin-bottom: 2em;
        font-weight: 500;
        animation: fadeIn 1.2s ease-out;
    }

    h2 {
        text-align: center;
        color: #2E7D32;
        font-weight: 700;
        margin-bottom: 1em;
    }

    .stNumberInput label {
        font-size: 1.6rem;
        color: #2E7D32;
        font-weight: 700;
        text-align: center;
        display: block;
    }

    .stNumberInput input {
        background: rgba(255, 255, 255, 0.5);
        border-radius: 10px;
        padding: 10px;
        font-size: 1.6rem;
        color: #1B5E20;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(0,0,0,0.2);
        backdrop-filter: blur(6px);
    }

    .stNumberInput input:focus {
        outline: none;
        border: 2px solid #4CAF50;
        box-shadow: 0 0 10px #81C784;
    }

    .stButton > button {
        background: linear-gradient(135deg, #4CAF50, #81C784);
        color: #fff;
        border: none;
        border-radius: 50px;
        padding: 1em 2em;
        font-size: 1.5rem;
        font-weight: 800;
        letter-spacing: 0.5px;
        box-shadow: 0 8px 25px rgba(76, 175, 80, 0.4);
        transition: all 0.3s ease-in-out;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #43A047, #66BB6A);
        transform: translateY(-2px) scale(1.05);
        box-shadow: 0 12px 30px rgba(67, 160, 71, 0.5);
    }

    .result-card {
        background: rgba(255, 255, 255, 0.4);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.25);
        backdrop-filter: blur(15px);
        text-align: center;
        animation: fadeInUp 1s ease-in-out;
        margin-top: 25px;
        border: 1px solid rgba(255,255,255,0.4);
    }

    .result-card h2 {
        font-size: 2.3rem;
        color: #2E7D32;
        margin-bottom: 0.6em;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.2);
    }

    .result-card p {
        font-size: 3.2rem;
        color: #1B5E20;
        font-weight: 800;
        letter-spacing: 0.5px;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.2);
    }

    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-30px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- HEADER SECTION ----
st.markdown('<p class="main-title">💼 Employee Salary Predictor</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Get quick salary estimations based on employee details</p>', unsafe_allow_html=True)

st.divider()

# ---- INPUT FORM SECTION ----
st.markdown('<h2 style="text-align: center; color: #2E7D32; font-weight: 700;">📋 Enter Employee Details</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    Years = st.number_input(
        "Years at Company",
        value=2,
        step=1,
        min_value=0,
        max_value=50,
        help="Enter the total number of years the employee has worked at the company. (e.g., 2 years)"
    )

with col2:
    JobRate = st.number_input(
        "Job Rating (1-5)",
        value=3.0,
        step=0.5,
        min_value=1.0,
        max_value=5.0,
        help="Enter the employee's performance rating (1=Low, 5=High). (e.g., 3.0 for average)"
    )

st.divider()

# ---- PREDICT BUTTON AND RESULT DISPLAY ----
predict = st.button("🔮 Predict Salary", use_container_width=True)

if predict:
    input_data = np.array([[Years, JobRate]])
    prediction = model.predict(input_data)
    st.toast("✅ Prediction successful!")
    st.markdown(
        f"""
        <div class="result-card">
            <h2>💰 Predicted Annual Salary</h2>
            <p>₹ {prediction[0]:,.2f}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.info("⬆️ Enter employee details in the fields above and click 'Predict Salary' to see the estimated annual salary.")

st.divider()

# ---- FOOTER SECTION ----
st.markdown(
    """
    <p style="text-align:center; color: #999; font-size: 0.9rem;">
    🔗 <i>Built with ❤️ & Edunet Foundation</i>
    </p>
    """,
    unsafe_allow_html=True
)
