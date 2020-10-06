import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import stats
 
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

vissual3 = sns.pairplot(BV, vars=['F_25_34','M_25_34'])
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

vissual3 = sns.pairplot(SB, vars=['F_25_34','M_25_34'])
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

vissual3 = sns.pairplot(CJ, vars=['F_25_34','M_25_34'])
plt.show()


#---------------------------------

#charts for Constanta 

CT=df[df.County=='CT']
print(SB)

sns.distplot(CT["Voters"])
plt.show()

vissual1= sns.lmplot(data=CT, x='Voters', y='F_25_34',
                 fit_reg=False)
plt.show()

vissual2 = sns.lmplot(data=CT, x='Voters', y='M_25_34',
                 fit_reg=False)
plt.show()

vissual3 = sns.pairplot(CT, vars=['F_25_34','M_25_34'])
plt.show()













































