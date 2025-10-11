lst=[3,54,56,7,3,3,2,2,4,5,6,78,8,9,9,7,65]
i=0
j=len(lst)
for x in lst:
    if x%2==0:
        i+=1
print("no. of even no.in tne list is:",i)
t=j-i
print("no. of odd no.in the list is:",t)