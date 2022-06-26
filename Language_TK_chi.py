from scipy.stats import chisquare
import pandas as pd

df1 = pd.read_excel('people_languge.xlsx')
Oi = df1['Oi'].values[0:5]
Ei = df1['Ei'].values[0:5]
#print(Oi, Ei)
print(chisquare(Oi, Ei))
