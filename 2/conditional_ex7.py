'''
Write a program that counts the number of 'a'
in a DNA string
'''

# get data
dna = 'actgtcacatgta'
counter = 0

# write the solution
for character in dna:
    if character == 'a':
        counter += 1

print(counter)