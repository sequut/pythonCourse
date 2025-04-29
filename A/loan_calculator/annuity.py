from A.loan_calculator.base import LoanBase, PaymentSchedule

class AnnuityPayment(LoanBase, PaymentSchedule):
    def calculate_schedule(self):
        r = self.monthly_rate
        n = self.term_months
        P = self.loan_amount

        monthly_payment = P * r * (1 + r)**n / ((1 + r)**n - 1)
        balance = P
        schedule = []

        for month in range(1, n + 1):
            interest = balance * r
            principal = monthly_payment - interest
            balance -= principal
            balance = max(balance, 0)

            schedule.append({
                'month': month,
                'payment': round(monthly_payment, 2),
                'interest': round(interest, 2),
                'principal': round(principal, 2),
                'remaining': round(balance, 2)
            })
        return schedule
