'''
Write a program that prints the first position at which
a given element occurs in a list
'''

# get the data
input_list = [0,1,2,3,4,2]
idx = 0
ets = 2

# write the solution
while idx < len(input_list):
    if ets == input_list[idx]:
        print(idx)
        break
    idx += 1
    
# reset the index
idx = 0
for element in input_list:
    if ets == element:
        print(idx)
        break
    idx += 1
