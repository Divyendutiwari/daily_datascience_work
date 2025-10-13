import json
data={'name': 'John', 'age': 30, 'city': 'New York'}
string_data = json.dumps(data)
print(string_data)
print(type(string_data))
parsed_data = json.loads(string_data)
print(parsed_data)
print(type(parsed_data))