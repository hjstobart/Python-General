"""
A function which computes the lowest common multiple of two integers. 
"""

def lcm(a, b) :
    great = a if (a>b) else b
    max = a*b
    for i in range(great, max):
        if i % a == 0 and i % b == 0 :
                print(i)
                break
        else :
            print(max)
            break
    
a = int(input('First number: '))
b = int(input('Second number: '))

lcm(a,b)