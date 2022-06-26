import pandas as pd
import scipy.stats as stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

df1 = pd.read_excel('train.xlsx')
month = df1['月']
s = df1['總運量']

Jan = []
Feb = []
Mar = []
Apr = []
May = []
Jun = []
Jul = []
Aug = []
Sep = []
Oct = []
Nov = []
Dec = []

for i in range(len(df1['月'])):
    if df1['月'][i] == 1:
        Jan.append(df1['總運量'][i])
    elif df1['月'][i] == 2:
        Feb.append(df1['總運量'][i])
    elif df1['月'][i] == 3:
        Mar.append(df1['總運量'][i])
    elif df1['月'][i] == 4:
        Apr.append(df1['總運量'][i])
    elif df1['月'][i] == 5:
        May.append(df1['總運量'][i])
    elif df1['月'][i] == 6:
        Jun.append(df1['總運量'][i])
    elif df1['月'][i] == 7:
        Jul.append(df1['總運量'][i])
    elif df1['月'][i] == 8:
        Aug.append(df1['總運量'][i])
    elif df1['月'][i] == 9:
        Sep.append(df1['總運量'][i])
    elif df1['月'][i] == 10:
        Oct.append(df1['總運量'][i])
    elif df1['月'][i] == 11:
        Nov.append(df1['總運量'][i])
    else:
        Dec.append(df1['總運量'][i])

#print(Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec)
lev = stats.levene(Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec)
print('levene test', lev)

if lev[1] > 0.05:
    print('變異數同值')
    ano1 = stats.f_oneway(Jan, Feb, Mar, Apr, May, Jun,
                          Jul, Aug, Sep, Oct, Nov, Dec)
    print(ano1)
    if ano1[1] <= 0.05:
        print('事後比較')
        df2 = df1['月']
        # print(df2)
        mst = df1['總運量']
        tukey = pairwise_tukeyhsd(endog=mst, groups=df2, alpha=0.05)
        print(tukey.summary())
else:
    krs = stats.kruskal(Jan, Feb, Mar, Apr, May, Jun,
                        Jul, Aug, Sep, Oct, Nov, Dec)
    print('變異數異值')
    print(krs)
