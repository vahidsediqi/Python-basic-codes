# in python we have a build-in function that shows the address of a 
# variable in memori

x = 5
print("varible", id(x))
# if we update the value of x the memori id will be changed becouse integer is Immutable 


# but lists are mmutable 
lst = [1,2,5,5,8,9,9]

print(lst, id(lst))

# now list change the value
lst.append(100)

print(lst, id(lst))
# we see that the value us same