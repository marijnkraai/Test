'''
Write a program that prints all the numbers
between 0 and 10 except the number 3
'''

# get the data
numbers = range(10)

# write the solution
for num in numbers:
    if num == 3:
        continue
    else:
        print(num)