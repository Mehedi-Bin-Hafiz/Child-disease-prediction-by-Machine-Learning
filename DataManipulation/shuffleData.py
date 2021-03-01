import  pandas as pd
MainDatabase = pd.read_excel("../database/RawData.xlsx",).sample(frac=1)
MainDatabase.to_excel(r'../database/MainDataset.xlsx', index=False)
