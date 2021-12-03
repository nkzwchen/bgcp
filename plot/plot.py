import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
df =  pd.read_csv(".result.txt",sep = '\t',header = None, names=['cmbd', 'kpi','min', 'q1', 'q2', 'q3', 'max', 'avg'])
name = ['gjjap02','system.cpu.pct_usage']
d = df[(df.cmbd == name[0]) & (df.kpi == name[1])].values.tolist()[0]
d1 = d[2:-1]
d2 = d[2:]
sns.boxplot(data=d2).get_figure().savefig(name[0] + '-' + name[1] + '-boxplot.png', dpi = 500)
data_plot = pd.DataFrame({"X":[1,1,1,1,1,1],"Value":d2, "Types":['min', 'q1', 'q2', 'q3', 'max', 'avg']})
sns.scatterplot(x="X", y="Value",hue="Types", data=data_plot,palette="deep",s = 150).get_figure().savefig(name[0] + '-' + name[1] + '-scatterplot.png', dpi = 500)
