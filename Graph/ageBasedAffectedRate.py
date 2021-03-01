

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

########### vvi code for paper#########
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["figure.figsize"] = [9,5]
plt.rcParams.update({'font.size': 12})
########### vvi code for paper#########
mainDataset = pd.read_excel(r'../database/MainDataset.xlsx')

Disease = mainDataset.iloc[ : , -1].values #dependent variables




print('########### Miscarriage ###########')

age1_disease1= mainDataset.loc[ (mainDataset['Age']==1) & (mainDataset['Disease'] == 1)] #() is vvi think
age1_disease1 = len(age1_disease1)
age1_disease2 = mainDataset.loc[ (mainDataset['Age']==1) & (mainDataset['Disease'] == 2)]
age1_disease2 = len(age1_disease2)


age2_disease1 = mainDataset.loc[ (mainDataset['Age']==2) & (mainDataset['Disease'] == 1)]
age2_disease1 = len(age2_disease1)
age2_disease2 = mainDataset.loc[ (mainDataset['Age']==2) & (mainDataset['Disease'] == 2)]
age2_disease2 = len(age2_disease2)


age3_disease1 = mainDataset.loc[ (mainDataset['Age']==3) & (mainDataset['Disease'] == 1)]
age3_disease1 = len(age3_disease1)
age3_disease2 = mainDataset.loc[ (mainDataset['Age']==3) & (mainDataset['Disease'] == 2)]
age3_disease2 = len(age3_disease2)



age1 = [age1_disease1,age1_disease2]
age2 = [age2_disease1,age2_disease2]
age3 = [age3_disease1,age3_disease2]




# Create the pandas DataFrame
index = ['Miscarriage', 'Anemia']
df = pd.DataFrame({'14-19': age1,
                   '20-35': age2,
                   '35 up':age3,}, index=index)
df.plot.bar(rot=0)
plt.ylabel('Numbers')
plt.xlabel('Diseases')
plt.savefig('disease vs age.png')
plt.show()














