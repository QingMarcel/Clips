"""
This program opens, process and 
close the files 
"""

doc_file = open('my_friends.doc','w')

doc_file.write(input("Enter your friend's name: ")+"\n")
doc_file.write(input("Enter another friend's name: ")+"\n")
doc_file.write(input("Enter another friend's name: ")+"\n")
doc_file.write(input("Enter another friend's name: ")+"\n")
doc_file.close()

#The Code below is to read the information from the file created.
print()
print("The names in the file you've created are listed below")
file =  open('my_friends.doc', 'r')
names = file.read()
file.close()
#print the names in the file
print(names.upper())