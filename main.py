from DAO import LoanService,CustomerService
from Entity import customer,loan

"""
Question number a, c , d all comes under choice 1 according to the question
"""


if __name__ == "__main__":
    loan_service=LoanService()
    customer_service=CustomerService()

    while True:
        print("""
        1. Apply Loan
        2. Get Loan status 
        3. loanRepayment     
        4. Get All Loan
        5. Get Loan by ID
        6. Exit
              """)
        choice=int(input("Enter Your choice:"))
        if choice == 1:
            Customer=int(input("Enter customer id:"))
            Principal_Amount=int(input("Enter principal amount:"))
            Interest_Rate=int(input("Enter interst rate:"))
            Loan_Term=int(input("Enter tenure in months:"))
            Loan_Type=input("Enter loan type (HomeLoan or CarLoan):")
            Loan_Status='Pending'
            loan_service.applyLoan(Customer,Principal_Amount,Interest_Rate,Loan_Term,Loan_Type,Loan_Status)
            loan_service.getAllLoan()
            Loan_ID=int(input("Enter loan id:"))
            print("Interest Amount:")
            loan_service.calculateInterest(Loan_ID)
            print("EMI :")
            loan_service.calculateEMI(Customer)

        if choice == 2:
            Loan_ID=int(input("Enter loan id:"))
            loan_service.loanStatus(Loan_ID)
            loan_service.status(Loan_ID)
        
        if choice == 3:
            loan_service.loanRepayment()
        if choice == 4:
            loan_service.getAllLoan()

        if choice == 5:
            Loan_ID=int(input("Enter loan id:"))
            loan_service.getLoanById(Loan_ID)

        if choice == 6:
            loan_service.close()
            customer_service.close()
            break
