import pandas as pd
def write(w1,w2):
    list1= [w1]
    list2= [w2]
    pd.DataFrame({'A': list1, 'B': list2,}).to_csv('hello.csv', index=False)

w1 = 'yes'
w2 = 'None'
write(w1,w2)