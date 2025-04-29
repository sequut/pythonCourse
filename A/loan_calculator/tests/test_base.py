import unittest
from A.loan_calculator.base import LoanBase

class DummyPayment(LoanBase):
    def calculate_schedule(self):
        return [{"month": 1, "payment": 1000, "interest": 100, "principal": 900, "remaining": 0}]

class TestPaymentBase(unittest.TestCase):
    def test_base_schedule(self):
        dp = DummyPayment(10000, 5, 1)
        schedule = dp.calculate_schedule()
        self.assertEqual(schedule[0]['payment'], 1000)
