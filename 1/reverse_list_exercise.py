'''
Write a program that prints a list on reverse
'''

my_list = [1,2,3,4,5,6,7,8,9]

idx = -1
list_idx = 0

while list_idx < len(my_list):
    print(my_list[idx])
    idx -= 1
    list_idx += 1
