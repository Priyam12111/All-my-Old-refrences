import os

def filname(path):
    a = os.listdir(path)
    x = 0
    while x < 30:
        with open('nam.csv','a') as f:
            f.write(a[x][:-5] + '\n')
            x += 1

path1 = input('Filepath: ')
filname(path1)