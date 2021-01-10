#2강 반복문 알고리즘
# n = int(input('n'))
# w = int(input('w'))
# for i in range(n//w):
#     print('*'*w)

area = int(input('a : '))
i = 0
# for i in range(1,area+1):
#     if i*i>area :
#         break
#     if area%i == 0:
#         print(f'{i} x {area//i} = {area}')

while True :
    i+=1
    if i*i>area : break
    if area%i : continue
    else : print(f'{i} x {area//i} = {area}')

# n = int(input('크기 : '))
# a = 1
# for i in range(n,-1,-1):
#     print(' '*i, end='')
#     print('*'*a)
#     a+=1
