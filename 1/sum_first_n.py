'''
Write a program that performs the sum of the first n
numbers. 
Ex:
n = 4
result = 0 + 1 + 2 + 3 
'''

# storing the value for n
n = range(4)

# variable containing the result
result = 0

for number in n:
    result = result + number

    print(result)