#Brendan Sweeney, 28/02/2018
#Program to display Iris.csv in a pleasing format

import csv #import csv tools
with open("data\iris.csv",) as f: # open file
    f_read= csv.reader(f) #read csv data
    print("Fisher's Iris data set:  ")
    for row in f_read: # For all rows in file
        print('{:<6}  {:<6}  {:<6}  {:<6}  {:<}'.format(*row)) #Align and space data to be displayed. 
        




    