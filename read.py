import os
import sys
import re
path='./example.txt'
with open(path, 'r')as file:
    content=file.read()
    print(content)