"""
This is a short function that finds and prints the factors of a number.
"""

def factor(number):
    print('\nFactors are: ') 
    for i in range(1, number+1) :
        if number % i == 0 :
            print(i)

number = int(input('Please enter a number: '))
factor(number)

