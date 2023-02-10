import csv
import pandas as pd

i = 0
while i < 3:
    df = pd.read_excel('Naukri Data.xlsx')
    print(df['Link'].iloc[i])
    df = df.drop('Link', axis = 1, inplace=True)
    print(df)
    i+=1