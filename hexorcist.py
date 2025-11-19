g = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def t(n,b):
    o=0
    p=0
    for c in n[::-1]:
        o+=g.index(c)*(b**p)
        p+=1
    return o
def f(n,a):
    o=""
    while 1:
        r=n%a
        o=g[r]+o
        n//=a
        if n==0:
            break
    return o
def h(n):
    while 1:
        try:
            int(n)
        except:
            print("no")
        else:
            if 2<=int(n)<=36:
                return int(n)
            else:
                print("no")
        n=input("no")
b=h(input("from"))
a=h(input("to"))
i=input(f"num").upper()
while 1:
    x=1
    for c in i:
        if c not in g.split(g[b])[0]:
            i=input("no").upper()
            x=0
    if x>0:
        break
d=t(i,b)
o=f(d,a)
print(o)