from scipy.stats import chisquare
import pandas as pd

df1 = pd.read_excel('Language.xlsx')
anscount = df1['人數']
print(chisquare(anscount))
