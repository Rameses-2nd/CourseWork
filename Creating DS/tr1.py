import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

file = r'foo.csv'
df = pd.read_csv(file)
df.plot()
plt.show()
print(df)
