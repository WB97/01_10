def search(s,c):    #s는 가게 부품, c는 고객이 찾는 부품
    for i in range(len(c)) :    #고객이 찾는 부품 갯수만큼 반복
        le = 0
        ri = len(s) - 1
        while True:     #이진 검색 시작
            center = (le+ri)//2
            if s[center] == c[i] :
                print(f'{c[i]}는 있습니다.')
                break
            elif s[center] > c[i] :
                ri = center-1
            elif s[center] < c[i] :
                le = center+1
            if le > ri :
                print(f'{c[i]}는 없습니다.')
                break

shop = int(input('가게의 부품 개수 : '))
shop_part=list(map(int,input('부품 종류 : ').split(' ')))

customer = int(input('손님의 요구 부품 개수 : '))
cus_part = list(map(int,input('부품 종류 : ').split(' ')))

search(shop_part,cus_part)