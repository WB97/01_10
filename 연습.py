import random
import time

bubble_time = 0
selection_time = 0

def bubble(a):
    start = time.time()
    n=len(a)
    global bubble_time

    for i in range(n-1):
        for j in range(n-1,i,-1):
            if a[j-1] > a[j]:
                a[j-1],a[j]=a[j],a[j-1]
    print(f'버블정렬 결과 : {a}')
    bubble_time = time.time() - start

def selection(a):
    start = time.time()
    n=len(a)
    global selection_time

    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
    print(f'단순선택정렬 결과 : {a}')
    selection_time = time.time() - start

a = list()
while True:
    a.append(random.randint(1,1000))
    if len(a) >= 1000:
        break
bubble(a)
selection(a)

if bubble_time > selection_time :
    print(f'선택정렬이 {bubble_time - selection_time:.3}초 만큼 더 빠름')
elif selection_time > bubble_time :
    print(f'버블정렬이 {selection_time - bubble_time:.3}초 만큼 더 빠름')
else :
    pass