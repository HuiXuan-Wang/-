from scipy import stats
import pandas as pd

df1 = pd.read_excel('Abalone.xlsx')
# print(df1)

F = []
M = []
I = []

for i in range(len(df1['Gender'])):
    if df1['Gender'][i] == "F":
        F.append(df1['Whole_weight'][i])
    elif df1['Gender'][i] == "M":
        M.append(df1['Whole_weight'][i])
    else:
        I.append(df1['Whole_weight'][i])

lev = stats.levene(F, M, center='mean')
print('lev：', lev)
if lev[1] > 0.05:
    ay6t = stats.ttest_ind(F, M)
    print('變異數同質：', ay6t)
else:
    ay6tf = stats.ttest_ind(F, M, equal_var=False)
    print('變異數異質：', ay6tf)
