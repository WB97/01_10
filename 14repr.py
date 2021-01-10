
class Node:
    def __init__(self,name,next):
        self.name = name
        self.next = next

class LinkedList:
    def __init__(self,max):
        self.no = 0
        self.head = None
        self.current = None
        self.max = max

    def __len__(self):
        return self.no

    def add(self,name):
        if self.no == self.max-1:
            return False
        if self.head is None:
            ptr = self.head
            self.head = self.current = Node(name,ptr)
            self.no += 1
            if self.no >= self.max:
                return False
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = self.current = Node(name,None)
            self.no += 1
            if self.no >= self.max:
                return False

    def search(self, name):
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data == name:
                self.current = ptr
                return cnt
            else:
                cnt += 1
                ptr = ptr.next
        return -1

    def remove(self,name):
        ptr = self.head
        p = None
        while ptr != None:
            if ptr.name == name:
                p = ptr
                break
            ptr = ptr.next
        else :
            return False

        if self.head is not None:
            if p is self.head:
                if self.head is not None:
                    self.head = self.current = self.head.next
                self.no -= 1
            else:
                ptr = self.head
                while ptr.next is not p:
                    ptr = ptr.next
                    if ptr is None:
                        return False
                ptr.next = p.next
                self.current = ptr
                self.no -= 1
                return True

    def next(self):
        if self.current is None or self.current.next is None:
            return False
        self.current = self.current.next
        return True

    def print(self):
        ptr = self.head

        while ptr is not None:
            print(ptr.name)
            ptr = ptr.next
        print()

    def selection_sort(self):
        ptr_1st = self.head
        while ptr_1st is not None:
            min = ptr_1st
            ptr_2nd = ptr_1st.next
            while ptr_2nd is not None:
                if ptr_2nd.name < min.name:
                    min = ptr_2nd
                ptr_2nd = ptr_2nd.next

            min.name,ptr_1st.name = ptr_1st.name,min.name
            ptr_1st = ptr_1st.next
        print('정렬이 완료되었습니다.')

from enum import Enum

Menu = Enum('Menu',['저장','삭제','검색','출력','정렬','종료'])

def select_menu():
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s,sep=' ',end='')
        n = int(input(' : '))
        if 1 <= n <= len(Menu):
            return Menu(n)

list = LinkedList(100)

while True:
    menu = select_menu()

    if menu == Menu.저장 :
        res = list.add(input('저장할 이름: '))
        if res == False:
            print('리스트가 풀입니다.')

    elif menu == Menu.삭제:
        res = list.remove(input('삭제할 이름 : '))
        if res:
            print('삭제 완료')
        else:
            print('해당 이름이 없습니다.')

    elif menu == Menu.검색:
        pos = list.search(input('검색할 이름 : '))
        if pos >= 0:
            print(f'이름은 {pos+1}번째에 있습니다.')
        else:
            print('해당 이름이 없습니다.')

    elif menu == Menu.출력:
        list.print()

    elif menu == Menu.정렬:
        list.selection_sort()

    elif menu == Menu.종료:
        print('프로그램이 종료됩니다.')
        break

    else:
        print('잘못입력하셨습니다.')

