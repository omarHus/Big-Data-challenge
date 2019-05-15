import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("Datasets/NSDUHsaeExcelTab01-2017.csv", skiprows=5)

def getting_int(df):

    coloumns = list(df)
    for i in range(2,len(coloumns)):
        df[coloumns[i]] = df[coloumns[i]].map(lambda x: x.rstrip("%"))
        df = df.astype({coloumns[i]:float})
    
    return df


numeric_df = getting_int(df)
numeric_df.hist(bins=15, figsize=(20,15))

plt.show()
print(numeric_df.get_dtype_counts())