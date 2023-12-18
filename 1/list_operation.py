'''
Operations on Lists

Add elements to a list
'''

# List creation
mangas = []


# Appending an element
mangas.append('Jojo')
mangas.append('Ghost in The Shell')

# Inserting an element
mangas.insert(0,'Trigun')

print(mangas)


'''
Remove elements from a list
'''

# Remove an element
del mangas[1]
print(mangas)

# Popping the element
popped_element = mangas.pop(0)
print(mangas)
