import unittest
from A.loan_calculator.annuity import AnnuityPayment

class TestAnnuityPayment(unittest.TestCase):
    def test_schedule_length(self):
        annuity = AnnuityPayment(loan_amount=1200000, annual_rate=12.0, term_years=1)
        schedule = annuity.calculate_schedule()
        self.assertEqual(len(schedule), 12)

    def test_total_payment(self):
        annuity = AnnuityPayment(loan_amount=1200000, annual_rate=12.0, term_years=1)
        schedule = annuity.calculate_schedule()
        total_paid = sum(row['payment'] for row in schedule)
        self.assertAlmostEqual(total_paid, 1200000 * 1.06, delta=10000)  # Примерная оценка

    def test_decreasing_balance(self):
        annuity = AnnuityPayment(1000000, 10.0, 1)
        schedule = annuity.calculate_schedule()
        balances = [row['remaining'] for row in schedule]
        self.assertTrue(all(x >= y for x, y in zip(balances, balances[1:])))
