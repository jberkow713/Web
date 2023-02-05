from event_systems import *

Users = []

class User:
    def __init__(self, name, password):
        self.name=name
        self.password=password
        
    def save(self):
        Users.append(self)
        for x in Users:
            print(x)

    def __str__(self):
        return f'name:{self.name}, password:{self.password}'             

def create_user(*args):
    name = args[0]
    password=args[1]
    User(name,password).save()

def function_2(*args):
    print(args)

def share_password(*args):
    password=args[1]
    friend = args[0]
    print(f'Sharing password {password} with {friend}')

register_event('register_user', create_user)
register_event('register_user', function_2)
register_event('share_info', share_password)

# Dispatch calls the Dictionary and all functions in it, and runs the individual functions, with the given
# Arguments, so in this case, 'register user' has 2 functions associated with it, and both are run 
# with the arguments passed to build_users
def build_users(*args):
    dispatch('register_user', args)

def share_info(*args):
    dispatch('share_info', args )   


build_users('John', 'Doe', 'extra_1', 'extra_2')
share_info('Peter', 'password')

 