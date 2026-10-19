### What is the Efficient Frontier?

The lowest-risk portfolio of the last 98 years wasn't all bonds. It mixed in stocks and gold—two assets that swing, or move, differently.

Based on Modern Portfolio Theory, this project demonstrates how combining uncorrelated assets (stocks, bonds, and gold) minimizes portfolio risk while maximizing expected returns through mathematical optimization.

---

### Step 1: The Data R

98 years of real annual returns, one column each for US stocks, ten-year government bonds, and gold.

---

### Step 2: Expected Return $\mu$

$\mu$ is each column's average yearly return:

* **Stocks:** 11.9%


* **Bonds:** 4.8%


* **Gold:** 7.4%



A portfolio earns the weighted average: $W \times \mu$.

---

### Step 3: Covariance C

$C$ is the covariance matrix.

* The diagonal holds each asset's own variance, as volatility: stocks 19.4%, bonds 7.9%, gold 21.5%.


* Off the diagonal, pairs move together. Here, stocks and bonds correlate at just 0.02.



---

### Step 4: Portfolio Risk $\sigma$

Risk isn't a weighted average. It's the square root of $W^T C W$. With two assets, that's each weight squared times its variance plus two times both weights times the covariance.

---

### Step 5: Optimize

Let's find the best mix for every level of risk. For each target return, `minimize` finds the lowest-variance weights with three rules:

1. Weights add up to 1.


2. The return hits the target.


3. No short selling.



40 targets, 40 optimal portfolios, and here's the mix from the start: 14% stocks, 75% bonds, 11% gold, 6.9% risk—below every single asset.

From there up is the efficient frontier: for its risk, nothing earns more. Everything below is inefficient, including all bonds. At the same risk, the frontier earns 7.2% instead of 4.8%.