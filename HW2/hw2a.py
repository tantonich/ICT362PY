######################################################################
# Software Requirement Document (SRD) 
# Assignemt: HW2a List Basics
# Author: Taylor Antonich
# 1. Create a list of 8 items.
# 2. Prints the list of 8 items as a column and without brackets
# 3. Prints a paragraph of text that access the list to print all of the elements of the list.
# 4. Access two elements of the list to modify them.
# 5. Uses the following:
#    1. insert() method to add one element to the middle of the list.
#    2. append() method to add one element to the end of the list.
#    3. del() method to remove the zeroth element of the array.
#    4. Prints a sentence as it uses the pop() method.
# 6. Removes an item of the list by name.
# 7. Sorts the list in ascending order.
# 8. Prints the list descending order (but the actual ascending order of the list is intact).
# 9. And includes a commented-out line that intends to access an element outside of the index scope. 
######################################################################
# Ref 1
foods = ['hamburger', 'pasta', 'french fries', 'pizza', \
'sushi', 'curry', 'chicken wings', 'salad']
# Ref 2
print(foods[0])
print(foods[1])
print(foods[2])
print(foods[3])
print(foods[4])
print(foods[5])
print(foods[6])
print(foods[7])
# Ref 3
print("Football parties are one of America's favorite activities. \n\
One of the most important parts of a football party is the food.\n\
The top five most popular football party foods are: \n\
1. "+foods[6].title()+"\n\
2. "+ foods[3].title()+"\n3. "+foods[0].title()\
+"\n4. "+foods[2].title()+"\n5. "+foods[7].title()+"\n\
The other favorite foods for Americans are "\
+foods[1].title()+", "+foods[4].title()+", and "+foods[5].title())
# Ref 4
foods[1] = 'chips and dip'
foods[5] = 'pretzle sticks'
# Ref 5.1
foods.insert(4, 'cookies')
# Ref 5.2
foods.append('veggie snacks')
# Ref 5.3
del foods[-2]
# Ref 5.4
print("Another fan favorite that are underrated are "+foods.pop().title()+".")
# Ref 6
foods.remove('sushi')
# Ref 7
foods.sort()
# Ref 8
print(sorted(foods, reverse=True))
# Ref 9
print(len(foods))
# foods[8] = 'nachos'