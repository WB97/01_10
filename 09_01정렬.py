#버블정렬 : 이웃한 두개의 원소의 대소를 비교해서 교환

# def bubble_sort(a):
#     n=len(a)
#     ccnt = 0
#     scnt = 0
#     k = 0
#
#     while True:
#         last = n-1
#         for j in range(n-1,k,-1):
#             ccnt += 1
#             if a[j-1] > a[j]:
#                 scnt += 1
#                 a[j-1],a[j]=a[j],a[j-1]
#                 last = j
#         k = last
#         if k >= n-1:
#             break
#     print(a)
#     print(f'교환 = {ccnt}')
#     print(f'비교 = {scnt}')
#
# x=[9,8,7,6,5,4,3]
# bubble_sort(x)

#####################################

#세이커정렬 : 맨 뒤에서부터 스캔, 맨 앞에서부터 스캔 둘 모두를 사용
def shaker_sort(a):
    left = 0
    right = len(a)-1
    last = right
    while left < right:
        for j in range(right, left, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        left = last
        print(f'오른쪽 - > {a}')

        for j in range(left, right):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1],a[j]
                last = j
        right = last
        print(f'왼쪽 - > {a}')
    print(a)

x=[9,8,7,6,5,4,3]
print(x)
shaker_sort(x)