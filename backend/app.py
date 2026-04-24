import joblib
import numpy as np
import streamlit as st
import os

modelo = joblib.load(os.path.join(os.path.dirname(__file__), "Project_Credit/modelo_credito.pkl"))

st.set_page_config(page_title="Análise de Crédito", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500&family=DM+Mono:wght@400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #0f0f11;
    color: #e2e2e8;
}
h1, h2, h3 { font-family: 'DM Sans', sans-serif; font-weight: 500; color: #ffffff; }

div[data-baseweb="input"] input {
    background-color: #141414 !important;
    border: 1px solid #141414 !important;
    color: #e2e2e8 !important;
    font-family: 'DM Mono', monospace !important;
    border-radius: 6px !important;
}

div[data-baseweb="select"] * {
    font-family: 'DM Mono', monospace !important;
    text-decoration: none !important;
    border: none !important;
    outline: none !important;
    box-shadow: none !important;
}

div[data-baseweb="select"] > div {
    background-color: #141414 !important;
    border: 1px solid #2e2e4a !important;
    border-radius: 6px !important;
}

div[data-baseweb="menu"] {
    background-color: #141414 !important;
    border: 1px solid #2e2e4a !important;
}

div[data-baseweb="option"] {
    background-color: #141414 !important;
    color: #e2e2e8 !important;
    font-family: 'DM Mono', monospace !important;
    text-decoration: none !important;
}

div[data-baseweb="option"]:hover {
    background-color: #2e2e4a !important;
}

label, .stNumberInput label, .stSelectbox label {
    font-family: 'DM Mono', monospace !important;
    font-size: 12px !important;
    letter-spacing: 0.04em !important;
}

div.stButton > button {
    background-color: #FFE600 !important;
    color: black !important;
    border: none !important;
    border-radius: 6px !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 13px !important;
    font-weight: 700 !important;
    letter-spacing: 0.06em !important;
    padding: 12px !important;
    width: 100% !important;
}

div.stButton > button:hover { opacity: 0.88 !important; }

hr { border-color: #2e2e4a !important; }

div[data-testid="metric-container"] {
    background-color: #141414;
    border: 1px solid #2e2e4a;
    border-radius: 8px;
    padding: 18px 20px;
}

div[data-testid="metric-container"] label {
    font-family: 'DM Mono', monospace !important;
    font-size: 10px !important;
}
            
button[kind="stepDown"], button[kind="stepUp"] {
    color: #141414 !important;
    background-color: #141414 !important; 
    border: none !important;
}

</style>
""", unsafe_allow_html=True)

GRADE_COLORS = {
    "A": "#00b894", "B": "#55efc4", "C": "#fdcb6e",
    "D": "#e17055", "E": "#d35400", "F": "#c0392b", "G": "#d81e0d",
}

def converter_grade(risco):
    if risco < 5:    return "A"
    elif risco < 15: return "B"
    elif risco < 30: return "C"
    elif risco < 45: return "D"
    elif risco < 60: return "E"
    elif risco < 75: return "F"
    else:            return "G"

st.markdown("<div style='font-family:DM Mono,monospace;font-weight:500;font-size:13px;letter-spacing:0.15em;color:#FFE600;text-transform:uppercase;margin-bottom:8px'>Credit Risk</div>", unsafe_allow_html=True)
st.header("Análise de Probabilidade de Inadimplência")
st.markdown("---")

st.subheader("Perfil do Solicitante")

col1, col2 = st.columns(2)
with col1:
    person_age    = st.number_input("Idade", min_value=18, max_value=80, value=35)
    person_income = st.number_input("Renda Anual (R$)", min_value=0, value=60000)
with col2:
    person_emp_length          = st.number_input("Tempo de Emprego (anos)", min_value=0, value=5)
    cb_person_cred_hist_length = st.number_input("Histórico de Crédito (anos)", min_value=0, value=8)

cb_person_default_on_file = st.selectbox(
    "Registro de dívida em aberto?",
    options=[0, 1],
    format_func=lambda x: "Não possui" if x == 0 else "Possui"
)

st.markdown("---")
st.subheader("Características do Empréstimo")

col3, col4 = st.columns(2)
with col3:
    loan_amnt     = st.number_input("Valor solicitado (R$)", min_value=0, value=15000)
with col4:
    loan_int_rate = st.number_input("Taxa de Juros (%)", min_value=0.0, value=12.5, step=0.1)

loan_percent_income = st.number_input("Comprometimento de renda (%)", min_value=0.0, value=25.0)

st.markdown("---")

if st.button("Calcular risco", use_container_width=True):
    features = np.array([[
        float(person_age),
        float(person_income),
        float(person_emp_length),
        float(loan_amnt),
        float(loan_int_rate),
        float(loan_percent_income) / 100,
        float(cb_person_cred_hist_length),
        float(cb_person_default_on_file),
    ]])

    proba = modelo.predict_proba(features)[0][1]
    risco = round(proba * 100, 2)
    grade = converter_grade(risco)
    cor   = GRADE_COLORS[grade]

    col_r, col_g = st.columns(2)

    with col_r:
        st.markdown(f"""
        <div style="padding: 18px 0;">
            <div style="font-family:'DM Mono',monospace;font-weight:550;font-size:12px;letter-spacing:0.14em;color:#888888;text-transform:uppercase;margin-bottom:10px;">
                Risco de Inadimplência (%)
            </div>
            <div style="font-family:'DM Mono',monospace;font-size:30px;font-weight:500;">
                {risco}%
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_g:
        st.markdown(f"""
        <div style="padding: 18px 0;">
            <div style="font-family:'DM Mono',monospace;font-weight:550;font-size:12px;letter-spacing:0.14em;color:#888888;text-transform:uppercase;margin-bottom:10px;">
                Classificação do Empréstimo
            </div>
            <div style="font-family:'DM Mono',monospace;font-size:30px;font-weight:500;color:{cor};">
                {grade}
            </div>
        </div>
        """, unsafe_allow_html=True)