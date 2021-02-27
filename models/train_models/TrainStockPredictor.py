import pandas as pd
import numpy as np

df = pd.read_csv('./data/stock_data.csv')

df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'OpenInt', 'Stock']

vals = np.unique(df['Stock'])

for i in vals:
    # loop through each stocks data 
    cmp_data = df.loc[df['Stock'] == i]
    print(len(cmp_data))
    