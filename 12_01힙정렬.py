import random
import time

def heap(a):
    def down_heap(a, left,right):
        temp = a[left]

        parent = left
        while parent < (right + 1) // 2:
            cl = parent * 2 + 1
            cr = cl+1
            child = cr if cr <= right and a[cr] > a[cl] else cl
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp

    n = len(a)

    for i in range((n-1)//2, -1, -1):
            down_heap(a, i, n-1)

    for i in range(n-1, 0, -1):
            a[0], a[i] = a[i], a[0]
            down_heap(a, 0, i -1)
x = list()
while True:
    x.append(random.randint(1,1000))
    if len(x) == 1000:
        break
start = time.time()
heap(x)
print(x)
print(f'실행 시간 : {time.time() - start:.5}')