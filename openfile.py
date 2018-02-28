#Brendan Sweeney, 28/02/2018
#Program to display Iris.csv in a pleasing format

import csv
with open("data\iris.csv",) as f:
    f_read= csv.reader(f)
    print("Fisher's Iris data set:  ")
    for row in f_read:
        print('{:<6}  {:<6}  {:<6}  {:<6}  {:<}'.format(*row))
        




    