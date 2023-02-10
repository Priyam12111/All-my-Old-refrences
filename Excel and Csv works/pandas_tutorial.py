import pandas as pd
df = pd.read_excel('FIle_PATH')
htm = (df['HEADER_NAME'].iloc['COLUMN_NUMBER'])
df = df.drop('HEADER_NAME', axis = 1, inplace=True)#This is use for escape from that column