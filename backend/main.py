import numpy as np
import joblib
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
app = FastAPI()
app.add_middleware(
   CORSMiddleware,
   allow_origins=["*"],
   allow_methods=["POST"],
   allow_headers=["*"],
)
modelo = joblib.load("Project_credit/modelo_credito.pkl")

class DadosCredito(BaseModel):
   person_age: float
   person_income: float
   person_emp_length: float
   loan_amnt: float
   loan_int_rate: float
   loan_percent_income: float
   cb_person_cred_hist_length: float
   cb_person_default_on_file: int

def calcular_risco(proba: float) -> float:
   return round(proba * 100, 2)

def converter_grade(risco: float) -> str:
   if risco < 3:
       return "A"
   elif risco < 6:
       return "B"
   elif risco < 12:
       return "C"
   elif risco < 25:
       return "D"
   elif risco < 50:
       return "E"
   elif risco < 75:
       return "F"
   else:
       return "G"

@app.post("/predict")
def predict(dados: DadosCredito):
   try:
       features = np.array([[
           dados.person_age,
           dados.person_income,
           dados.person_emp_length,
           dados.loan_amnt,
           dados.loan_int_rate,
           dados.loan_percent_income,
           dados.cb_person_cred_hist_length,
           dados.cb_person_default_on_file,
       ]])
       proba = modelo.predict_proba(features)[0][1]
       risco = calcular_risco(proba)
       loan_grade = converter_grade(risco)
       return {"risco": risco, "loan_grade": loan_grade}
   except Exception as e:
       raise HTTPException(status_code=500, detail=str(e))

# rodar o comando uvicorn main:app --reload para iniciar o servidor