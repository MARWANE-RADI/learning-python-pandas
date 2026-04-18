import pandas as pd

data =[True,False,True]
x = pd.Series(data, index=['STUDANT1','STUDANT2','STUDANT3'])

print(x.iloc[0])
