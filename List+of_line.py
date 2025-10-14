lines=['\nfirst line\n','second line\n','third line\n']
with open('example.txt','a')as file:
    file.writelines(lines)