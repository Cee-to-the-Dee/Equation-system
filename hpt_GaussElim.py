import numpy as np
def hpt(n):
    A = np.empty((n,n+1))
    x = np.empty((n))
    
    for j in range(n):
        for k in range(n+1):
            A[j,k] = input(f'Variable {j+1}{k+1} ')
            
    for k in range(n-1):
        for j in range(k+1,n):
            A[j] = A[j] - A[k]*A[j,k]/A[k,k]
    
    for j in reversed(range(n)):
        s = 0
        for k in reversed(range(j+1,n)):
            s += x[k]*A[j,k]
        x[j] = (A[j,n] - s) / A[j,j]
       
    return x
    
while True:
    n = int(input('How many variables? '))
    a = hpt(n)
    print(a)
