"""
File: cashier.py
"""
from linkedqueue import LinkedQueue

class Cashier(object):
    
    def __init__(self):
        self.totalCustomerWaitTime = 0
        self.customersServed = 0
        self.currentCustomer = None
        self.queue = LinkedQueue()
        
    def addCustomer(self, c):
        self.queue.add(c)
        
    def serveCustomers(self, currentTime):
        
        if self.currentCustomer is None:
            # No customers yet
            if self.queue.isEmpty():
                return
            else:
                # Pop first waiting customer
                # and tally results
                self.currentCustomer = self.queue.pop()
                self.totalCustomerWaitTime += \
                currentTime - \
                self.currentCustomer.getArrivalTime()
                self.customersServed += 1
                
        # Give a unit of service
        self.currentCustomer.serve()
        
        # If current customer is finished, send it away
        if self.currentCustomer.getAmountOfServiceNeeded() == 0:
            self.currentCustomer = None
            
    def __str__(self):
        result = "TOTALS FOR THE CASHIER\n" + \
            "Number of customers served: " + \
            str(self.customersServed) + "\n"
            
        if self.customersServed != 0:
            aveWaitTime = self.totalCustomerWaitTime / self.customersServed
                    
        result += "Number of customers left in queue: " + \
            str(len(self.queue)) + "\n" + \
            "Average time customers spend\n" + \
            "waiting to be served: " + \
            "%5.2f" % aveWaitTime
        
        return result