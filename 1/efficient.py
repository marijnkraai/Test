'''
write a program that prints the sum of the first
n numbers

In this file, we see the difference between efficiency and effectiveness
'''
n = 100000000000000000000000000000000000000000000000000
result = 0
n_range = range(1,n)

#for number in n_range:
 #   result = result + number

result = (n * (n+1))/2

print(result)