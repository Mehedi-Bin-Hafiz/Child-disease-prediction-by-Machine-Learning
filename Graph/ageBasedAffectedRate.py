

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

########### vvi code for paper#########
plt.rcParams["font.family"] = "Times New Roman"
# plt.rcParams["figure.figsize"] = [9,5]
plt.rcParams.update({'font.size': 10})
########### vvi code for paper#########
mainDataset = pd.read_excel(r'../database/MainDataset.xlsx')

Disease = mainDataset.iloc[ : , -1].values #dependent variables




print('########### age vs affected disease ###########')

age0_disease0 = mainDataset.loc[ (mainDataset['AffectedAge']==0) & (mainDataset['DiseaseName'] == 0)]
age0_disease0 = len(age0_disease0)
age0_disease1 = mainDataset.loc[ (mainDataset['AffectedAge']==0) & (mainDataset['DiseaseName'] == 1)]
age0_disease1 = len(age0_disease1)
age0_disease2 = mainDataset.loc[ (mainDataset['AffectedAge']==0) & (mainDataset['DiseaseName'] == 2)]
age0_disease2 = len(age0_disease2)

age1_disease0= mainDataset.loc[ (mainDataset['AffectedAge']==1) & (mainDataset['DiseaseName'] == 0)] #() is vvi think
age1_disease0 = len(age1_disease0)
age1_disease1= mainDataset.loc[ (mainDataset['AffectedAge']==1) & (mainDataset['DiseaseName'] == 1)] #() is vvi think
age1_disease1 = len(age1_disease1)
age1_disease2 = mainDataset.loc[ (mainDataset['AffectedAge']==1) & (mainDataset['DiseaseName'] == 2)]
age1_disease2 = len(age1_disease2)


age2_disease0 = mainDataset.loc[ (mainDataset['AffectedAge']==2) & (mainDataset['DiseaseName'] == 0)]
age2_disease0 = len(age2_disease0)
age2_disease1 = mainDataset.loc[ (mainDataset['AffectedAge']==2) & (mainDataset['DiseaseName'] == 1)]
age2_disease1 = len(age2_disease1)
age2_disease2 = mainDataset.loc[ (mainDataset['AffectedAge']==2) & (mainDataset['DiseaseName'] == 2)]
age2_disease2 = len(age2_disease2)




age0 = [age0_disease0,age0_disease1, age0_disease2]
age1 = [age1_disease0,age1_disease1, age1_disease2]
age2 = [age2_disease0,age2_disease1, age2_disease2]





# Create the pandas DataFrame
index = ['Chicken Pox', 'Malaria', 'Diarrhea']
df = pd.DataFrame({'0-3': age0,
                   '4-6': age1,
                   '6-9':age2,}, index=index)
df.plot.bar(rot=0)
plt.ylabel('Numbers')
plt.xlabel('Diseases')
plt.savefig('disease vs age.png')
plt.show()














