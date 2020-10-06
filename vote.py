import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
 
#open the file
vote=pd.read_csv('population.csv')
print(vote.columns)
df=DataFrame(vote)

#-----------------------------------------------------------

#charts for BV 
BV=df[df.County=='BV']
print(BV)

sns.distplot(BV["Voters"])
plt.show()

vissual1= sns.lmplot(data=BV, x='Voters', y='F_25_34',
                 fit_reg=False)
plt.show()

vissual2 = sns.lmplot(data=BV, x='Voters', y='M_25_34',
                 fit_reg=False)
plt.show()

#------------------------------------------------------------------

#charts for Sibiu 

SB=df[df.County=='SB']
print(SB)

sns.distplot(SB["Voters"])
plt.show()

vissual1= sns.lmplot(data=SB, x='Voters', y='F_25_34',
                 fit_reg=False)
plt.show()

vissual2 = sns.lmplot(data=SB, x='Voters', y='M_25_34',
                 fit_reg=False)
plt.show()

#--------------------------------------------------------------

#charts for Cluj 

CJ=df[df.County=='CJ']
print(SB)

sns.distplot(CJ["Voters"])
plt.show()

vissual1= sns.lmplot(data=CJ, x='Voters', y='F_25_34',
                 fit_reg=False)
plt.show()

vissual2 = sns.lmplot(data=CJ, x='Voters', y='M_25_34',
                 fit_reg=False)
plt.show()








































