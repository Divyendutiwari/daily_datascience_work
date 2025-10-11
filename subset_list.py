lst1=[2,5,6,67,4,43,2,5,3,3]
lst2=[2,5,6,67,4,43,2,5,3,3,72,667,3435]
se1=set(lst1)
se2=set(lst2)
if se1.issubset(se2):
    print("list1 is subset of list2")
else:
    print("list1 is not subset of list2")
if se2.issubset(se1):
    print("list2 is subset of list1")
else:
    print("list2 is not subset of list1")