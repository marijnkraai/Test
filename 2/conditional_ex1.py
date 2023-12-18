'''
Write a program that checks if a word is inside a list
of words and prints True.
'''

# define the word to search
wts = 'hello'

# define the list of words
words = ['banana','hello','smartphone','bottle','Pippo']

# define the variable that contains the result
result = False

# Solution 1
result = wts in words
print(result)

# reset the variable
result = False

# Solution 2
for word in words:
    if wts == word:
        result = True
        break

print(result)

# reset the variable
result = False

# Solution 3
idx = 0
while idx < len(words):
    if wts == words[idx]:
        result = True
        break
    idx += 1

print(result)

