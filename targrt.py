axe=[3,4,7]
zig=[]
target=7
for i in range(len(axe)):
    for j in range(len(axe)):
        if axe[i]+axe[j]==target:
            zig.append((i,j))
            break
print(zig)