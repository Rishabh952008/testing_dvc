import pandas as pd 

df = pd.read_csv('data/employee_data.csv')

df = df[df['Age']>=40]

df = df[df['Attrition']=='Yes']

df.to_csv('data/employee_data.csv',index=False)