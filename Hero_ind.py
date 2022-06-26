from scipy import stats
import pandas as pd

df1 = pd.read_excel('hero.xlsx')
win1122 = df1['11.22勝率']
win1123 = df1['11.23勝率']
# print(before)

lev = stats.levene(win1122, win1123, center='mean')
print('lev：', lev)
if lev[1] > 0.05:
    ay6t = stats.ttest_ind(win1122, win1123)
    print('變異數同質：', ay6t)
else:
    ay6tf = stats.ttest_ind(win1122, win1123, equal_var=False)
    print('變異數異質：', ay6tf)
