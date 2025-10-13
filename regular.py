import re
pattern = r'\d+'
text='these are very bad 1234 numbers 5678'
matches = re.findall(pattern, text)
print(matches)
print(type(matches))
print(matches[0])
print(type(matches[0]))