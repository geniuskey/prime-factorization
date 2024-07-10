def calc_prime_factorization(number):
    factors = []

    # 짝수일 경우
    while number % 2 == 0:
        number //= 2
        factors.append(2)

    # 홀수일 경우
    factor = 3
    while number != 1 and factor <= number ** 0.5:
        if number % factor == 0:
            number //= factor
            factors.append(factor)
        else:
            factor += 2

    # 그 자체가 소수인 경우
    if number > 2:
        factors.append(number)
    return factors
