#Brendan Sweeney,05/03/2018
#Factorial Function
#The following discussion was consulted : https://stackoverflow.com/questions/5136447/function-for-factorial-in-python

def factorial(n_in): #Define factorial
    fact = 1
    while (n_in > 0):# loop only for positive numbers
        fact = fact * n_in #first multiplication will set 'fact' to value of n_in 
        n_in = n_in - 1 #then n_in reduced by one on each pass will give factorial
    return fact # return final value of fact at end of looping
print("The factorial of 5 is", factorial(5))
print("The factorial of 7 is", factorial(7))
print("The factorial of 10 is", factorial(10))




