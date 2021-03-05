import matplotlib.pyplot as plt
import pandas as pd

########### vvi code for paper#########
plt.rcParams["font.family"] = "Times New Roman"
# plt.rcParams["figure.figsize"] = [9,5]
plt.rcParams.update({'font.size': 10})
########### vvi code for paper#########

mainDataset = pd.read_excel(r'../database/MainDataset.xlsx')

# real = mainDataset['Pneumonia (+ / -)'].values.tolist()
# predicted = mainDataset['Prediction'].values.tolist()

ChickenPox,Malaria, Diarrhea,NoDisease = mainDataset['DiseaseName'].values.tolist().count(0),mainDataset['DiseaseName'].values.tolist().count(1),mainDataset['DiseaseName'].values.tolist().count(2),mainDataset['DiseaseName'].values.tolist().count(3)

labels = 'ChickenPox','Malaria', 'Diarrhea','NoDisease'

sizes = [ChickenPox,Malaria, Diarrhea,NoDisease]
explode = (0,0,0,0)
#autopact show percentage inside graph
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',)
plt.axis('equal')
plt.savefig('diseaseParcentage.png')
plt.show()