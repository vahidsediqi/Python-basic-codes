name = "Vahid Sediqi"
print(name[0])
print("")

# prints from 0 index to 4 index
print(name[0:5])

# if we dont mention the first index it puts it 0
# if we don't mention last index it puts the -1

print(name[:5])
print(name[0:])


# -1 take as to the end of the string
print(name[-1])


# to display \ in out string we should use \\ back slash
message ='Python Programming \\ language '

print(message)

# we can triple quotes in python for multi line string
print("\n")

details = """This is a python course for developers
with a Django library and some projects  
"""

print(details)

# Formatted Strings
firstname = "Vahid"
lastname = "Sediqi"
full = firstname + ' ' + lastname

# we can do like

fullname = f"{firstname} {lastname}"
print(fullname)

