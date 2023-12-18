'''
Given a string, replace it's first element
'''

# string creation
my_string = 'Hello'
my_list = []

for element in my_string:
    my_list.append(element)

my_list[0] = 'C'

new_string = ''

for element in my_list:
    new_string = new_string + element

print(new_string)
