import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 12})

checkValidationDataSet = pd.read_excel(r'../database/predictedDataSet.xlsx')

real = checkValidationDataSet['DiseaseName'].values.tolist()
predicted = checkValidationDataSet['Prediction'].values.tolist()

XandYLen = []
for i in range(1, len(real) + 1):
    XandYLen.append(i)
axes = plt.axes()
plt.plot(XandYLen, real,  linewidth=6)
plt.plot(XandYLen, predicted,  linewidth=2)
axes.set_yticks([ -1,-.5,0, .5, 1, 1.5, 2, 2.5,3,3.5,4])
plt.grid()
plt.legend(['Real value', 'Predicted value'])
plt.xlabel('Numbers')
plt.ylabel('Prediction')
plt.savefig(" real vs prediction.png")
plt.show()
print('###Bar Graph###')