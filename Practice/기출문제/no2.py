# Given list
my_list = ['H', 'e', 'l', 'l', 'o', ',', ' ', 'I', 'o', 'T']

# A. Add '!' to the end of the list and print
my_list.append('!')
print("A:", my_list)

# B. Remove the fifth element ('o') and print
my_list.pop(4)
print("B:", my_list)

# C. Insert 'a' at index 4 and print
my_list.insert(4, 'a')
print("C:", my_list)

# D. Convert the list to a string and print
as_string = ''.join(my_list)
print("D:", as_string)

# F. Sort the list in descending order and print
desc_sorted_list = sorted(my_list, reverse=True)
print("F:", desc_sorted_list)