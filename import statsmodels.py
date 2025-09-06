import statsmodels.api as sm

# Load either pickle
inf_results = sm.load("outputs/inflation_model.pkl")
print(inf_results.summary())

g_results = sm.load("outputs/growth_model.pkl")
print(g_results.summary())