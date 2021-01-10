#해시법

class Node: #해시를 구성하는 노드
    def __init__(self,key, value, next:None):
        self.key = key
        self.value = value
        self.next = next    #뒤쪽노드

class ChainedHash:  #체인법으로 해시 클래스 구현
    def __init__(self):  #초기화
        self.capacity = 13    #해시테이블의 크기
        self.table = [None]*self.capacity   #해시 테이블(리스트)을 선언, capacity만큼의 크기 지정
        a = {1:'kor',2:'eng',3:'usa',14:'jpn',15:'chn',16:'fra',27:'ind',28:'sud',29:'mex',4:'bra'}
        for i,j in a.items():
            hash = self.hash_value(i)
            temp = Node(i,j,self.table[hash])
            self.table[hash] = temp

    def hash_value(self,key):  #해시값을 구함
        return key % self.capacity

    def search(self,key):    #키가 key인 원소를 검색하여 값을 반환
        hash = self.hash_value(key)     #검색하는 키의 해시값
        p = self.table[hash]    #노드를 주목

        while p is not None:
            if p.key == key:
                return p.value  #검색 성공
            p = p.next      #뒤쪽 노드 주목
        return None     #검색 실패

    def add(self,key,value):    #키가 key이고 값이 value인 원소를 추가
        hash = self.hash_value(key)     #추가하는 key의 해시값
        p = self.table[hash]    #노드를 주목

        while p is not None:
            if p.key == key:    #들어갈 키와 p에 들어있는 키가 같은지를 비교
                return False    #추가 실패
            p = p.next      #뒤쪽 노드를 주목

        temp = Node(key,value,self.table[hash])
        self.table[hash] = temp     #노드를 추가
        return True     #추가 성공

    def remove(self,key):   #키가 key인 원소를 삭제
        hash = self.hash_value(key)     #삭제할 key의 해시값
        p = self.table[hash]
        pp = None

        while p is not None:    #key를 발견하면 아래를 실행
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True     #key 삭제 성공
            pp = p
            p = p.next  #뒤쪽 노드를 주목
        return False    #삭제 실패(key가 존재하지 않음)

    def dump(self) -> None: #해시 테이블을 덤프
        for i in range(self.capacity):
            p = self.table[i]
            print(i,end='')
            while p is not None:
                print(f' ->{p.key} ({p.value})',end='')
                p = p.next
            print()

#############################################

from enum import Enum
Menu=Enum('Menu',['추가','삭제','검색','덤프','종료'])

def select_menu():
    s=[f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s,sep=' ',end='')
        n=int(input(': '))
        if 1 <= n <= len(Menu) :
            return Menu(n)

hash = ChainedHash()

while True:
    menu=select_menu()
    if menu == Menu.추가:
        key=int(input('추가할 키 : '))
        val=input('추가할 값 : ')
        if not hash.add(key,val):
            print('추가 실패')

    elif menu == Menu.삭제:
        key=int(input('삭제할 키 : '))
        if not hash.remove(key):
            print('삭제 실패')

    elif menu == Menu.검색:
        key=int(input('검색할 키 : '))
        t=hash.search(key)
        if t is not None:
            print(f'검색한 키를 갖는 값은 {t}입니다.')
        else:
            print('검색할 데이터가 없읍니다.')
    elif menu == Menu.덤프:
        hash.dump()
    else:
        break