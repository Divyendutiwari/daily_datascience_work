s=input("give a sentence:")
words=s.split()
st=input("enter the word to find its frequency:")
i=0
for x in words:
    if x==st:
        i+=1
print(f"The frequency of the word '{st}' is: {i}")
    