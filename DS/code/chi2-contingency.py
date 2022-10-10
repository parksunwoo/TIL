import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

obs = np.array([[4,16,20], [23, 18, 19]])
chi2_contingency(obs)

n = 20  # Number of samples.
d = 3  # Dimensionality.
c = 2  # Number of categories.
data = np.random.randint(c, size=(n, d))
data = pd.DataFrame(data, columns=['CAT1', 'CAT2', 'CAT3'])

print(data)

chi2_contingency(data['CAT1'], data['CAT2'])
# Contingency table.
contingency = pd.crosstab(data['CAT1'], data['CAT2'])

# Chi-square test of independence.
c, p, dof, expected = chi2_contingency(contingency)
chi2_contingency(contingency)
