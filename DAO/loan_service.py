from Utility.DBconn import DBconnection
from abc import ABC, abstractmethod
from MyExceptions.InvalidLoanException import InvalidLoanException

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


    
class LoanService(ILoanService,DBconnection):
    def applyLoan(self,Customer,Principal_Amount,Interest_Rate,Loan_Term,Loan_Type,Loan_Status):
        try:
            self.cursor.execute("""
            insert into loan values
            (?,?,?,?,?,?)""",
            (Customer,Principal_Amount,Interest_Rate,Loan_Term,Loan_Type,Loan_Status)
            )
            
            print("Enter 'YES' to confirm the loan: ")
            choice=input()
            if choice=='YES':
                self.conn.commit()
                print("successfully applied loan")
            else:
                print("Loan application Failed ❌")
        except Exception as e:
            print(e)

    def calculateInterest(self,Loan_ID):
        try:
            self.cursor.execute("""
            select  ((Principal_Amount * Interest_Rate * Loan_Term) / 12) as Interest_Amount from loan
            where Loan_ID= ? """,
            (Loan_ID))
            loan = self.cursor.fetchall()  # Get all data
            if len(loan) == 0:
                raise InvalidLoanException(Loan_ID)
            else:
                print(loan)
        except Exception as e:
            print(e)

    def loanStatus(self,Loan_ID):
        try:
            self.cursor.execute("""
            update Loan
            set Loan_Status='Approved'
            where loan_id = ? and 650<(select Credit_Score from Customer inner join
                                    loan on customer=customer_id
                                    where loan_id= ? )
            """,
            (Loan_ID ,Loan_ID))
            self.conn.commit()
            
        except Exception as e:
            print(e)
    def status(self,Loan_ID):
        try:
            self.cursor.execute("""
                                select Loan_status from loan
                                where loan_id =?""",Loan_ID)
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
            ,Loan_ID                    
            )
            loan = self.cursor.fetchall()  # Get all data
            if len(loan) == 0:
                raise InvalidLoanException(Loan_ID)
        except Exception as e:
            print(e)