class InvalidLoanException(Exception):
    def __init__(self, Loan_ID):
        super().__init__(f"Director with {Loan_ID} is not found")