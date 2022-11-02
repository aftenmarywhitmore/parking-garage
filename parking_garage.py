class parkingGarage():
    def __init__(self, tickets, parkingSpaces, currentTicket, licensePlate):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket
        self.licensePlate = licensePlate 
        
    
    def takeTicket(self):
        user = str(input('What is your license plate number? '))
        if self.tickets == []:
            print('Sorry, the garage is at capacity.')
        else:
            self.currentTicket[self.tickets[0]] = 'not paid'
            print(f'Your ticket number is {self.tickets[0]}')
            del self.tickets[0]
            del self.parkingSpaces[0]
            
         
    def payForParking(self):
        user = int(input('What is your ticket number? '))
        
        if user < 1 or user > 5:              
            print('This is not a ticket.')
        
        elif user not in self.currentTicket:
            print('Please enter a valid ticket number.')
        
        else:
            if self.currentTicket[user] == 'not paid':
                payment = input('Type "pay" to pay. ')
                self.currentTicket[user] = 'paid'
                print(self.currentTicket)        
            
                       
    def leaveGarage(self):
        user = int(input('What is your ticket number? '))
        
        if user not in self.currentTicket:
            print('Please enter a valid ticket number.')
        
        elif self.currentTicket[user] == 'Paid. You have 15 minutes to leave!':
            print('Come again soon!')
            self.tickets.insert(0, user)
            self.parkingSpaces.insert(0, user)
            del self.currentTicket[user]                
            self.tickets.sort()
            self.parkingSpaces.sort()
        
        elif self.currentTicket[user] == 'not paid':
            print('Please pay before leaving.')
      
        else:
            print('Please pay before leaving.')

def park():
        parking = parkingGarage([1,2,3,4,5], [1,2,3,4,5], {}, {})
        while True:
            user = input('Welcome. Would you like to park, pay, or leave? ')
            
            if user.lower() == 'park':
                parking.takeTicket()
                        
            elif user.lower() == 'pay':
                parking.payForParking()
                
            elif user.lower() == 'leave':
                parking.leaveGarage()
            
            elif user.lower() == 'quit':
                break
            
            else:
                print('Type a valid command.')

park()
