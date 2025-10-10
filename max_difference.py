lst=[33,5,4,5,43,3,2,43,1,3,335,334,2,4,56,7,8,8]

maxi=max(lst)
print("maximum no. in the list is:",maxi)
t=len(lst)
diff=[]
for x in range(t):
    y=x+1
    if x==len(lst)-1:
        break
    z=lst[y]-lst[x]
    if z<0:
        z=-z
    diff.append(z)
max_consicutive_diff=max(diff)
print("maximum consicutive difference is:",max_consicutive_diff)