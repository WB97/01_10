#스택
class FixedStack:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self,capacity=256):
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self):      #객체의 길이를 가져다줌
        return self.ptr

    def is_empty(self):
        return self.ptr <=0

    def is_full(self):
        return self.ptr >= self.capacity

    def push(self, value):
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self):
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self): #스택의 top을 읽음
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]

    def clear(self):
        self.ptr = 0

    def find(self,value):
        for i in range(self.ptr-1,-1,-1):
            if self.stk[i] == value:
                return i
            return -1

    def count(self,value):
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c += 1
        return c
    def __contains__(self, value):
        return self.count(value)

    def dump(self):
        if self.is_empty():
            print('스택이 비어 있습니다.')
        else:
            print(self.stk[:self.ptr])

#######################################

from enum import Enum
Menu=Enum('Menu',['푸시','팝','피크','검색','덤프','종료'])

def select_menu():
    s=[f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s,sep=' ',end='')
        n=int(input(': '))
        if 1 <= n <= len(Menu) :
            return Menu(n)

s = FixedStack(64)

while True:
    print(f'현재 데이터 개수 : {len(s)} / {s.capacity}')   #__len__이 있기때문에 len(s)가능
    menu = select_menu()

    if menu == Menu.푸시:
        x = int(input('데이터 : '))
        try:
            s.push(x)
        except FixedStack.Full:
            print('스택이 가득 차 있습니다.')

    elif menu == Menu.팝:
        try:
            x = s.pop()
            print(f'팝한 데이터는 {x}입니다.')
        except FixedStack.Empty:
            print('스택이 비어 있습니다.(팝)')

    elif menu == Menu.피크:
        try:
            x = s.peek()
            print(f'피크한 데이터는 {x}입니다.')
        except FixedStack.Empty:
            print('스택이 비어있습니다.(피크)')

    elif menu == Menu.검색:
        x = int(input('검색할 값을 입력하세요'))
        if x in s:  #__contains__(x)가 있기때문에 객체로 실행 가능하다.
            print(f'{s.count(x)}개 포함되고, 맨 위의 위치는{s.find(x)}입니다.')

    elif menu == Menu.덤프:
        s.dump()

    else:
        break