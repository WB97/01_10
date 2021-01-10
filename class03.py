# a = 1
# def test() :
#     global a
#     a = 3
#     print(a)
# print(a)
# test()
# print(a)

#스택
# a=[]
# a.append(100)   #차곡차곡 저장
# a.append(200)
# a.append(300)
# print(a)
# b = a.pop()     #가장 마지막 인덱스 추출
# print(a)
# print(b)

#큐
# a = []
# a.append(100)      #차곡차곡 저장
# a.append(200)
# a.append(300)
# print(a)
# b=a.pop(0)      #가장 처음 인덱스 추출
# print(a)
# print(b)

#print([1,2,3] < [2,1,2])

# a=[1,2,3]
# b=[1,2,3]
# print(a is b)
#
# a=1
# b=1
# print(a is b)

# a={1,1,2,2,3,3}
# print(a)
# b=set([1,1,2,2,3,3])
# print(b)
# a.clear()
# print(a)

# def max(a) :
#     m=a[0]
#     # if a[1] > m:
#     #     m=a[1]
#     # if a[2] > m:
#     #     m=a[2]
#     # if a[3] > m:
#     #     m=a[3]
#     # if a[4] > m:
#     #     m=a[4]
#     # if a[5] > m:
#     #     m=a[5]
#     for i in range(1,len(a)) :
#         if a[i] > m :
#             m = a[i]
#     return m
#
# a=[1,2,3,4,5,22,2,3,33]
# print(max(a))

# from typing import Any, Sequence
#
# def max(a:Sequence) -> Any :

# it=iter({100,200,300})
# print(it.__next__())
# print(next(it))

# def reverse_array(a):
#     n=len(a)
#     for i in range(n//2):
#         a[i],a[n-i-1]=a[n-i-1],a[i]
#     print(a)
# a=[1,2,3,4,5,6,7,8,9]
# reverse_array(a)