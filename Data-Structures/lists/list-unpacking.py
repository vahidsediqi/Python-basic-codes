number1 = list(range(3))
# it unpack out list in save them in sprat variable
first, second, third = number1
print(second)


# if we have so money items we can do like this
number2 = [1,2,5,2,3,5,8,6,5,9,5,7,5,6,5,8,5,6]
# can only stor some of them
a, b, c, *others = number2

print(others)
print(a)