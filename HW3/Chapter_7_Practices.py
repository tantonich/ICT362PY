# # 7-1 Rental Car
# car = input("What kind of rental car would you like? ")
# print("Let me see if I can find you a " + car.title())

# 7-2 Restaurant Seating
# party = input("How many people are in your dinner party? ")
# party = int(party)
# if party > 8:
#     print("You will need to wait for a table.")
# else:
#     print("We have a table for you.")

# 7-3 Multiples of ten
# number = input("Enter a number, and I will tell you if it's a multiple of 10: ")
# number = int(number)
# if number % 10 == 0:
#     print(str(number) + " is a multiple of 10.")
# else:
#     print(str(number) + " is not a multiple of 10.")

# 7-4 Pizza Toppings
# prompt = "What do you want on your pizza? "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# 7-5 Movie Tickets \BROKEN
# age = "What age are you? "
# if int(age) < 3:
#     cost = 0
# elif int(age) <= 12:
#     cost = 10
# else:
#     cost = 15
# print("Since you are " + str(age) + " years old, your movie price is $" + str(cost))

# 7-6 Three Exits
# prompt = "What do you want on your pizza? "

# while True:
#     message = input(prompt)
#     if message == 'quit':
#         break
#     else:
#         print(message)

# 7-7 Infinity
# x = 1
# while x <= 5:
#    print(x)

# 7-8 Deli
# sandwich_orders = ['grilled cheese', 'club', 'blt', 'ham and swiss']
# finished_sandwiches = []
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print("We are making your " + current_sandwich.title() + " sangwich now.")
#     finished_sandwiches.append(current_sandwich)
# print("\nThe following sangwiches have been made:")
# for sangwich in finished_sandwiches:
#     print(sangwich.title())

# 7-9 No Pastrami
# sandwich_orders = ['grilled cheese', 'pastrami', 'club','pastrami', 'blt','pastrami', 'ham and swiss']
# print("We don't have pastrami")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# print("\nThe following sangwiches have been made:")
# for sangwich in sandwich_orders:
#     print(sangwich.title())

# 7-10 Dream Vacation
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Where would you like to visit someday? ")
    # Store the response in the dictionary:
    responses[name] = response
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
    # Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to visit " + response + ".")