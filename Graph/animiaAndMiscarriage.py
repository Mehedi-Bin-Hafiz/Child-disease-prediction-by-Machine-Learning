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
miscarriage= Disease.tolist().count(1)
totalPositive = Disease.tolist().count(2)
sns.heatmap(mainDataset.corr(),annot=True)
plt.savefig('heatmap.png')
plt.show()

#
# affected_age = mainDataset.loc[mainDataset['Disease'] == 1, 'Ages']
# affected_value = affected_age.value_counts()
# print('affected numbers are: ',len(affected_age))
# affected_value.plot(kind = 'pie',autopct='%1.1f%%' )
# plt.savefig('pie chart.png')
# plt.show()
#
print('########### Miscarriage ###########')

# mis15_19Iron= mainDataset.loc[ (mainDataset['Age']==1) & (mainDataset['Disease'] == 1) , 'Iron Deficiency',] #() is vvi think

misIron=[109,19,69]
misCervix=[225,40,14]
misBleeding = [83,15,53]
misFre=[32,24,84]

data = [misIron, misCervix, misBleeding,misFre]

# Create the pandas DataFrame
index = ['15-19', '20-35', '35 up']
df = pd.DataFrame({'Iron Deficiency': misIron,
                   'Incompetent Cervix': misCervix,
                   'Excess Menstrual Bleeding':misBleeding,
                   'Frequent Pregnancy': misFre}, index=index)
ax = df.plot.bar(rot=0)
plt.ylabel('Numbers')
plt.xlabel('Age Range')
plt.savefig('miscarriageBar.png')
plt.show()

print('########### Anemia ###########')

# mis15_19Iron= mainDataset.loc[ (mainDataset['Age']==1) & (mainDataset['Disease'] == 1) , 'Iron Deficiency',] #() is vvi think

misIron=[316,154,201]
misCervix=[197,96,125]
misBleeding = [366,179,234]
misFre=[270,132,172]


# Create the pandas DataFrame
index = ['15-19', '20-35', '35 up']
df = pd.DataFrame({'Iron Deficiency': misIron,
                   'Incompetent Cervix': misCervix,
                   'Excess Menstrual Bleeding':misBleeding,
                   'Frequent Pregnancy': misFre}, index=index)
df.plot.bar(rot=0)
plt.ylabel('Numbers')
plt.xlabel('Ages Range')
plt.savefig('anemiaBar.png')
plt.show()
