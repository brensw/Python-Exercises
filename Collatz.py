#Brendan Sweeney
#Collatz Conjecture
print ("This program will test the Collatz Conjecture")

n_in = int(input("Please enter a number:") ) #Get number to test conjecture
n_test = n_in #Keep original input
while n_test != 1: #loop until n=1 
    n_check = n_test % 2 #Check if number is odd or even 
    if n_check > 0: #If odd multiply by 3 and add 1
        n_test= (n_test * 3) + 1
    else:
        n_test = (n_test /2)    # If even devide by 2 

n_test = str(int(n_test)) #remove decimal point in answer

 
print ("After apllying the conditions of Collatz's conjecture to", n_in )
print ("the number " + n_test + " was generated")
