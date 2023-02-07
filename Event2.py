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

def function_3(*args):
    print(f'{args[0]}:{args[1]} has been added to user database')

class Register:
    def __init__(self, event, funcs):
        self.event = event
        self.funcs = funcs
    def register(self):
        for func in self.funcs:
            register_event(self.event,func)
    def add(self, func):
        self.funcs.append(func)
    def dispatch(self,  *args):
        dispatch(self.event,*args)
        
H = Register('register_user', [create_user,function_2])
H.add(function_3)
H.register()
H.dispatch(['John', 'Doe', 'extra_1', 'extra_2'])

H2 = Register('share_info', [share_password])
H2.register()
H2.dispatch(['Peter', 'password'])



 