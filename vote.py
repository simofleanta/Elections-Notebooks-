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
 #CHARTS

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

vissual4= sns.lmplot(data=BV, x='Voters', y='F_35_44',
                 fit_reg=False)
plt.show()

vissual5= sns.lmplot(data=BV, x='Voters', y='M_35_44',
                 fit_reg=False)
plt.show()


vissual3 = sns.pairplot(BV, vars=['F_25_34','M_25_34'])
plt.show()

vissual7 = sns.pairplot(BV, vars=['F_35_44','F_67'])
plt.show()

vissual8 = sns.pairplot(BV, vars=['M_35_44','M_67'])
plt.show()

plt.figure(figsize=(10,6))
sns.heatmap(BV.corr(),cmap='Blues')
plt.show()
#------------------------------------------------------------------
"""Sibiu"""

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

plt.figure(figsize=(10,6))
sns.heatmap(SB.corr(),cmap='Blues')
plt.show()


#--------------------------------------------------------------
"""Cluj"""

#charts for Cluj 

CJ=df[df.County=='CJ']
print(CJ)

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

plt.figure(figsize=(10,6))
sns.heatmap(CJ.corr(),cmap='Blues')
plt.show()

#---------------------------------
"""cONSTANTA"""

#charts for Constanta 

CT=df[df.County=='CT']
print(CT) 


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

plt.figure(figsize=(10,6))
sns.heatmap(CT.corr(),cmap='Blues')
plt.show()

#---------------------------------------------------------------

"""Timisoara"""

#TIMISOARA :)

TM=df[df.County=='TM']
print(TM) 

TM=df[df.County=='TM']
print(TM) 

#scatterdot
vissual2 = sns.lmplot(data=TM, x='Voters', y='M_25_34',
                 fit_reg=False)
plt.show()
#pairplot
pairplot = sns.pairplot(TM, vars=['F_25_34','M_25_34'])
plt.show()

#heatmap
plt.figure(figsize=(10,5))
sns.heatmap(TM.corr(),cmap='Blues')
plt.show()

#----------------------------------------------------------------------------------

"""BASIC Stats"""

vote=pd.read_csv('population.csv')
print(vote.columns)
df=DataFrame(vote)


"""Find the average per county """
#groupby county
voters=df.groupby('County')
print(voters.get_group('TM'))

#total per county
total_per_county=df['County'].value_counts()
print(total_per_county)

#highest number of voters are in the below counties
voters=df.groupby('County')
votersdf = voters['County','Voters'].max()
print(votersdf)

#mean per county
voters=df.groupby('County')
votersdf = voters['County','Voters'].mean()
print(votersdf)

#the lowest presence in the counties below
voters=df.groupby('County')
votersdf = voters['County','Voters'].min()
print(votersdf)


#the lowest presence in the counties below
voters=df.groupby('County')
votersdf = voters['County','Voters'].median()
print(votersdf)

















 

















































