def square(n):
    for i in range(n):
        yield i * i
square(3)
for num in square(3):
    print(num)
a=square(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
