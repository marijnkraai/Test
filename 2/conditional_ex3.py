'''
Write a program that counts the number of
occurencies of an element inside a list
'''

# data needed for the solution
in_list = [0,0,0,1,2,3,4,5,5,5,5,]
counter = 0
wts = 33

# solution
for element in in_list:
    if element == wts:
        counter += 1
print(f'The element {wts} appears {counter} times in the list')