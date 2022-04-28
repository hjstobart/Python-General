"""
This script contains two functions, both computing and displaying the Fibonacci sequence, but each depending on slightly different criteria.
"""

# ----------------------------------
# Function 1:
# Fibonacci function that prints numbers in the sequence less than n.

def fibonacci_1(n):
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b , a+b
    
n = int(input('Please enter a number: '))
fibonacci_1(n)

# ----------------------------------
# Function 2:
# Fibonacci function that prints the first n numbers in the sequence.

def fibonacci_2(n):
    a, b = 0, 1
    fib = [] ;
    while len(fib) != n:
        fib.append(b)
        print(b)
        a, b = b, a+b
        
n = int(input('Please enter a number: '))
fibonacci_2(n)