import os
path='D:\anaconda program\modulespackages\new_directory'
dir_list=os.listdir(path)
print("Files and directories in '", path, "' :")
print(dir_list)
with open('sample.txt', 'w') as fp:
    f.write("This is a sample file.")
print("File created successfully.")
dir_list_new=os.listdir(path)
print("Updated list of files and directories in '", path, "' :")
print(dir_list_new)