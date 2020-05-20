# Lambada passing a function as an arrgument
items = [
    ("Product1", 10),
    ("Product2", 11),
    ("Product3", 8),
    ("Product4", 7),
    ("Product5", 6)
]

# items.sort(key=lambda item: item[1])
# print(items)

# prices = []

# for item in items:
#     prices.append(item[1])

# the easy way

prices = list(map(lambda item: item[1], items))
print(prices)