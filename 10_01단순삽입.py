#단순삽입정렬
import random
import time

def insertion(a):
    start = time.time()
    n=len(a)

    for i in range(1,n):
        j = i
        tmp = a[i]
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp
    print(a)
    print(f'총 걸린 시간 : {time.time()-start:.5}')

x = list()
for i in range(1,1000):
    x.append(random.randint(1,1000))
insertion(x)

###############################################

#이진 삽입 정렬
