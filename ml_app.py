import streamlit as st
import joblib
import os
import numpy as np

# Model yükleme fonksiyonu
@st.cache_data
def load_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file), "rb"))
    return loaded_model

# Makine öğrenmesi uygulaması
def run_ml_app():
    st.subheader("Machine Learning Section")
    loaded_model = load_model("log_model.sav")

    with st.expander("Attributes Info"):
        attrib_info = """
        #### Attribute Information:
        - Pregnancies
        - Glucose
        - BloodPressure
        - SkinThickness
        - Insulin
        - BMI
        - DiabetesPedigreeFunction
        - Age
        """
        st.markdown(attrib_info, unsafe_allow_html=True)

    # Kullanıcıdan veri girişi
    col1, col2 = st.columns(2)
    with col1:
        Pregnancies = st.number_input("Pregnancies", 0, 20)
        Glucose = st.number_input("Glucose", 0, 200)
        BloodPressure = st.number_input("BloodPressure", 0, 150)
        SkinThickness = st.number_input("SkinThickness", 0, 100)

    with col2:
        Insulin = st.number_input("Insulin", 0, 1000)
        BMI = st.number_input("BMI", 0.0, 70.0)
        DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction", 0.0, 2.5)
        Age = st.number_input("Age", 0, 90)

    # Kullanıcının girdiği değerleri birleştirme
    result = {
        'Pregnancies': Pregnancies,
        'Glucose': Glucose,
        'BloodPressure': BloodPressure,
        'SkinThickness': SkinThickness,
        'Insulin': Insulin,
        'BMI': BMI,
        'DiabetesPedigreeFunction': DiabetesPedigreeFunction,
        'Age': Age
    }

    st.write("Your Selected Options:", result)

    # Modelin beklediği formatta giriş oluşturma
    single_sample = np.array(list(result.values())).reshape(1, -1)

    # Tahmin ve olasılık hesaplama
    with st.expander("Prediction Results"):
        prediction = loaded_model.predict(single_sample)
        pred_prob = loaded_model.predict_proba(single_sample)

        st.write(f"Prediction: {prediction[0]}")

        if prediction[0] == 1:
            st.warning("Positive Risk Detected")
            pred_probability_score = {
                "Negative DM": pred_prob[0][0] * 100,
                "Positive DM": pred_prob[0][1] * 100
            }
        else:
            st.success("Negative Risk Detected")
            pred_probability_score = {
                "Negative DM": pred_prob[0][0] * 100,
                "Positive DM": pred_prob[0][1] * 100
            }

        st.subheader("Prediction Probability Score")
        st.json(pred_probability_score)
