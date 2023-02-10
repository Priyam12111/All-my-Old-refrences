import csv
import pandas as pd

i = 0
while i < 3:
    df = pd.read_excel('plag.xlsx')
    print(df['Instrument'].iloc[i])
    df = df.drop('Instrument', axis = 1, inplace=True)
    i+=1