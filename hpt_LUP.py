import numpy as np

class sqr_sys():
    
    def __init__(self, n):
        self.self = np.empty((n,n))
        for j in range(n):
            for k in range(n):
                self.self[j,k] = input(f'variable {j+1}{k+1}: ')
        self.L = np.zeros((n,n))
        self.U = np.array(self.self)
        self.b = np.empty((n))
        # Gaussian elimination with U
        for k in range(n):
            self.L[k,k] = 1       
        for k in range(n-1):
            for j in range(k+1,n):
                self.L[j,k] = self.U[j,k]/self.U[k,k]
                self.U[j] = self.U[j] - self.U[k]*self.U[j,k]/self.U[k,k]
        
    def solve(self):
        n = len(self.b)
        for j in range(n):
            self.b[j] = input()
        x = np.empty((n))
        y = np.empty((n))
        # Solve Ly = b
        for j in range(n):
            s = 0
            for k in range(j):
                s += y[k]*self.L[j,k]
            y[j] = (self.b[j] - s) / self.L[j,j]        
        # Solve Ux = y
        for j in reversed(range(n)):
            s = 0
            for k in reversed(range(j+1,n)):
                s += x[k]*self.U[j,k]
            x[j] = (y[j] - s) / self.U[j,j]
        return x

while True:
    a = int(input('How many variables? '))
    b = sqr_sys(a)
    while True:
        print('Enter U ')
        c = b.solve()
        print(c)
        d = input('New sys?(y/n) ')
        if d == 'y':
            break
        else:
            continue




