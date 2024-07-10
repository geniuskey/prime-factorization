from random import randint
from unittest import TestCase
from sympy.ntheory import factorint

from prime_factors import calc_prime_factorization


class TestPrimeFactors(TestCase):

    def test_calc_prime_factorization(self):
        for _ in range(10):
            number = randint(2, 10000)
            with self.subTest(f"{number}"):
                answer_dict = factorint(number)
                answer_list = []
                for k, v in answer_dict.items():
                    answer_list += [k] * v
                ret = calc_prime_factorization(number)
                self.assertEqual(answer_list, ret)


if __name__ == '__main__':
    print()