# when we put 2 starts befor an arguments in function
# python will comile that as a dictionary
def save_user(**user):
    print(user)

save_user(id=1, name="Vahid", email="vahid.sediqi@gmail.com")