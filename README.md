# Risco de Crédito — Engenharia de Dados & Machine Learning

## Visão Geral

Este projeto implementa um **pipeline completo de Engenharia de Dados e Machine Learning para Análise de Risco de Crédito**, integrando dados de empréstimos com indicadores macroeconômicos brasileiros — **IPCA** e **SELIC** — para gerar uma base enriquecida e treinar um modelo preditivo de inadimplência.

O projeto cobre desde a extração e tratamento dos dados até a disponibilização do modelo via API REST e interface web para simulação.

---

## Estrutura do Projeto

```
Projeto-cred/
├── README.md
├── requirements.txt
│
├── backend/
│   ├── data/
│   │   ├── processed/
│   │   │   └── credit_risk_integrado_v1.csv
│   │   └── credit_risk.db
│   ├── docs/
│   │   └── data_dictionary_credito_integrado.csv
│   ├── Project_Credit/
│   │   ├── Credit/
│   │   │   └── credit_risk_dataset.csv
│   │   ├── Ipca/
│   │   │   ├── ipca_2024_2026_tratado.csv
│   │   │   └── ipca_202602SerieHist.xls
│   │   ├── Selic/
│   │   │   └── bcdata.sgs.11.csv
│   │   ├── gradient_boost.ipynb
│   │   └── modelo_credito.pkl
│   ├── testes/
│   │   ├── decision_tree.ipynb
│   │   ├── insights_estrategicos.ipynb
│   │   ├── logistic_regression.ipynb
│   │   └── random_forest.ipynb
│   ├── cien_dados.ipynb
│   ├── concessao_cred.ipynb
│   ├── eng_dados.ipynb
│   └── main.py
│
└── frontend/
    └── index.html
```

---

## Tecnologias Utilizadas

- Python 3.11
- Pandas e NumPy
- Scikit-learn
- SQLite
- CSV / Excel (.xls)
- Jupyter Notebook
- FastAPI + Uvicorn
- HTML / CSS / JavaScript
- VS Code

---

## Pipeline de Dados

1. **Extração** — base de crédito, séries históricas de IPCA e SELIC
2. **Transformação** — limpeza, padronização, ajuste temporal por mês/ano, cálculo da SELIC média mensal e validação
3. **Carga** — exportação para CSV analítico e persistência em banco SQLite

---

## Base Final

- **Registros:** 32.581
- **Colunas:** 27
- **Granularidade:** crédito enriquecido com dados macroeconômicos mensais
- **Taxa de inadimplência na base:** 21.8%

---

## Análise Exploratória — Principais Insights

A análise exploratória (`insights_estrategicos.ipynb`) identificou os principais fatores de risco:

**Loan Grade** é o preditor com maior poder discriminativo. A taxa de inadimplência cresce progressivamente de 10% no grade A até 98.4% no grade G.

**Comprometimento de renda** funciona como gatilho de alarme. Abaixo de 30% a inadimplência se mantém abaixo de 22%. Acima de 30% ela explode para 70-79%.

**Renda** atua como fator protetor. Clientes com renda abaixo de R$30k inadimplem em 45.5%, enquanto faixas acima de R$100k ficam abaixo de 13%.

**Taxa de juros** tem correlação de 0.33 com default — a segunda maior da base. Empréstimos com juros acima de 16% chegam a 62.9% de inadimplência.

**Histórico de default** dobra o risco: clientes com registro anterior inadimplem em 37.8% vs 18.4% dos sem histórico.

**Situação de moradia**: proprietários (OWN) têm taxa de 7.5%, contra 31.6% de quem aluga.

---

## Modelo de Machine Learning

Foram testados quatro algoritmos. O **Gradient Boosting** foi escolhido como modelo final por apresentar a melhor performance.

| Modelo | AUC-ROC CV | AUC-ROC Test | Accuracy |
|---|---|---|---|
| Gradient Boosting | 0.9025 ± 0.0046 | **0.8998** | **87%** |
| Random Forest | — | 0.8814 | 84% |
| Decision Tree | 0.8628 ± 0.0086 | 0.8596 | 85% |
| Logistic Regression | 0.8352 ± 0.0096 | 0.8312 | 76% |

**Importância das features (Gradient Boosting):**

| Feature | Importância |
|---|---|
| `loan_percent_income` | 38.0% |
| `loan_int_rate` | 32.0% |
| `person_income` | 19.9% |
| `person_emp_length` | 5.0% |
| `loan_amnt` | 2.7% |
| `person_age` | 1.3% |
| `cb_person_cred_hist_length` | 0.9% |
| `cb_person_default_on_file` | 0.1% |

O modelo treinado está salvo em `backend/Project_Credit/modelo_credito.pkl`.

---

## API (Backend)

```bash
# dentro da pasta backend/
uvicorn main:app --reload
```

**Endpoint:** `POST /predict`

```json
{
  "person_age": 35,
  "person_income": 60000,
  "person_emp_length": 5,
  "loan_amnt": 15000,
  "loan_int_rate": 12.5,
  "loan_percent_income": 0.25,
  "cb_person_cred_hist_length": 8,
  "cb_person_default_on_file": 0
}
```

**Resposta:**

```json
{
  "risco": 23.45,
  "loan_grade": "C"
}
```

---

## Frontend

Interface web em HTML/CSS/JS puro para testar o modelo. Abrir `frontend/index.html` diretamente no navegador com o backend rodando.

---

## Dicionário de Dados

Disponível em `backend/docs/data_dictionary_credito_integrado.csv`.

---

## Autores

**Engenharia de Dados**
Ana Cristina | Elielton Santos

**Engenharia de Dados & Machine Learning**
Davi Fernandes Coutinho | João Vitor Rodrigues

---

## Licença

Projeto de uso educacional e analítico.
Dados macroeconômicos provenientes do IBGE e do Banco Central do Brasil.
