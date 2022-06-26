# one-way anova
import scipy.stats as stats
import pandas as pd

from statsmodels.stats.multicomp import pairwise_tukeyhsd
df1 = pd.read_excel('Abalone.xlsx')

H = []
M = []
L = []

for i in range(len(df1['Rings'])):
    if df1['Rings'][i] == "H":
        H.append(df1['Whole_weight'][i])
    elif df1['Rings'][i] == "M":
        M.append(df1['Whole_weight'][i])
    else:
        L.append(df1['Whole_weight'][i])

lev = stats.levene(H, M, L)
print('levene test', lev)

if lev[1] > 0.05:
    print('變異數同值')
    ano1 = stats.f_oneway(H, M, L)
    print(ano1)
    if ano1[1] <= 0.05:
        print('事後比較')
        df2 = df1['Rings']
        # print(df2)
        mst = df1['Whole_weight']
        tukey = pairwise_tukeyhsd(endog=mst, groups=df2, alpha=0.05)
        print(tukey.summary())
else:
    krs = stats.kruskal(H, M, L)
    print('變異數異值')
    print(krs)
