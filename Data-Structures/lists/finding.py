letters = ['a','b','c','d','e']

# finding index of an item
# if the item is not in the the we get error
# to solve it we have to use if statment
print(letters.index('d'))

if 'f' in letters:
    print(letters.index('f'))
else:
    print('The letter is not exist')