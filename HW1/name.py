name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

message = "Hello, " + full_name.title() + "!"
print(message)

print("\tpython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavascript")

# stripping white space from right side
favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())

# change the variable to remove right white space
favorite_language = favorite_language.rstrip()
print(favorite_language)

# stripping white space from left side
favorite_language = ' python'
print(favorite_language)
print(favorite_language.lstrip())

# stripping all white space from left and right sides
favorite_language = ' python '
print(favorite_language)
print(favorite_language.strip())

