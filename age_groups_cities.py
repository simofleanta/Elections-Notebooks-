
import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt



age=pd.read_csv('KasFebAge.csv')
print(age)
df=DataFrame(age)


#perform violin plots based on city
sns.violinplot(x=df["City"], y=df["30_34"], palette="Blues")
plt.show()
sns.violinplot(x=df["City"], y=df["20_14"], palette="Blues")
plt.show()
sns.violinplot(x=df["City"], y=df["15_19"], palette="Blues")
plt.show()

#extract a city 
Bucharest=df[df.City=='Bucuresti']
print(Bucharest)

#and perform charts on the specific city
Bucharest_vis= sns.lmplot(data=Bucharest, x='15_19', y='20_14',
                 fit_reg=False)
plt.show()

B_vis = sns.pairplot(Bucharest, vars=['Year','20_14'])
plt.show()

Bucx= sns.boxplot(data=Bucharest, x="Year", y="30_34")
plt.show()



















