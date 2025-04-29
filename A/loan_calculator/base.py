from abc import ABC, abstractmethod

class LoanBase:
    def __init__(self, loan_amount, annual_rate, term_years):
        self.loan_amount = loan_amount
        self.annual_rate = annual_rate
        self.monthly_rate = annual_rate / 12 / 100
        self.term_months = term_years * 12


class PaymentSchedule(ABC):
    @abstractmethod
    def calculate_schedule(self):
        pass
