x=input("enter the first value :")
y=input("enter the second value :")
if x.isnumeric() and y.isnumeric():
    a=int(x)
    b=int(y)    
    c=input("enter any opeartor")
    
    if c=='+':
        print(a+b)
    if c=='-':
        print(a-b)
    if c=='*':
        print(a*b)
    if c=='/':
        print(a/b)
elif x.isalpha() or y.numeric():
    print("both are not same")
    
else:
    print("this is an alphabet")


