# UIUC FIN 411: Inflation and Economic Model

**Recreating inflation and economic forecasting models originally implemented in Excel, now developed in Python—with reproducible outputs, figures, embedded regression tables, and clear variable descriptions.**

![Python](https://img.shields.io/badge/Language-Python-blue?logo=python)
![Completed](https://img.shields.io/badge/Status-Completed-brightgreen)
![Final Project](https://img.shields.io/badge/Project-UIUC_FIN_411_Inflation_and_Economic_Model-blue)

---

## Overview

This repository contains **Python-based recreations** of inflation and macroeconomic forecasting projects originally built in Microsoft Excel—implemented **without external data APIs**. The goal is to show how macroeconomic indicators relate to inflation and other outcomes using **linear regression** and clear, reproducible workflows.

---

## Features & Approach

- **Inflation Model (CPI-based)**: Regresses Consumer Price Index (CPI) on key macroeconomic drivers.  
- **Economic Model (Industrial Production-based)**: Regresses Industrial Production (IP) on structural macro factors.  
- **Script-first**: One-command runs that save model artifacts to `outputs/`  
- **Visualizations & Tables**: Actual vs. Predicted, residual diagnostics, correlation heatmaps, and **raw statsmodels summaries embedded below**

---

## Variables Used

### Inflation Model (CPI)
Dependent Variable:  
- **CPI** – Consumer Price Index, proxy for overall inflation  

Independent Variables:  
- **Wages** – Measures aggregate wage growth, reflecting cost pressures from labor markets  
- **WTI** – West Texas Intermediate crude oil price, proxy for energy costs  
- **M2** – Broad money supply, proxy for liquidity and monetary conditions  
- **T10Y** – 10-year Treasury yield, proxy for long-term interest rates and monetary policy stance  
- **PPI** – Producer Price Index, measures wholesale cost pressures feeding into consumer inflation  

---

### Economic Model (Industrial Production)
Dependent Variable:  
- **IP** – Industrial Production, indicator of real economic activity and output growth  

Independent Variables:  
- **CapUtil** – Capacity Utilization, measures how intensively resources/factories are used  
- **WTI** – West Texas Intermediate crude oil price, proxy for energy input costs  
- **M2** – Broad money supply, indicator of monetary liquidity affecting investment and output  
- **T10Y** – 10-year Treasury yield, proxy for borrowing costs and financial conditions  

---

## Getting Started

### Prerequisites
- Python 3.x  
- Libraries: `pandas`, `numpy`, `statsmodels`, `matplotlib` (optionally `scikit-learn`)

### Installation & Usage
```bash
# Clone the repository
git clone https://github.com/FlynnPeters15/UIUC-Fin-411-Inflation-and-Economic-Model-.git
cd UIUC-Fin-411-Inflation-and-Economic-Model-

# (Optional) create & activate a virtual env, then install deps
# python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
# pip install -r requirements.txt

# Run the inflation model
python inflation_model.py

# Run the economic model
python economic_model.py
