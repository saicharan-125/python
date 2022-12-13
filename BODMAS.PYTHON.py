x=input("enter the first value :")
y=input("enter the second value :")
if x.isalpha():
    print("alpha is not allowed")
elif y.isalpha():
    print("alpha is not allowed")
else:
    a=int(x)
    b=int(y)    
    c=input("enter any opeartor ,+,-,/,*")
    if c=='+':
        print(a+b)
    elif c=='-':
        print(a-b)
    elif c=='*':
        print(a*b)
    elif c=='/':
        print(a/b)


