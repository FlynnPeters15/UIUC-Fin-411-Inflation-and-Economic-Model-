# UIUC FIN 411: Inflation and Economic Model

**Recreating an inflation forecasting model originally implemented in Excel, now developed in Python—with added visualizations.**

![Python](https://img.shields.io/badge/Language-Python-blue?logo=python)
![Completed](https://img.shields.io/badge/Status-Completed-brightgreen)
![Final Project](https://img.shields.io/badge/Project-UIUC_FIN_411_Inflation_and_Economic_Model-blue)

---

## Overview

This repository contains a **Python-based recreation** of an inflation and economic forecasting project initially built in Microsoft Excel—performed without using an external data API. The goal is to demonstrate how economic indicators influence inflation trends through linear modeling in Python.

---

## Features & Approach

- **Python Rebuild** of an Excel model for reproducibility and automation  
- **Regression Analysis** on macroeconomic indicators to estimate inflation  
- **Script-first Workflow** for simple execution and inspection of results  
- **Outputs Directory** with model artifacts and figures for quick review

---

## Getting Started

### Prerequisites
- Python 3.x  
- Libraries: `pandas`, `numpy`, `statsmodels`, `matplotlib` (and optionally `scikit-learn`)

### Installation & Usage
```bash
# Clone the repository
git clone https://github.com/FlynnPeters15/UIUC-Fin-411-Inflation-and-Economic-Model-.git
cd UIUC-Fin-411-Inflation-and-Economic-Model-

# (Optional) create & activate a virtual env, then install deps
# python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
# pip install -r requirements.txt

# Run the model
python fred_linear_regression.py

Inflation Model Summary:
- Coefficient on GDP Growth: 0.85 (p < 0.01)
- Coefficient on Unemployment Rate: -0.45 (p < 0.05)
- R-squared: 0.72

Sample Prediction:
- With GDP growth 3.2% and unemployment 5.1% → Predicted inflation: 2.6%

outputs/
  inflation_actual_vs_predicted.png
  inflation_residuals.png
  inflation_qqplot.png
  inflation_corr_heatmap.png
  economic_actual_vs_predicted.png
  economic_residuals.png
  economic_qqplot.png
  economic_corr_heatmap.png

inflation_model.py
economic_model.py
README.md
