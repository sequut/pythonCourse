from A.loan_calculator.base import LoanBase, PaymentSchedule

class DifferentiatedPayment(LoanBase, PaymentSchedule):
    def calculate_schedule(self):
        P = self.loan_amount
        n = self.term_months
        r = self.monthly_rate

        principal_part = P / n
        balance = P
        schedule = []

        for month in range(1, n + 1):
            interest = balance * r
            payment = principal_part + interest
            balance -= principal_part
            balance = max(balance, 0)

            schedule.append({
                'month': month,
                'payment': round(payment, 2),
                'interest': round(interest, 2),
                'principal': round(principal_part, 2),
                'remaining': round(balance, 2)
            })
        return schedule
