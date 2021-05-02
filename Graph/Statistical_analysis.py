import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
########### vvi code for paper#########

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 12})

########### vvi code for paper#########
mainDataset = pd.read_excel(r'../database/MainDataset.xlsx')
# print(mainDataset)

DiseaseName = mainDataset.iloc[ : , -1].values #dependent variables
checkenPox = DiseaseName.tolist().count(0)
Malaria = DiseaseName.tolist().count(1)
Diarrhea = DiseaseName.tolist().count(2)
# sns.heatmap(mainDataset.corr(),annot=True)
# plt.savefig('heatmap.png')
# plt.show()

affected_age = mainDataset.loc[mainDataset['Disease'] == 1, 'AffectedAge']
dict = {0:"0 (0-3 years)", 1:" 1(4-6 years)", 2:"2 (7-9 years)"}
affected_value = affected_age.value_counts().rename(index=dict)
print(affected_value)
print('affected numbers are: ',len(affected_age))
affected_value.plot(kind = 'pie',autopct='%1.1f%%' )
plt.savefig('diseaseYesVsAffectedAge.png')
plt.show()

################# Mother Information ###############
diseased = mainDataset.loc[(mainDataset['Disease']) == 1, 'AgeOfDelivery']
diseased = pd.DataFrame(diseased)
categorizeBasedOnMother = diseased['AgeOfDelivery'].value_counts()
print(categorizeBasedOnMother)
categorizeBasedOnMother.plot.bar(rot=0)
plt.ylabel('Numbers')
plt.xlabel('Delivery age ')
plt.savefig('disease vs Delivery age.png')
plt.show()

diseased = mainDataset.loc[(mainDataset['Disease']) == 1, 'DiseaseDuringPregnancy']
diseased = pd.DataFrame(diseased)
categorizeBasedOnMother = diseased['DiseaseDuringPregnancy'].value_counts()
print(categorizeBasedOnMother)
categorizeBasedOnMother.plot(kind = 'pie',autopct='%1.1f%%' )
plt.ylabel('Numbers')
plt.xlabel('Delivery age ')
plt.savefig('child disease vs disease during mother pregnancy .png')
plt.show()

