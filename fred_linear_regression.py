
#Re‑creates the CPI and Industrial‑Production regressions with 7‑month leads and
#saves focused correlation heat‑maps plus all artefacts into `outputs/`.

from __future__ import annotations
import ssl, urllib.request
from pathlib import Path
import certifi, pandas as pd, matplotlib.pyplot as plt, seaborn as sns, statsmodels.api as sm
from fredapi import Fred

# SSL workaround
ssl_ctx = ssl.create_default_context(cafile=certifi.where())
urllib.request.install_opener(urllib.request.build_opener(urllib.request.HTTPSHandler(context=ssl_ctx)))

# Config
START_DATE  = "2000-01-01"
LEAD_MONTHS = 7
OUTDIR      = Path("outputs").resolve(); OUTDIR.mkdir(exist_ok=True)
API_KEY     = ""

SERIES = {
    "CPI":"CPIAUCSL","IP":"INDPRO","Wages":"AHETPI","WTI":"DCOILWTICO",
    "M2":"M2SL","T10Y":"DGS10","PPI":"PPIACO","CapUtil":"TCU"
}

fred = Fred(api_key=API_KEY)

#1. Download data
print("Downloading data from FRED …")
raw = pd.DataFrame({n: fred.get_series(c, START_DATE) for n,c in SERIES.items()}).resample("ME").last()
print(f"Fetched {raw.shape[0]:,} rows × {raw.shape[1]} cols")

#2. Correlation heat‑maps
def save_heatmap(cols, filename, title):
    plt.figure(figsize=(6,5))
    sns.heatmap(raw[cols].corr(), annot=True, cmap="vlag", vmin=-1, vmax=1, fmt=".2f")
    plt.title(title); plt.tight_layout()
    path = OUTDIR/filename; plt.savefig(path, dpi=300); plt.close(); print("→", path)
save_heatmap(["CPI","Wages","WTI","M2","T10Y","PPI"], "cpi_corr_heatmap.png", "Inflation variables")
save_heatmap(["IP","CapUtil","WTI","M2","T10Y"],       "ip_corr_heatmap.png",  "Growth variables")
raw.corr().to_csv(OUTDIR/"correlation_matrix.csv")

# 3. Helper: fit model
def build(target, predictors):
    df = pd.concat([raw[target], raw[predictors].shift(-LEAD_MONTHS)], axis=1).dropna()
    model = sm.OLS(df[target], sm.add_constant(df[predictors])).fit()
    df["fitted"] = model.fittedvalues
    return model, df

# Inflation model
infl_X = ["Wages","WTI","M2","T10Y","PPI"]
inf_model, inf_df = build("CPI", infl_X)
(inf_df[["CPI","fitted"]]).plot(title="CPI actual vs fitted")
plt.tight_layout(); plt.savefig(OUTDIR/"cpi_fit.png"); plt.close()
inf_df.to_csv(OUTDIR/"inflation_model_data.csv"); inf_model.save(OUTDIR/"inflation_model.pkl")

# Industrial Production model
g_X = ["CapUtil","WTI","M2","T10Y"]
g_model, g_df = build("IP", g_X)
(g_df[["IP","fitted"]]).plot(title="IP actual vs fitted")
plt.tight_layout(); plt.savefig(OUTDIR/"ip_fit.png"); plt.close()
g_df.to_csv(OUTDIR/"growth_model_data.csv"); g_model.save(OUTDIR/"growth_model.pkl")

print("✓ all artefacts saved to", OUTDIR)
