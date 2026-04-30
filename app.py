import streamlit as st
from joblib import load
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Height Prediction System",
    page_icon="📏",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    return load("model.joblib")   # ✅ joblib instead of pickle

model = load_model()

# ---------------- HEADER ----------------
st.markdown("<h1 style='text-align:center;'>📏 Height Prediction System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Machine Learning based estimation of a child's adult height</p>", unsafe_allow_html=True)

st.divider()

# ---------------- PROJECT OVERVIEW ----------------
st.markdown("""
### 📌 Project Overview
This application predicts a child's **estimated adult height** using a **Machine Learning model**.

⚠️ **Note:** Prediction is an estimate.
""")

# ---------------- SIDEBAR ----------------
st.sidebar.header("🧾 Enter Input Details")

father = st.sidebar.number_input("Father Height (cm)", 100.0, 250.0, step=0.1)
mother = st.sidebar.number_input("Mother Height (cm)", 100.0, 250.0, step=0.1)
children = st.sidebar.number_input("Total Number of Children", min_value=1, step=1)
childNum = st.sidebar.number_input("Child Birth Order", min_value=1, step=1)

gender = st.sidebar.selectbox(
    "Gender", [0, 1],
    format_func=lambda x: "Female" if x == 0 else "Male"
)

predict_btn = st.sidebar.button("🔍 Predict Height")

# ---------------- LAYOUT ----------------
col1, col2 = st.columns(2)

# ---------------- INPUT DISPLAY ----------------
with col1:
    st.subheader("📊 Input Summary")
    st.write(f"Father Height: {father} cm")
    st.write(f"Mother Height: {mother} cm")
    st.write(f"Children: {children}")
    st.write(f"Birth Order: {childNum}")
    st.write(f"Gender: {'Male' if gender else 'Female'}")

# ---------------- PREDICTION ----------------
with col2:
    st.subheader("📈 Prediction Result")

    if predict_btn:
        try:
            # Feature engineering
            mid_parent = (father + mother) / 2
            features = [[mid_parent, children, childNum, gender]]

            prediction = model.predict(features)[0]

            mae = 5.5
            lower, upper = prediction - mae, prediction + mae

            st.success(f"📏 Predicted Height: {prediction:.2f} cm")
            st.info(f"📊 Range: {lower:.1f} – {upper:.1f} cm")

            # -------- BAR CHART --------
            fig1, ax1 = plt.subplots()
            ax1.bar(["Father", "Mother", "Child"], [father, mother, prediction])
            ax1.set_ylabel("Height (cm)")
            st.pyplot(fig1)

            # -------- POSITION --------
            fig2, ax2 = plt.subplots()
            ax2.axvline(father, linestyle="--", label="Father")
            ax2.axvline(mother, linestyle="--", label="Mother")
            ax2.axvline(prediction, linestyle="-", label="Predicted")
            ax2.legend()
            st.pyplot(fig2)

        except Exception as e:
            st.error(f"Error: {e}")

# ---------------- FOOTER ----------------
st.divider()
st.caption("Developed by Shivprasad Vanshete")