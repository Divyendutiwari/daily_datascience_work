num=int(input("Enter a number to find Fibonacci series up to: "))
a=0
b=1
for i in range(num):
    print(b)
    a=b
    b=b+i
    i=b
    print(a)
    