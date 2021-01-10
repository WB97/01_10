import time

def bm(txt, pat):
    skip = [None] * 256

    for pt in range(256):
        skip[pt] = len(pat)
    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) - pt - 1

    while pt < len(txt):
        pp = len(pat)-1
        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt
            pt -= 1
            pp -= 1
        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp else len(pat) - pp

    return -1

s1 = '''After Korea was forcibly defeated by the Japanese imperialism in 1910, Korean medical and enthusiastic soldiers launched independence movements across the country in protest against the unjust invasion of Japan. The government-general of the Joseon Dynasty sought to remove the foundation of legitimate national resistance by the Korean people by the extermination of the national culture and the thorough economic domination while undertaking a strong unauthorized governance.
In exile abroad such as the elderly and the Americas, the independence movement was launched, or secret associations were organized to hide underground and wait for opportunities.
In the midst of this, U.S. President Wilson, T. W.'s principle of self-determination was introduced in January 1918 as part of the 14 articles of post-war principles of World War I.
The principle of national self-determination that Wilson envisioned was intended to be applied only to the colonies of allies, such as Germany, Austria, and Turkey, which had confronted the allied powers, but this principle was accepted as a gospel by all the oppressed peoples, each in a direction in its own favor Interpretation of the principle came to demand independence.
Korean national leaders also tried to appeal for the independence of the Korean people based on Wilson's announcement of self-determination of national self-determination.
It was the Korean Americans who responded most sensitively to Wilson's national self-determination. They convened a Korean American representative meeting.
There, Syngman Rhee, Chanho Min, and Hankyung Jeong were elected as representatives of the Korean people and insisted on the self-determination of the Korean people in accordance with the essential ideology of national self-determination.
I tried to appeal for the independence of Korea by sending a Korean representative.
'''

a = input('찾을 문자열 입력')
start = time.time()

b = bm(s1,a)

t = f'{time.time() - start:.30}'

if b == -1:
    print('없음')
else:
    print(f'{b}번째 인덱스에 위치함')
print(f'실행 시간 : {t}')