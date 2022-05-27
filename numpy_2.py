import numpy as np

def task_k(matr,k):
    matr=np.array(matr)
    return(matr[matr%k!=0])

#print(task_1([20, 30, 40, 50, 60, 70, 80], 4))

def task_evens(matr):
    matr=np.array(matr)
    matr[matr%2 == 0] //= 2
    return(matr)

#print(task_2([20, 30, 40, 50, 60, 70, 80, 65]))

def task_resheto(matr):
    for i in range (2,101):
        mask = np.logical_or(matr%i != 0, matr == i)
        matr = matr[mask]
    return matr

#matr = np.arange(2,101)
#print(task_3(matr))

def task_fib(n):
    matr = np.array([[0,1],[1,1]])
    matr = np.linalg.matrix_power(matr, n)
    return(matr[1][1])

#print(task_fib(3))