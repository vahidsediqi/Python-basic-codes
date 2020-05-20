# how to sum the list values
# when we pass an * befor the argument the python will 
# compile this as an tuple
def sum(*list):
    total = 0
    for number in list:
        total += number
    return total

print(sum(10,10,10,10,10))

def multiply(*list):
    total = 1
    for number in list:
        total *= number
    return total

print(multiply(10,10,10,10,10))