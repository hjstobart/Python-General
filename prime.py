"""
This is a short function that tests whether a given number is prime. 
"""

def isPrime(number) :
    if number > 1 :
        for i in range(2 , number//2) :
            if number % i == 0 :
                return False
        return True
    else :
        return False
    
number = int(input('Enter a number to check if its prime: '))

if isPrime(number) :
    print('{} is a Prime number'.format(number))
else :
    print('{} is not a Prime number'.format(number))
