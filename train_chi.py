from scipy.stats import chisquare
import pandas as pd

df1 = pd.read_excel('train.xlsx')
s = df1['總運量']
print(chisquare(s))
