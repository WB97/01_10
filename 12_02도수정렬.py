import random
import time

def fsort(a, max):
    n = len(a)
    f = [0] * (max+1)
    b = [0]*n

    for i in range(n):
        f[a[i]] += 1
    for i in range(1, max+1):
        f[i] += f[i-1]
    for i in range(n-1, -1, -1):
        f[a[i]] -= 1
        b[f[a[i]]] = a[i]
    for i in range(n):
        a[i] = b[i]

def counting_sort(a):
    fsort(a,max(a))

x = list()
while True:
    x.append(random.randint(1,1000))
    if len(x) == 1000:
        break
start = time.time()
counting_sort(x)
print(x)
print(f'실행 시간 : {time.time() - start:.5}')