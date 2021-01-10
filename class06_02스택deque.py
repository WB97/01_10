from collections import deque
class Stack:
    def __init__(self,maxlen = 256):
        self.capacity = maxlen
        self.__stk = deque([],maxlen)   #__변수 : 클래스 private변수

    def __len__(self):
        return len(self.__stk)

    def is_empty(self):
        return not self.__stk

    def is_full(self):
        return len(self.__stk) == self.__stk.maxlen

    def push(self, value):
        self.__stk.append(value)

    def pop(self):
        return self.__stk.pop()

    def peel(self):
        return self.__stk[-1]

    def clear(self):
        self.__stk.clear()

    def find(self,value):
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1

    def count(self, value):
        return self.__stk.count(value)

    def __contains__(self,value):
        return self.count(value)

    def dump(self):
        print(list(self.__stk))

############################################

from enum import Enum
Menu=Enum('Menu',['푸시','팝','피크','검색','덤프','종료'])

def select_menu():
    s=[f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s,sep=' ',end='')
        n=int(input(': '))
        if 1 <= n <= len(Menu) :
            return Menu(n)

s = Stack(64)

while True:
    print(f'현재 데이터 개수 : {len(s)} / {s.capacity}')   #__len__이 있기때문에 len(s)가능
    menu = select_menu()

    if menu == Menu.푸시:
        x = int(input('데이터 : '))
        try:
            s.push(x)
        except Stack.Full:
            print('스택이 가득 차 있습니다.')

    elif menu == Menu.팝:
        try:
            x = s.pop()
            print(f'팝한 데이터는 {x}입니다.')
        except Stack.Empty:
            print('스택이 비어 있습니다.(팝)')

    elif menu == Menu.피크:
        try:
            x = s.peek()
            print(f'피크한 데이터는 {x}입니다.')
        except Stack.Empty:
            print('스택이 비어있습니다.(피크)')

    elif menu == Menu.검색:
        x = int(input('검색할 값을 입력하세요'))
        if x in s:  #__contains__(x)가 있기때문에 객체로 실행 가능하다.
            print(f'{s.count(x)}개 포함되고, 맨 위의 위치는{s.find(x)}입니다.')

    elif menu == Menu.덤프:
        s.dump()

    else:
        break