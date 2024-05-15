from Utility.DBconn import DBconnection
from abc import ABC, abstractmethod
from MyExceptions.InvalidLoanException import InvalidLoanException
class ICustomerService(ABC):
    @abstractmethod
    def dispalycustomer(self):
        pass

class CustomerService(ICustomerService,DBconnection):
    def dispalycustomer(self):
        try:
            self.cursor.execute("""
            select * from Customer
             """
            )
            for cusomer in self.cursor:
                print(cusomer)
        except Exception as e:
            print(e)