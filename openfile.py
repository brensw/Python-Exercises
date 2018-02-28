
import csv
with open("data\iris.csv", 'r') as f:
    f_read= csv.reader(f, delimiter =',')
    for line in f_read:
        print(line)