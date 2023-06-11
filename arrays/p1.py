a,b,c,d,e=[i for i in input().split()]
a=int(a)
e=int(e)
c=int(c)
if b=='-':
    if a-c==e:
        print("Yes")
    else:
        print( a-c)




elif b=='+':
    if a+c==e:
        print("Yes")
    else:
        print( a+c)


        
elif b=='*':
    if a*c==e:
        print("Yes")
    else:
        print( a*c)
