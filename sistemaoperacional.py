import os
cwd = os.getcwd()
print(cwd)
print(os.path.abspath('output.txt'))
print(os.path.exists('output.txt'))
print(os.path.isfile('output.txt'))
print(os.path.isdir('D:\workspace\Python\PensePython'))
for file in os.listdir(cwd):
    if 'py' not in file:
        print(file)
