'''
Write a program that analyses a list of numbers,
and creates 2 other lists, one for even numbers
and one for odd numbers belonging to the input list
'''

# creation of the input list
in_list = [0,1,2,3,4,5]

# creation of the new lists
even_list = []
odd_list = []

# solve the problem!
for element in in_list:
    # check if even or odd
    if element%2 == 0:
        even_list.append(element)
    else:
        odd_list.append(element)

print(even_list)
print(odd_list)
