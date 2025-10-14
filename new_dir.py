import os
new_directory='new_folder'
os.makedirs(new_directory)
print(f"Directory '{new_directory}' created successfully.")
items = os.listdir('.')
print("Contents of the current directory:")
print(items)
print(type(items))