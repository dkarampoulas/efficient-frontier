import numpy as np
from scipy.optimize import minimize

# ==========================================
# STEP 1: THE DATA (R)
# 98 years of real annual returns (Example structure)
# Columns: Stocks, Bonds, Gold
# ==========================================

np.random.seed(42)
R = np.random.randn(98, 3) * 0.1 + np.array([0.119, 0.048, 0.074])

# ==========================================
# STEP 2: EXPECTED RETURN (μ)
# ==========================================
mu = np.mean(R, axis=0)  # Average yearly return per asset

# ==========================================
# STEP 3: COVARIANCE MATRIX (C)
# ==========================================
C = np.cov(R, rowvar=False)  # Covariance matrix

# ==========================================
# STEP 4: PORTFOLIO RISK FUNCTION (σ)
# Risk = sqrt(W^T * C * W)
# ==========================================
def risk(w):
    return np.sqrt(w.T @ C @ w)

def ret(w):
    return w.T @ mu

# ==========================================
# STEP 5: OPTIMIZATION (Efficient Frontier)
# ==========================================
n_assets = len(mu)
# Budget constraint: weights sum to 1, no short selling (0 <= w <= 1)
budget = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}
bounds = tuple((0, 1) for _ in range(n_assets))

# Generate target returns to map the frontier
frontier = []
for target in np.linspace(mu.min(), mu.max(), 40):
    # Constraint: portfolio return hits the target
    target_hit = {'type': 'eq', 'fun': lambda w, t=target: ret(w) - t}
    
    # Minimize portfolio risk for the target return
    w0 = np.ones(n_assets) / n_assets
    res = minimize(risk, w0, bounds=bounds, constraints=[budget, target_hit])
    
    if res.success:
        frontier.append((risk(res.x), ret(res.x)))

frontier = np.array(frontier)
print("Optimization completed successfully! Total optimal portfolios found:", len(frontier))