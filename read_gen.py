def read_file(path):
    with open(path, 'r') as file:
        for line in file:
            yield line.strip()
path='d:/anaconda program/Advanced Python/sample.txt'
for line in read_file(path):
    print(line)
