
# 💳 Sprint Engenharia de Dados – Risco de Crédito

## 📌 Visão Geral

Este projeto implementa um **pipeline de Engenharia de Dados para Análise de Risco de Crédito**, integrando **dados de empréstimos** com **indicadores macroeconômicos brasileiros**, especificamente:

- 📈 IPCA (Inflação)
- 💰 SELIC (Taxa de Juros Média Mensal)

O resultado é uma **base de dados integrada, limpa e padronizada**, pronta para análises, BI e aplicações de Machine Learning.

## 🗂️ Estrutura do Projeto

PROJETO-CRED-DATAENGINEEREL
├── README.md ✅
├── Untitled.ipynb
│
├── data/
│   ├── processed/
│   │   └── credit_risk_integrado_v1.csv
│   │
│   └── credit_risk.db
│
├── docs/
│   └── data_dictionary_credito_integrado.csv ✅
│
└── Project_Credit/
    ├── Credit/
    │   └── credit_risk_dataset.csv
    ├── Ipca/
    │   ├── ipca_2024_2026_tratado.csv
    │   └── ipca_202602SerieHist.xls
    └── Selic/
        └── bcdata.sgs.11.csv

## 🔧 Tecnologias Utilizadas

- Python 3.11  
- Pandas e NumPy  
- SQLite  
- CSV / Excel (.xls)  
- Jupyter Notebook  
- VS Code  

## 🔄 Pipeline de Dados

1. **Extração**
   - Base de dados de crédito
   - IPCA
   - Taxas diárias da SELIC

2. **Transformação**
   - Limpeza e padronização
   - Ajuste temporal por ano e mês
   - Cálculo da SELIC média mensal
   - Validação de dados

3. **Carga**
   - Exportação para CSV analítico
   - Persistência em banco SQLite

## 📊 Base Final

- **Registros:** 32.581  
- **Colunas:** 27  
- **Granularidade:** crédito enriquecido com dados macroeconômicos mensais  

Aplicações:
- Criação de ML's
- Previsão de inadimplência
- Análise de risco de crédito
- Credit Scoring
- Dashboards analíticos

## 📘 Dicionário de Dados

O dicionário de dados com a descrição completa das colunas está disponível em:

📎 `docs/data_dictionary_credito_integrado.csv`

## ✅ Entregáveis

- ✅ Base integrada em CSV
- ✅ Banco de dados SQLite
- ✅ Dicionário de dados documentado

## 👤 Autor

### Engenharia de Dados

**Ana Cristina** |
**Elielton Santos** 

## 📜 Licença

Projeto de uso educacional e analítico.  
Dados macroeconômicos provenientes do IBGE e do Banco Central do Brasil.