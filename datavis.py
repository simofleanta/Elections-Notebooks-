import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt

v=pd.read_csv('Kasbv.csv')
print(v)
df=DataFrame(v)

pairplot=sns.pairplot(df, vars=['Year','Pibmilioane'])
plt.show()






