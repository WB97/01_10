#이진 검색
from typing import Any, Sequence
def bin_search(a:Sequence, key:Any)->int:
    pl=0    #검색 범위 맨 앞의 인덱스
    pr=len(a)-1     #검색 범위 맨끝 인덱스

    while True:
        pc=(pl+pr)//2   #중앙 인덱스

        if a[pc]==key: return pc    #검색 성공
        elif a[pc] < key: pl=pc+1   #검색 범위를 뒤쪽 절반으로 좁힘
        else: pr=pc-1   #검색 범위를 앞쪽 절반으로 좁힘
        if pl>pr: break
        return -1   #검색 실패

if __name__=='__main__':
    num = int(input('원소 수 입력 : '))
    x=[None]*num

    print('배열 데이터를 오름차순으로 입력.')
    x[0]=int(input('x[0] : '))

    for i in range(1,num):
        while True:
            x[i]=int(input(f'x[{i}] : '))
            if x[i] >= x[i-1]:
                break
    ky = int(input('검색 할 값 : '))
    idx = bin_search(x,ky)

    if idx==-1:
        print('없음')
    else:
        print(f'x[{idx}]에 있습니다.')

#########################################

#복잡도
