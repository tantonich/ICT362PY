# Welcome the user to Zion's Pizza Restaurant 
# and ask the user how many people are in their dinner group.
party = input("How many people are in your dinner party? ")
party = int(party)

# If the answer is more than eight (8), print a message saying they'll have to
# wait for a table.  Otherwise, report that their table is ready 
# and take their order.
if party > 8:
    print("You will need to wait for a table.")
else:
    print("We have a table for you.")

# Assume the client orders one pizza, 
# and ask what he/she would like on their pizza, 
# include a loop that prompts the user to enter a series of pizza toppings
# until they enter a quit value.
prompt = "\nWhat do you want on your pizza? "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print("I'll add " + message + " to your pizza!")

# Make a list called sandwich_orders
# and fill it with the names of various sandwiches.
sandwich_orders = ['grilled cheese', 'club', 'blt', 'ham and swiss']

# Make an empty list called finished_sandwiches.
finished_sandwiches = []

# Loop through the list of sandwich orders and
# spring a message for each order such as "I am working on your tuna sandwich"
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("We are making your " + current_sandwich.title() + " sandwich now.")

    # As each sandwich is made, move it to the list of finished sandwiches.
    finished_sandwiches.append(current_sandwich)

# After all the sandwiches have been made, 
# print a message listing each sandwich that was made.    
print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich.title())