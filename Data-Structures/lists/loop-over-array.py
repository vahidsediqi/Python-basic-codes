letters = ['a','b','c','d','e']

for i in letters:
    print(i)

print('displaying enumerate opject')
# enumerate display the each array and also there indexes
# if we print letter[0] we get only the indexes
for letter in enumerate(letters):
    print(letter)
    print(letter[0])
