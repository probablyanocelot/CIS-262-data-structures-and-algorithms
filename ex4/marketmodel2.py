"""
    In real life, customers do not choose a random cashier when they check out.
    They typically base their choice on at least the following two factors:
    
    a. the length of a line of customers waiting to check out.
    b. the physical proximity of a cashier.
    
    Modify the simulation of Project 5 so that it takes account of the first factor.
"""

"""
File: marketmodel2.py
"""
from cashier import Cashier
from customer import Customer

class MarketModel(object):
    def __init__(self, lengthOfSimulation, averageTimePerCus,
    probabilityOfNewArrival):
        self.probabilityOfNewArrival = probabilityOfNewArrival
        self.lengthOfSimulation = lengthOfSimulation
        self.averageTimePerCus = averageTimePerCus

        self.cashierAmount = int(input("Enter the number of cashiers: ")) #get user input for number of cashiers
        self.cashiers = [Cashier() for x in range(0, self.cashierAmount)] # create a list of cashiers
        
    def queueSelector(self):
        """
        Selects the index of the queue with the smallest number of items in it.
        """
        smallest_queue = None
        smallest_size = float('inf')
        
        for index, cashier in enumerate(self.cashiers):
            if len(cashier.queue) < smallest_size:
                smallest_size = len(cashier.queue)
                smallest_queue = index
        
        return smallest_queue
        
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
                cashier = self.queueSelector() # select the cashier with the smallest queue
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

