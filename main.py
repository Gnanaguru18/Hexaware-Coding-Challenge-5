import pyodbc
from datetime import date
from abc import ABC,abstractmethod

server_name = "TIGGER\\SQLEXPRESS"
database_name = "Loan_Management_System"
 
 
conn_str = (
    f"Driver={{SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"Trusted_Connection=yes;"
)

print(conn_str)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute("Select 1")
print("Database connection is successful")

class ILoanService(ABC):
    @abstractmethod
    def applyLoan(self):
        pass

    @abstractmethod
    def calculateInterest(self):
        pass

    @abstractmethod
    def loanStatus(self):
        pass

    @abstractmethod
    def calculateEMI(self):
        pass

    @abstractmethod
    def loanRepayment(self):
        pass

    @abstractmethod
    def getAllLoan(self):
        pass

    @abstractmethod
    def getLoanById(self):
        pass


    
class LoanService:
    def applyLoan(self,Customer,Principal_Amount,Interest_Rate,Loan_Term,Loan_Type):
        try:
            self.cursor.execute("""
            insert into loan values
            (?,?,?,?,?)""",
            (Customer,Principal_Amount,Interest_Rate,Loan_Term,Loan_Type))
            print("Enter 'YES' to confirm the loan: ")
            choice=input()
            if choice=='YES':
                self.conn.commit()
            else:
                print("Loan application Failed ❌")
        except Exception as e:
            print(e)

    def calculateInterest(self,Customer):
        try:
            self.cursor.execute("""
            select  ((Principal_Amount * Interest_Rate * Loan_Term) / 12) as Interest_Amount from loan
            where Customer= ? """,
            (Customer))
            for director in self.cursor:
                print(director)
        except Exception as e:
            print(e)

    def loanStatus(self,Loan_ID):
        try:
            self.cursor.execute("""
            update Loan
            set Loan_Status='Approved'
            where loan_id = 2 and 650<(select Credit_Score from Customer inner join
                                    loan on customer=customer_id
                                    where loan_id= ? )""",
            Loan_ID )
            self.conn.commit()
            self.cursor.execute(""" 
            select Loan_status from loan
            where Loan_ID =?""")

            for director in self.cursor:
                print(director)
        except Exception as e:
            print(e)
        
    def calculateEMI(self,Customer):
        try:
            self.cursor.execute("""
            select ((Principal_Amount*(Interest_Rate/12/100)*power((1+(Interest_Rate/12/100)),Loan_term)) / (power((1+(Interest_Rate/12/100)),Loan_term-1))) as EMI from loan
            where customer= ?
             """,Customer
            )
            for director in self.cursor:
                print(director)
        except Exception as e:
            print(e)

    def loanRepayment(self):
        pass

    def getAllLoan(self):
        try:
            self.cursor.execute("""
            select * from loan """
            )
            for director in self.cursor:
                print(director)
        except Exception as e:
            print(e)

    def getLoanById(self,Loan_ID):
        try:
            self.cursor.execute("""
            select * from loan
            where Loan_ID =?"""
            )
            for director in self.cursor:
                print(director)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    loan_service=LoanService()

    while True:
        print("""
        1. Apply Loan
        2. Get Loan status      
        3. exit      
              """)
        choice=int(input("Enter Your choice:"))
        if choice == 1:
            Customer=int(input("Enter customer id:"))
            Principal_Amount=int(input("Enter principal amount:"))
            Interest_Rate=int(input("Enter interst rate:"))
            Loan_Term=int(input("Enter tenure in months:"))
            Loan_Type=input("Enter loan type:")
            loan_service.applyloan(Customer,Principal_Amount,Interest_Rate,Loan_Term,Loan_Type)
            print("Interest Amount:")
            loan_service.calculateInterest(Customer)

        if choice == 2:
            Loan_ID=int(input("Enter loan id:"))
            loan_service.loanStatus(Loan_ID)
        
        if choice == 3:
            break
