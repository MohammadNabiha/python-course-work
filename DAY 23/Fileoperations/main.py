'''file =open("PFS53.txt",'r')
print(file.readline())#reads a single line
file.seek(0)#to read the filr from start 
print(file.readlines())#read all lines
file.seek(0)
print(file.read())#reads the file
file.close() #for closing the file
'''

#second method--recommended---no need to close the file

'''with open("PFS53.txt",'r') as file:
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.seek(0)
    print(file.read())'''

#write operation on new file

'''with open("PFS54.txt",'w') as file:
    file.write("pratyusha")
    file.write("\npranaya")
    file.write("\namulya")'''

#write operation on existing file--over writes the new content

'''with open("PFS53.txt",'w') as file:
    file.write("pratyusha")
    file.write("\npranaya")
    file.write("\namulya")'''

#append

'''with open("PFS53.txt",'a') as file:
    file.write("pratyusha")
    file.write("\npranaya")
    file.write("\namulya")'''
#
'''with open("PFS53.txt",'r+') as file:
    file.write("pratyusha")
    file.write("\npranaya")
    file.write("\namulya")
    file.seek(0)
    print(file.read())


    

