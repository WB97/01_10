address=dict()
n = int(input('사람 수 : '))

for i in range(n):
    name = input(f'{i + 1}번째 사람 이름 : ')
    age = int(input(f'{i + 1}번째 사람 나이 : '))
    address.setdefault(name, age)   #키(이름)와 값(나이) 저장

s = sum(address.values())//n        #평균 계산

for i,j in address.items():
    print(f'{i}의 나이는{j}입니다.')

print(f'주소록에 있는 사람들의 평균 나이는{s}입니다.')