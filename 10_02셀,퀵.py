#셸 정렬
import random
import time

def shell(a):
    start = time.time()
    n =len(a)
    h = n//2
    while h>0:
        for i in range(h,n):
            j = i-h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j+h] = a[j]
                j -= h
            a[j+h] = tmp
        h //= 2
    print(a)
    print(f'총 걸린 시간 : {time.time() - start:.5}')

#퀵 정렬

# start = time.time()
# def quick(a,left,right):
#     pl = left
#     pr = right
#     pv = a[(left+right)//2]
#
#     while pl <= pr:
#
#         while a[pl] < pv :
#             pl += 1
#         while a[pr] > pv :
#             pr -= 1
#
#         if pl <= pr:
#             a[pl],a[pr] = a[pr], a[pl]
#             pl += 1
#             pr -= 1
#     if left < pr : quick(a,left,pr)
#     if pl < right : quick(a,pl,right)

x = list()
for i in range(1,1000):
    x.append(random.randint(1,1000))
# quick(x,0,len(x)-1)
shell(x)
# print(x)
# print(f'총 걸린 시간 : {time.time()-start:.5}')