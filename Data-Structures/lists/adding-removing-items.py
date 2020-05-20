letters = ['a','b','c','d','e']

# Add
letters.append('Added Item one')
print(letters)

# Adding to Specifec index

letters.insert(0, 'Start of letter')

print(letters)

# Remove
# .pop removes by index
# .remove will remove by value
letters.pop(0)
print(letters)

letters.remove('d')