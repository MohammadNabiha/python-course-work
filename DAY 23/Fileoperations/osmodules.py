import os
import shutil

os.mkdir('sample')#for creating folder

os.rmdir('sample')#for removing folder which is empty
os.mkdir('sample')

os.makedirs('sample/demo')#for creating folder inside folder

shutil.rmtree('sample')#for removing folder which is not empty

print(os.getcwd())#to get the path of folder

print(os.listdir())#to get the list of folders
os.chdir('../')#to change the directory

print(os.getcwd())
print(os.listdir())

