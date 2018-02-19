# Ian McLoughlin
# A program that displays Fibonacci numbers.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# Test the function with the following value.
x = 16 
ans = fib(x)
print("Fibonacci number", x, "is", ans)


#My name is Brendan, so the first and last letter of my name (B+ N = 2 + 14) gives the number 16 . 
#The 16th Fibonacci number is 987.

# Ian McLoughlin
# A program that displays Fibonacci numbers using people's names.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Sweeney"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)

#My surname is Sweeney
#The first letter S is number 83
#The last letter y is number 121
#Fibonacci number 204 is 1923063428480944139667114773918309212080528



#The ord() command well generate a numerical value for an 
#unicode character based on the characters position on the unicode list. 

#sycing test. 
