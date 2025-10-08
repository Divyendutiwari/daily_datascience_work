lst=list(range(1,21))
print(lst, end=" ");
print(lst[0])
popped=lst.pop()
print(popped)
print(lst[len(lst)//2+1])
print(lst[:5])
print(lst[5:16])
print(lst[-5:])
list=[3,5,7,9]
square=[x**2 for x in list]
print(square)

kl=[x for x in lst if x%2==0]
print(kl)
lst.sort()
print(lst)
lst.reverse()
print(lst)