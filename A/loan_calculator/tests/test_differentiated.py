import unittest
from A.loan_calculator.differentiated import DifferentiatedPayment

class TestDifferentiatedPayment(unittest.TestCase):
    def test_schedule_length(self):
        diff = DifferentiatedPayment(600000, 10, 2)
        schedule = diff.calculate_schedule()
        self.assertEqual(len(schedule), 24)

    def test_interest_decreases(self):
        diff = DifferentiatedPayment(600000, 10, 1)
        schedule = diff.calculate_schedule()
        interests = [row['interest'] for row in schedule]
        self.assertTrue(all(x >= y for x, y in zip(interests, interests[1:])))
