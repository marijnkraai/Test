'''
Write a program that checks if a number is prime, and
prints True if so
'''

# get the data
n = 1
isPrime = True


# write the solution
if n > 1:
    for number in range(2,n):
        if n%number == 0:
            isPrime = False
            break
else:
    isPrime = False
    
print(isPrime)