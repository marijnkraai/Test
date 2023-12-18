'''
Write a program that given two strings, it prints
all the pairs (a,b), where a is an elements of the
first string and b is an element of the second
string.

Example
str1 = 'abc'
str2 = '123'

result = (a,1), (a,2), (a,3)...(c,3)
'''

# creation of the string
str1 = 'abc'
str2 = '123'

# printing the pairs
'''for element1 in str1:
    for element2 in str2:
        print(element1,element2)'''

idx = 0
idx2 = 0


'''while idx < len(str1):
    idx2 = 0
    while idx2 < len(str2):
        print(str1[idx],str2[idx2])
        idx2 += 1
    idx += 1'''

while idx < len(str1):
    for element in str2:
        print(str1[idx],element)
    idx += 1