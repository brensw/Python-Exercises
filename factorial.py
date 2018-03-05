def factorial(n_in):
    fact = 1
    while (n_in > 0):
        fact = fact * n_in
        n_in = n_in - 1
    return fact 
print(factorial(12))



