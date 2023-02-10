import pandas as pd

with open('ssh.csv', 'r') as csvfile:
    df = pd.read_csv(csvfile, lineterminator = '\n')
    df1 = df.T.to_csv('ssh.csv')
    # Transpose(df1)