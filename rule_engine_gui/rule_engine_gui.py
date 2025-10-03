import streamlit as st
from PIL import Image
import os
import time

st.markdown("""
    <style>
    .centered-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

symptoms = {
  'fever': 'images/fever.png',
    'facial_pain': 'images/facial_pain.png',
    'purulent_nasal_discharge': 'images/purulent_nasal_discharge.png',
    'recent_infection': 'images/recent_infection.png',
    'symptoms_more_than_12_weeks': 'images/symptoms_more_than_12_weeks.png',
    'nasal_obstruction': 'images/nasal_obstruction.png',
    'facial_pressure': 'images/facial_pressure.png',
    'sneezing': 'images/sneezing.png',
    'nasal_itching': 'images/nasal_itching.png',
    'watery_rhinorrhea': 'images/watery_rhinorrhea.png',
    'allergen_exposure': 'images/allergen_exposure.png',
    'nasal_congestion': 'images/nasal_congestion.png',
    'visible_deviation': 'images/visible_deviation.png',
    'chronic_nasal_obstruction': 'images/chronic_nasal_obstruction.png',
    'history_of_trauma': 'images/history_of_trauma.png',
    'unilateral_nasal_obstruction': 'images/unilateral_nasal_obstruction.png'
}

friendly_labels = {
    key: key.replace("_", " ").title()
    for key in symptoms
}

def rule_acute_sinusitis(sym):
    if {'recent_onset', 'fever', 'facial_pain', 'purulent_nasal_discharge'}.issubset(sym):
        return "Acute Sinusitis"
    if {'recent_infection', 'facial_pain', 'purulent_nasal_discharge'}.issubset(sym):
        return "Acute Sinusitis"
    return None

def rule_chronic_sinusitis(sym):
    if {'symptoms_more_than_12_weeks', 'nasal_obstruction', 'facial_pressure'}.issubset(sym):
        return "Chronic Sinusitis"
    return None

def rule_rhinitis_allergic(sym):
    if {'sneezing', 'nasal_itching', 'watery_rhinorrhea', 'allergen_exposure'}.issubset(sym):
        return "Allergic Rhinitis"
    return None

def rule_rhinitis_non_allergic(sym):
    if {'watery_rhinorrhea', 'nasal_congestion'}.issubset(sym) and 'allergen_exposure' not in sym:
        return "Non-Allergic Rhinitis"
    return None

def rule_deviated_septum(sym):
    if {'visible_deviation', 'chronic_nasal_obstruction'}.issubset(sym) or \
       {'history_of_trauma', 'unilateral_nasal_obstruction'}.issubset(sym):
        return "Deviated Nasal Septum"
    return None

RULES = [
    rule_acute_sinusitis,
    rule_chronic_sinusitis,
    rule_rhinitis_allergic,
    rule_rhinitis_non_allergic,
    rule_deviated_septum
]

st.set_page_config(page_title="🩺 ENT Symptom Diagnosis", layout="centered")

st.markdown("<h1 style='text-align: center;'>🩺 ENT Symptom Diagnosis</h1>", unsafe_allow_html=True)

if "index" not in st.session_state:
    st.session_state.index = 0
if "selected_symptoms" not in st.session_state:
    st.session_state.selected_symptoms = set()
if "finished" not in st.session_state:
    st.session_state.finished = False
    def show_image_with_transition(img_path, caption):
        img = Image.open(img_path).resize((300, 300))
        img_placeholder = st.empty()
        for opacity in range(0, 11):
            img_placeholder.image(img, caption=caption)
            time.sleep(0.03)
        return img_placeholder

symptom_keys = list(symptoms.keys())

def restart():
    st.session_state.index = 0
    st.session_state.selected_symptoms = set()
    st.session_state.finished = False

if not st.session_state.finished:
    idx = st.session_state.index
    if idx < len(symptom_keys):
        key = symptom_keys[idx]
        label_text = friendly_labels[key]
        img_path = os.path.join(os.path.dirname(__file__), symptoms[key])
        col_img, col_spacer, col_img2 = st.columns([1, 2, 1])
        with col_spacer:
            if os.path.exists(img_path):
                img = Image.open(img_path).resize((300, 300))
                st.image(img, caption=label_text)
            else:
                st.warning(f"Image not found: {img_path}")
            st.markdown(f"<h3 style='text-align: center;'>{label_text}</h3>", unsafe_allow_html=True)
            col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
            with col_btn2:
                if st.button("✅ Yes", key=f"yes_{idx}"):
                    st.session_state.selected_symptoms.add(key)
                    st.session_state.index += 1
                    st.rerun()
                if st.button("❌ No", key=f"no_{idx}"):
                    st.session_state.index += 1
                    st.rerun()
    else:
        st.session_state.finished = True
        st.rerun()
else:
    st.markdown("<h2 style='text-align: center;'>✔️ Review Complete</h2>", unsafe_allow_html=True)
    st.button("🔁 Restart", on_click=restart)
    selected = st.session_state.selected_symptoms
    if not selected:
        st.success("😊 You don’t seem to show any signs of these ENT conditions. Stay healthy!")
    else:
        st.markdown("### 🩺 Symptoms You Selected:")
        for s in selected:
            st.write(f"- {friendly_labels[s]}")
        diagnoses = []
        for rule in RULES:
            d = rule(selected)
            if d and d not in diagnoses:
                diagnoses.append(d)
        if diagnoses:
            st.markdown("### 🔍 Possible Diagnosis:")
            for d in diagnoses:
                st.write(f"- {d}")
        else:
            st.info("❓ No specific ENT condition matched your symptoms.")
