class Event:
    def __init__(self):
        self.Events = {}

    def add(self, event,func):
        e = self.Events.get(event)        
        if e == None:
            self.Events[event]=[func]
        else:
            self.Events[event].append(func)

    def sub(self, event,func):
        e = self.Events.get(event)

        if e ==None:
            print('No event to remove')
            return
        else:
            if func in self.Events[event]:
                self.Events[event].remove(func)
                print(f'{func} was removed')
                return
            else:
                print("function not found")

    def remove_entire_event(self, event):
        if self.Events.get(event)==None:
            print('nothing to remove')
        else:
            del self.Events[event]

    def run(self,event,*args):
        if self.Events[event]==None:
            print('Nothing to run')
            return

        for e in self.Events[event]:
            e(*args)

class Police:
    def __init__(self, phone):
        self.phone = phone
     
    def Call_Police(self,*args):
        num = [x for x in args if type(x)==int ]
        print (f"{self.phone} has been called, police have been informed {num[0]} times")

class Owner:
    def __init__(self, phone):
        self.phone = phone
     
    def Message(self,*args):
        name = [x for x in args if type(x)==str and x.isalpha()==True]        
        print (f"We are calling {self.phone}, is this {name[0]}? There has been a possible theft")

class Alarm:
     
    def Start_Alarm(self,*args):
        time = [x for x in args if type(x)==str and x.isalpha()==False]
        print (f"Alarm has started at {time[0]}")

class Lock:
    def __init__(self):
        self.LockBroken  = Event()
    def add(self, name, func):
        self.LockBroken.add(name, func)
    def sub(self, name, func):
        self.LockBroken.sub(name,func)
    def LockBroken(self,name,*args):
        self.LockBroken.run(name,*args)

def Simulation():
         
    # Required objects
    LockObj = Lock()
    PoliceObj = Police(911)
    ownerObj = Owner(99999999)
    AlarmObj = Alarm()
     
    # Setting these objects to receive the events from lock
    LockObj.add('broken', PoliceObj.Call_Police)
    LockObj.add('broken',ownerObj.Message)
    LockObj.add('broken',AlarmObj.Start_Alarm)
    
    LockObj.LockBroken.run('broken',11,'James', '5:30pm')       
    LockObj.sub('broken',AlarmObj.Start_Alarm)

Simulation()    