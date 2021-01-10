n = 3
pos = [0]*n
flag = [False]*n    #각 행에 퀸을 배치 했는지 체크

def put():
    for i in range(n):
        print(f'{pos[i]:2}',end='')
    print()

def set(i):
    for j in range(n):
        if not flag[j]: #flag[j]가 True면 pass
            pos[i] = j
            if i == n-1:
                put()
            else:
                flag[j] = True  #pos[j]에 값이 들어갔으니 flag[j]에도 true
                set(i+1)    #i증가시켜서 호출 (재귀)
                flag[j] = False
            print(flag)

set(0)