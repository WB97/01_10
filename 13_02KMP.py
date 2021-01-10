import time

def kmp(txt,pat):
    pt = 1
    pp = 0
    skip = [0] * (len(pat)+1)

    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] == pp
        else:
            pp = skip[pp]

    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]

    return pt - pp if pp == len(pat) else -1

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

b = kmp(s1,a)

t = f'{time.time() - start:.20}'

if b == -1:
    print('없음')
else:
    print(f'{b}번째 인덱스에 위치함')
print(f'실행 시간 : {t}')