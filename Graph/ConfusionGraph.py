import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns
plt.rcParams["font.family"] = "Times New Roman"
# plt.rcParams["figure.figsize"] = [9,5]
plt.rcParams.update({'font.size': 12})

checkValidationDataSet = pd.read_excel(r'../database/predictedDataSet.xlsx')
real = checkValidationDataSet['DiseaseName'].values
predicted = checkValidationDataSet['Prediction'].values
print(real)
print(predicted)
cf_matrix= confusion_matrix(real,predicted)
group_names = ['TN','FP','FN','TP']
group_counts = ['{0:0.0f}'.format(value) for value in
                cf_matrix.flatten()]
labels = [f"{v1}\n{v2}" for v1, v2 in
          zip(group_names,group_counts)]
labels = np.asarray(labels).reshape(2,2)
print(labels.shape, cf_matrix.shape)
sns.heatmap(cf_matrix, annot=True, fmt='',)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.savefig("Confusion Matrix.png")
plt.show()


