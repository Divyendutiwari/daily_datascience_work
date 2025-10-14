##to read a file
with open('example.txt', 'r') as file:
    content=file.read()
    print(content)
##to write a file
with open('example.txt', 'a') as file:
    file.write('\nhello world')

    