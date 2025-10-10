dic=[{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]
result = {}
if isinstance(dic, list):
    for d in dic:
        if isinstance(d, dict):
            for key, value in d.items():
                if key in result:
                    result[key] += value
                else:
                    result[key] = value
print(result)