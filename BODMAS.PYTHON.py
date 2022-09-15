x=input("enter the first value :")
y=input("enter the second value :")
if x.isnumeric() and y.isnumeric():
    a=int(x)
    b=int(y)    
    c=input("enter any opeartor")
    
    if c=='+':
        print(a+b)
    elif c=='-':
        print(a-b)
    elif c=='*':
        print(a*b)
    elif c=='/':
        print(a/b)
elif x.isalpha() and y.isalpha():
    print("both are alphabets ")
else:
    print("both are not same")


