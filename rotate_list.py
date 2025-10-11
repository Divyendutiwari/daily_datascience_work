lst1=[1,2,3,4,5]
i=int(input("enter no. of times to rotate the list:"))
k=len(lst1)
lst2=lst1[k-i:k]+lst1[0:k-i]
print("rotated list is:",lst2)
    