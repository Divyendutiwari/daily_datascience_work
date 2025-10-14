import os
path='./likk.txt'
with open(path, 'r')as file:
    lines=file.readlines()
    lines_count=len(lines)
    print("number of lines:",lines_count)
    words_count=sum(len(line.split()) for line in lines)
    print("number of words:",words_count)
    char_count=sum(len(line) for line in lines)
    
   