import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt

v=pd.read_csv('Kasbv.csv')
print(v)
df=DataFrame(v)



sns.violinplot(x=df["Products"], y=df["Profit"], palette="Blues")
plt.show()




