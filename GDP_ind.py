from scipy import stats
import pandas as pd

df1 = pd.read_excel('GDP.xlsx')
GDP2018 = df1['2018GDP(美元)']
GDP2020 = df1['2020GDP(美元)']
# print(before)

lev = stats.levene(GDP2018, GDP2020, center='mean')
print('lev：', lev)
if lev[1] > 0.05:
    ay6t = stats.ttest_ind(GDP2018, GDP2020)
    print('變異數同質：', ay6t)
else:
    ay6tf = stats.ttest_ind(GDP2018, GDP2020, equal_var=False)
    print('變異數異質：', ay6tf)
