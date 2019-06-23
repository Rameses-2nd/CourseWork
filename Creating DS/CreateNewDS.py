
from pandas import DataFrame, read_csv

import pandas as pd


file = r'FMAC-HPI_COLIN.csv'
df = pd.read_csv(file)
df3 = df['Value'] >= 50.881677028
df4= df[df3]

file2 = r'FMAC-HPI_COROR.csv'
df2 = pd.read_csv(file2)
df5 = df2['Value'] >= 50.881677028
df6=df2[df5]




print(df4)
print(df6)

pd.concat([
    pd.concat([df4, df6])]).to_csv('foo.csv')


df7 = pd.read_csv('foo.csv')

df7.set_index('Date', inplace = True)
df7.to_csv('foo.csv')

df7['Value'].to_csv('foo.csv')



