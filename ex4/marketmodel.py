"""Modify the supermarket checkout simulator so that it simulates a store with 
many checkout lines. Add the number of cashiers as a new user input. At instantiation,
    the model should create a list of these cashiers. When a customer is generated,
    it should be sent to a cashier randomly chosen from the list of cashiers. 
On each tick of the abstract clock, each cashier should be told to serve its next 
customer. At the end of the simulation, the results for each cashier should be 
displayed.
"""

"""
File: marketmodel.py
"""
from cashier import Cashier
from customer import Customer
from random import randint

class MarketModel(object):
    def __init__(self, lengthOfSimulation, averageTimePerCus,
    probabilityOfNewArrival):
        self.probabilityOfNewArrival = probabilityOfNewArrival
        self.lengthOfSimulation = lengthOfSimulation
        self.averageTimePerCus = averageTimePerCus

        self.cashierAmount = int(input("Enter the number of cashiers: ")) #get user input for number of cashiers
        self.cashiers = [Cashier() for x in range(0, self.cashierAmount)] # create a list of cashiers
        
    def runSimulation(self):
        """Run the clock for n ticks."""
        for currentTime in range(self.lengthOfSimulation):
            # Attempt to generate a new customer
            customer = Customer.generateCustomer(
            self.probabilityOfNewArrival,
            currentTime,
            self.averageTimePerCus)
            
            # Send customer to cashier if successfully
            # generated
            if customer != None:
                cashier = randint(0, len(self.cashiers)-1) # randomly select a cashier
                currentCashier = self.cashiers[cashier]
                currentCashier.addCustomer(customer)
                
                # Tell cashier to provide another unit of service
                currentCashier.serveCustomers(currentTime)
        
        for i in range(self.cashierAmount):
            print(self.cashiers[i])
            print("")
        
    def __str__(self):
        return str(self.cashiers)
    
model = MarketModel(100, 5, 0.2)
model.runSimulation()

