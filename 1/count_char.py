'''
Write a program that counts the number of characters inside a string
'''

# string initialization
my_str = 'Hello World!'

# counter variable
str_len = 0

# let's count!
for char in my_str:
    str_len += 1 # is the same of str_len = str_len + 1

print(f'The lenght of the string is {str_len}')