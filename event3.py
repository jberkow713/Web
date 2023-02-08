class Event: 
    def __init__(self):
        self.__eventhandlers = []
 
    def __iadd__(self, handler):
        self.__eventhandlers.append(handler)
        # kind of optional return here
        return self
 
    def __isub__(self, handler):
        self.__eventhandlers.remove(handler)
        return self
 
    def __call__(self, *args, **keywargs):
        for event in self.__eventhandlers:
            event(*args, **keywargs)

                 
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
         
# LockClass
 
class Lock(object):
     
    def __init__(self):
        self.IfLockBroken = Event()
         
    def LockBroken(self):
        #the same as self.IfLockBroken() 
        self.IfLockBroken.__call__(11,'James', '5:30pm')
         
    def AddEvent(self,Method):
        self.IfLockBroken += Method
         
    def RemoveEvent(self,Method):
        self.IfLockBroken -= Method
 
def Simulation():
         
    # Required objects
    godrejLockObj = Lock()
    PoliceObj = Police(911)
    ownerObj = Owner(99999999)
    AlarmObj = Alarm()
     
    # Setting these objects to receive the events from lock
    godrejLockObj.AddEvent(PoliceObj.Call_Police)
    godrejLockObj.AddEvent(ownerObj.Message)
    godrejLockObj.AddEvent(AlarmObj.Start_Alarm)
    
    godrejLockObj.LockBroken()       
    godrejLockObj.RemoveEvent(AlarmObj.Start_Alarm)

Simulation()    