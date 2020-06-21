# Python has functions for creating, reading, updating, and deleting files.

myFile = open('myFile.json','w')


print('Name: ',myFile.name)
print('Is Closed : ',myFile.closed)
print('Opening Mode: ',myFile.mode)


person = 'kaushal'

#write file
myFile.write(person)
myFile.close()


myFile = open('myFile.json','a')
myFile.write(' I like php')
myFile.close()
