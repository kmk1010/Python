def fun1(a,b):
    if a * b > 1000:
        print(a+b)
        return a + b
    else:
        print(a*b)
        return a * b

a=int(input("enter first number"))
b=int(input("enter second number"))
fun1(a,b)


