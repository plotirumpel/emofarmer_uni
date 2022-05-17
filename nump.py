import numpy as np

def task10x10():
    one = np.ones(10, dtype = np.int64)
    zero = np.zeros((9,10), dtype = np.int64)
    return np.vstack((one,zero))

#print(task10x10())

def task_border():
    ans = np.ones((10,10), dtype = np.int64)
    ans[1:-1,1:-1]=0
    return ans

#print(task_border())

def task_2_5x5():
    ans = np.full((5,5), 2, dtype=np.int64)
    return ans

#print(task_2_5x5())

def task_0123():
    zero = np.zeros((5,5), dtype=np.int_)
    one, two, three = np.full_like(zero, 1), np.full_like(zero, 2), np.full_like(zero, 3)
    return np.hstack((np.vstack((zero,two)), np.vstack((one,three))))

#print (task_0123())

def task_chess():
    square = [[0,1],[1,0]]
    return np.tile(square, [5,5])

#print(task_chess())

def task_1_to_9_lines():
    mask = np.zeros((10,10), dtype = np.int64)
    for i in range (10):
        mask[i]+=i
    return mask

#print (task_1_to_9_lines())

def task_1_to_100():
    ans = np.arange(1,101).reshape(10,10)
    return ans

#print (task_1_to_100())

def task_multiplication_table():
    first = np.arange(1,10)
    mask = np.tile(first, (10,1))
    for i in range(10):
        mask[i] *= i
    return mask

#print(task_multiplication_table())

def task_3_diags(n,a,b):
    diag = np.diag(np.array([a]*n), k=0)
    triang_1 = np.diag(np.array([b]*(n-1)), k=1)
    triang_2 = np.diag(np.array([b]*(n-1)), k=-1)
    return diag + triang_2 + triang_1

#print(task_3_diags(4,1,2))

def task_double_chess():
    ans1 = np.resize(np.array([[0,0], [1,1]]), (2, 20))
    ans2 = np.resize(np.array([[1,1], [0,0]]), (2, 20))
    ans = np.vstack((ans1, ans2))
    for i in range (4):
        ans = np.vstack((ans, ans1))
        ans = np.vstack ((ans, ans2))
    return ans

#print(task_double_chess())
