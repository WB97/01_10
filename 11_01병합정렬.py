import random
import time

def merge(a) :
    def _merge(a,left,right):
        if left < right:
            center = (left + right)//2

            _merge(a, left, center)
            _merge(a, center+1, right)

            p = j = 0
            i = k = left

            while i <= center:
                buff[p] = a[i]
                p += 1
                i += 1

            while i <= right and j < p:
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1

            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1

    n = len(a)
    buff = [None] * n
    _merge(a,0,n-1)
    del buff

x = list()
for i in range(1000):
    x.append(random.randint(1,1000))
start = time.time()
merge(x)
print(x)
print(f'실행시간 : {time.time()-start:.5}')
