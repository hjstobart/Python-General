'''
Low Dimension Matrix Inversion
--------------------------------
This is a short and simple Python script that implements the analytical 
inversion of a 2x2 matrix. It can be done using a direct code implementation
(not recommended) or using a function. Both of which are included in this file.
'''

# -------------------------------
# Method 1: Direct implementation
# -------------------------------

print('2x2 Matrix Inverter\n')

a = float(input('Input a: '))
b = float(input('Input b: '))
c = float(input('Input c: '))
d = float(input('Input d: '))

matrix = [[a , b] , [c , d]]
print('\nYour matrix:\n')
print(matrix[0],'\n',matrix[1])

det = ((a * d) - (b * c))
print('\nDeterminant: ', det)

if det == 0:
    print('\nMatrix is singular.')
else:
    inv_matrix = [[(d/det) , (-1*b/det)] , [(-1*c/det) , (a/det)]]
    print('\nInverse:\n')
    print(inv_matrix[0],'\n',inv_matrix[1])
    
    
# -------------------------------
# Method 2: Using a function
# -------------------------------

def twobytwoinversion(a,b,c,d):
    a, b, c, d = float(a), float(b), float(c), float(d)

    matrix = [[a , b] , [c , d]]
    print('\nYour matrix:\n')
    print(matrix[0],'\n',matrix[1])

    det = ((a * d) - (b * c))
    print('\nDeterminant: ', det)

    if det == 0:
        print('\nMatrix is singular.')
    else:
        inv_matrix = [[(d/det) , (-1*b/det)] , [(-1*c/det) , (a/det)]]
        print('\nInverse:\n')
        print(inv_matrix[0],'\n',inv_matrix[1])

