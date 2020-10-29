# file_path = r'D:\NMSU\2020_Fall\ICT362PY\HW4\Chapter10\text_files\pi_digits.txt'
# with open(file_path) as file_object:

# with open('text_files\pi_digits.txt') as file_object:
# 	contents = file_object.read()
# 	print(contents.rstrip())

filename = 'text_files\pi_digits.txt'
with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())