######################################################################
# Software Requirement Document (SRD) 
# Assignemt: HW4c
# Author: Taylor Antonich
# 1. Write a python program that reads the hw4c.txt file that
#	 prints what you wrote once by reading in the entire file. 
# 2. Modify your Python program so it also includes code that
#	 reads the hw4c.txt file to print what you wrote once
#	 by looping over the file object.  
# 3. Modify your Python program so it also includes code that
#	 reads the hw4c.txt file to print what you wrote once
#	 by storing the lines in a list
#	 and then working with them outside the with block.
# 4. Have your hw4c.py file include code that
#	 prompts the user for their name after the printing in the steps above.
# 5. When the user responds, store their name in a file called hw4c_guest.txt.
######################################################################
# Setting the file variable
filename = 'hw4c.txt'
# Ref.1
print("--- Reading the entire file:")
with open(filename) as file_object:
	contents = file_object.read()
	print(contents.rstrip())

# Ref.2
print("\n--- Looping over the lines:")
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

# Ref.3
print("\n--- Storing the lines in a list:")
with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())

# Ref.4
username = input("Enter you first name: ")
# Ref.5
output_file = 'hw4c_guest.txt'
with open(output_file, 'w') as file_object:
	file_object.write(username.title())