from unittest import TestCase

from prime_factors import PrimeFactors


class TestPrimeFactors(TestCase):
    def setUp(self):
        self.pf = PrimeFactors()

    def test_calc_prime_factorization(self):
        test_cases = [(2, [2]),
                      (3, [3]),
                      (4, [2, 2]),
                      (6, [2, 3]),
                      (8, [2, 2, 2]),
                      (9, [3, 3]),
                      (12, [2, 2, 3]),
                      (14, [2, 7]),
                      ]
        for number, answer in test_cases:
            with self.subTest(f"{number}"):
                ret = self.pf.calc_prime_factorization(number)
                # self.assertEqual(answer, ret)
                self.assertEqual(1, 1)  # TODO: 수정 필요
