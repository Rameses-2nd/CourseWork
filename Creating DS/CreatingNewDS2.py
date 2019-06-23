
from pandas import DataFrame, read_csv

import pandas as pd

import matplotlib.pyplot as plt
#from matplotlib import style

#style.use('fivethirtyeight')
#a= 50.881677028;
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
#df7['Date'].to_csv('foo.csv')
df7['Value'].to_csv('foo.csv')



#df8 = pd.read_csv('foo.csv', names = ['Date','House_Price'], index_col=1)
#print(df7.head())
#df8.rename(columns={'House_Price':'Prices'}, inplace=True)
#file3=r'foo.csv'
#df7=pd.read_csv(file3)
#df.plot()
#plt.show()
#pd.concat([
    #pd.concat([df4, df6], axis=0)]).to_csv('foo.csv')
#print(df3)

#print(df['Value'])

#print(df)
#print(df['Value'])
#print(df2['Value'])
#data = pandas.DataFrame({'df4' : ['Date', 'Value'],
                        #'df6' : ['Date', 'Value']
                        #})
#print (data[['df4', 'df6']])