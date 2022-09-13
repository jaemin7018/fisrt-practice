import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

date_1 = pd.read_excel("D:/Downloads/9월12일.xlsx")
df2 = pd.DataFrame(date_1)
All = df2.loc[df2["Data Type"]== "Arrival"]
NaN = len(All.loc[All["AI Suggested Accuracy"] == -1])
K = len(All.loc[All["AI Suggested Locator"]== 'EE'])
Y = len(All.loc[All["AI Suggested Accuracy"] == 'Y'])
N = len(All.loc[All["AI Suggested Accuracy"] == 'N'])
ratio = [NaN, Y, N ]
labels = ['-1', 'Y', 'N']
explode = [0.05, 0.05, 0.05]
def make_autopct(ratio):
    def my_autopct(pct):
        total = sum(ratio)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct

plt.title("(9/12)")
plt.pie(ratio, labels=labels, autopct=make_autopct(ratio),
       explode = explode, shadow=True)
plt.show()
