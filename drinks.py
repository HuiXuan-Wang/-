from scipy import stats
import pandas as pd

df1 = pd.read_excel('drinks.xlsx')
winterCup = df1['wintercup']
summerCup = df1['summercup']

lev = stats.levene(summerCup,winterCup,center='mean')
print('lev:',lev)

if lev[1] > 0.05:
    result = "變異數同質:"
    ttest = stats.ttest_ind(summerCup,winterCup)
else:
    result = "變異數異質:"
    ttest = stats.ttest_ind(summerCup,winterCup,equal_var=False)
    
print(result,ttest)