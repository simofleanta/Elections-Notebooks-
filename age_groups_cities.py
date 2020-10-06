
import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt



age=pd.read_csv('KasFebAge.csv')
print(age)
df=DataFrame(age)


sns.violinplot(x=df["City"], y=df["30_34"], palette="Blues")
plt.show()






