#Brendan Sweeney,05/03/2018
#Factorial Function

def factorial(n_in):
    fact = 1
    while (n_in > 0):# set limit on number of loops
        fact = fact * n_in #set fact to value of n_in
        n_in = n_in - 1 #then reduce n_in by one on each pass
    return fact # return final value of fact at end of looping
print("The factorial of 5 is", factorial(5))
print("The factorial of 7 is", factorial(7))
print("The factorial of 10 is", factorial(10))




