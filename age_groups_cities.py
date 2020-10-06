
import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt



age=pd.read_csv('KasFebAge.csv')
print(age)
df=DataFrame(age)


sns.violinplot(x=df["City"], y=df["30_34"], palette="Blues")
plt.show()
sns.violinplot(x=df["City"], y=df["20_14"], palette="Blues")
plt.show()
sns.violinplot(x=df["City"], y=df["15_19"], palette="Blues")
plt.show()








