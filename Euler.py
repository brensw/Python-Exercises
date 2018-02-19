#Brendan Sweeney. 19/02/2018
#Euler Project problem_5

# Modified code from stack exchange
smallest_num = 1
for i in range (1,21): 
    if smallest_num % i != 0: # Check if smallest_num is not evenly divisable by i then 
        for k in range (1,21):
            if (smallest_num * k) % i == 0: # If number evenly divisible by i then   
                smallest_num = smallest_num * k # Change value of smallest_num
                break #back to i loop
print ("The smallest number the can be divided evenly by all the numbers between 1 to 20 is" ,smallest_num)