import csv

def write(w1, w2):
    with open('eggs.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile)
        # spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        spamwriter.writerow([w1,w2])
