import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
 
#open the file
vote=pd.read_csv('population.csv')
print(vote.columns)
df=DataFrame(vote)

sns.violinplot(x=df["County"], y=df["M_18_24"], palette="Blues")
plt.show()

sns.distplot(df["M_18_24"])
plt.show()

sns.boxplot(data=df, x="County", y="F_45_64")
plt.show()
#-----------------------------------------------------------
BV=df[df.County=='BV']
print(BV)






















