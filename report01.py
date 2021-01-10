def med3(a,b,c) :
    if a>=b and b>=c :
        return b
    elif a<b and b<c :
        return b
    elif a>=c and c>=b :
        return c
    elif b>c and c>a :
        return c
    elif b>=a and a>=c:
        return a
    elif c>a and a>b:
        return a

print(med3(3,1,2))