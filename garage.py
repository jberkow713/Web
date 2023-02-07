from random import choice

class Garage:
    def __init__(self):
        self.types = ['compact', 'luxury']
        self.spots = self.build_garage()
        
    def build_garage(self):
        Rows = 10
        Count = 0
        garage = []
        for i in range(Rows):
            Row = []
            for x in range(10):
                ticket = (Ticket(choice(self.types)),Count)                 
                Row.append(ticket)
                Count +=1
            garage.append(Row)
        return garage
        
class Ticket:
    def __init__(self, type):
        self.type = type
        self.open =True  

G = Garage()

class Customer:
    def __init__(self,garage,type):
        self.garage = garage
        self.type = type
        self.open_spots = self.find_openings() 
    def find_openings(self):
        Open = []

        for row in self.garage.spots:
            for spot in row:
                # (<__main__.Ticket object at 0x0000029D59E9A308>, 0)
                if spot[0].type == self.type:
                    if spot[0].open==True:
                        Open.append(spot[1])
        return Open
    def reserve(self,num):
        if num in self.open_spots:
            for row in self.garage.spots:
                for spot in row:
                    if spot[1]==num:
                        if spot[0].open==True:
                            spot[0].open=False
                            print(f'Spot {num} has been reserved')
                            return 
        print('Can not reserve this spot')

c = Customer(G,'compact')
c.reserve(5)

                    



