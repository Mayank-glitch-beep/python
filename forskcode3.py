"""
Dataset: titanic.csv
Problem Statement:
      
It’s a real-world data containing the details of 
titanic ships passengers list.
Import the  dataset "titanic.csv"
Answer the Following:
How many people survived the disaster ?
How many people died ?
Calculate the survival rates as proportions (percentage)
Males that survived vs males that passed away
Females that survived vs Females that passed away      
Does age play a role in the survival?
Since it's probable that children were saved first.

"""

import pandas as pd
df=pd.read_csv("titanic.csv")
#peoplesurvived
peop_surv=len(df[df['Survived']==1])

#peopledied
peop_died=len(df[df['Survived']==0])

#survivalrate
surv_rate=peop_surv/(peop_surv+peop_died)*100

#deathrate
death_rate=peop_died/(peop_surv+peop_died)*100

df['Age']=df['Age'].fillna(df['Age'].mean())
df1=df[(df['Survived']==1) & (df['Age']>18) & (df['Sex']=='male')]
df2=df[(df['Survived']==0) & (df['Age']>18) & (df['Sex']=='male')]
male_surv=len(df1)
male_died=len(df2)
tot_male=male_surv+male_died
male_per=(male_surv/tot_male)*100
maledied_per=100-male_per
df3=df[(df['Survived']==1) & (df['Age']>18) & (df['Sex']=='female')]
df4=df[(df['Survived']==0) & (df['Age']>18) & (df['Sex']=='female')]
female_surv=len(df3)
female_died=len(df4)
tot_fem=female_surv+female_died
fem_per=(female_surv/tot_fem)*100
femdied_per=100-fem_per
df5=df[(df['Survived']==1) & (df['Age']<18)]
df6=df[(df['Survived']==0) & (df['Age']<18)]
child_surv=len(df5)
child_died=len(df6)
total_child=child_surv+child_died
child_per=(child_surv/total_child)*100
print(peop_surv,"People survived")
print(peop_died,"People died")
print(surv_rate,"People survived")
print(death_rate,"People died")
print("male survived:",round(male_per,2))
print("male passed away:",maledied_per)
print("female survived:",fem_per)
print("female passed away:",femdied_per)
print("Child survived:",child_per)










 



