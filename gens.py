import string


def gens_1(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b


def gens_2(name):
    with open(name, mode='r', encode='utf8') as f:
        while True:
            symb = f.read(1)
            yield symb

def gens_3(name):
    with open(name, mode="r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if line == "":
                break
            words = line.split()
            ans = [word.strip(string.punctuation) for word in words]
            for i in range(len(ans)):
                yield ans[i]

#g = gens_3('text1.txt')
#for x in g:
#    print(x)

def gens_4(var1, var2):
    leng = min(len(var1),len(var2))
    for i in range(leng):
        yield (var1[i], var2[i])

'''
g = gens_4([10, 20, 30], "ab")
for x in g:
    print(x)
'''

def gens_5(n):
    counter = 0
    for i in range(1, n):
        for j in range(0, i):
            counter += 1
            if counter == n+1:
                return
            yield i
''' 
g = gens_5(10)
for x in g:
    print(x)
'''