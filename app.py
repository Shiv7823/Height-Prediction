import streamlit as st
import pickle
import matplotlib.pyplot as plt
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Height Prediction System",
    page_icon="📏",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

# ---------------- HEADER ----------------
st.markdown(
    "<h1 style='text-align:center;'>📏 Height Prediction System</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>Machine Learning based estimation of a child's adult height</p>",
    unsafe_allow_html=True
)

st.divider()

# ---------------- PROJECT OVERVIEW ----------------
st.markdown("""
### 📌 Project Overview
This application predicts a child's **estimated adult height** using a **Machine Learning model** trained on real-world parental and demographic data.

⚠️ **Note:**  
This prediction is an *estimate*, not an exact value, as biological growth depends on multiple factors.
""")

# ---------------- SIDEBAR INPUTS ----------------
st.sidebar.header("🧾 Enter Input Details")

father = st.sidebar.number_input(
    "Father Height (cm)", 100.0, 250.0, step=0.1,
    help="Father's height has a strong genetic influence"
)

mother = st.sidebar.number_input(
    "Mother Height (cm)", 100.0, 250.0, step=0.1,
    help="Mother's height contributes genetically"
)

children = st.sidebar.number_input(
    "Total Number of Children", min_value=1, step=1,
    help="Used to model family size patterns"
)

childNum = st.sidebar.number_input(
    "Child Birth Order", min_value=1, step=1,
    help="Birth order may slightly influence growth"
)

gender = st.sidebar.selectbox(
    "Gender", [0, 1],
    format_func=lambda x: "Female" if x == 0 else "Male",
    help="Gender affects average height"
)

predict_btn = st.sidebar.button("🔍 Predict Height")

# ---------------- MAIN LAYOUT ----------------
col1, col2 = st.columns(2)

# ---------------- INPUT SUMMARY ----------------
with col1:
    st.subheader("📊 Input Summary")
    st.write(f"**Father Height:** {father} cm")
    st.write(f"**Mother Height:** {mother} cm")
    st.write(f"**Total Children:** {children}")
    st.write(f"**Child Birth Order:** {childNum}")
    st.write(f"**Gender:** {'Male' if gender == 1 else 'Female'}")

# ---------------- PREDICTION & VISUALS ----------------
with col2:
    st.subheader("📈 Prediction Result")

    if predict_btn:
        # Feature engineering (MUST match training)
        mid_parent = (father + mother) / 2
        features = [[mid_parent, children, childNum, gender]]

        prediction = model.predict(features)[0]

        # Error margin (use your MAE)
        mae = 5.5
        lower = prediction - mae
        upper = prediction + mae

        st.success(f"📏 Predicted Height: **{prediction:.2f} cm**")
        st.info(f"📊 Expected Range: **{lower:.1f} – {upper:.1f} cm**")

        # ---------------- BAR CHART ----------------
        st.subheader("📊 Height Comparison")
        fig1, ax1 = plt.subplots()
        ax1.bar(
            ["Father", "Mother", "Predicted Child"],
            [father, mother, prediction],
        )
        ax1.set_ylabel("Height (cm)")
        st.pyplot(fig1)

        # ---------------- POSITION CHART ----------------
        st.subheader("📈 Height Positioning")
        fig2, ax2 = plt.subplots()
        ax2.plot([father, mother], [1, 1], "o", label="Parents")
        ax2.axvline(prediction, color="green", linestyle="--", label="Predicted Height")
        ax2.set_yticks([])
        ax2.set_xlabel("Height (cm)")
        ax2.set_title("Relative Height Position")
        ax2.legend()
        st.pyplot(fig2)

# ---------------- DATASET INFO ----------------
st.divider()
st.subheader("📂 Dataset & Model Information")

st.write("""
- **Dataset Size:** 936 records  
- **Model Used:** Random Forest Regressor  
- **Target Variable:** Height (cm)  
- **Feature Engineering:** Mid-parent height used  
""")

# ---------------- LIMITATIONS ----------------
with st.expander("ℹ️ Model Details & Limitations"):
    st.write("""
    **Limitations of the Model:**
    - Age, nutrition, and environmental factors are not included
    - Predictions are statistical estimates
    - Individual variations may exist

    **Best Use Case:**  
    Educational, analytical, and demonstration purposes
    """)

# ---------------- FOOTER ----------------
st.divider()
st.caption("Developed by Shivprasad Vanshete | Machine Learning Project")
