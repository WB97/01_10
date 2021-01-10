#오픈 주소법

from enum import Enum

class Status(Enum):
    OCCUPIED = 0
    EMPTY = 1
    DELETED = 2

class Bucket:
    def __init__(self,key=None, value=None, stat=Status.EMPTY):
        self.key=key
        self.value=value
        self.stat=stat

    def set(self,key,value,stat):
        self.key=key
        self.value=value
        self.stat=stat

    def set_status(self,stat):
        self.stat=stat

class OpenHash:
    def __init__(self,capacity):
        self.capacity = capacity
        self.table = [Bucket()]*self.capacity

    def hash_value(self,key):
        return key % self.capacity

    def rehash_value(self,key):
        return (self.hash_value(key)+1) % self.capacity

    def search_node(self,key):
        hash=self.hash_value(key)
        p = self.table[hash]

        for i in range(self.capacity):
            if p.stat == Status.EMPTY : break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            hash=self.rehash_value(hash)
            p=self.table[hash]
        return None

    def search(self,key):
        p=self.search_node(key)
        if p is not None:
            return p.value
        else :
            return None

    def add(self,key,value):
        if self.search(key) is not None:
            return False

        hash = self.hash_value(key)
        p = self.table[hash]

        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key,value,Status.OCCUPIED)
                return True
            hash=self.rehash_value(hash)
            p=self.table[hash]
        return False

    def remove(self,key):
        p=self.search_node(key)
        if p is None:
            return False
        p.set_status(Status.DELETED)
        return True

    def dump(self):
        for i in range(self.capacity):
            print(f'{i:2}',end='')
            if self.table[i].stat == Status.OCCUPIED:
                print(f' {self.table[i].key} ({self.table[i].value})')
            elif self.table[i].stat == Status.EMPTY:
                print('--미등록--')
            elif self.table[i].stat == Status.DELETED:
                print('--삭제완료--')

####################################################

from enum import Enum
Menu=Enum('Menu',['추가','삭제','검색','덤프','종료'])

def select_menu():
    s=[f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s,sep=' ',end='')
        n=int(input(': '))
        if 1 <= n <= len(Menu) :
            return Menu(n)

hash = OpenHash(13)

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