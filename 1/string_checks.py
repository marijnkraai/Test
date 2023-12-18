'''
Write a program that asks the input to a user, and prints it on the screen.
if the user types 'quit', the program ends.
'''

# this is the prompt to show to the user
prompt = "Tell me something, I will print it back! "

# variable for storing the user input
usr_input = ""

    # get the input from the user
while usr_input != 'quit':

    usr_input = input(prompt)

    # print the message on the screen
    print(usr_input)