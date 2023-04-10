from math import comb as binomial_coefficient


def calculate_coefficient(n, k):
    total = 0

    for j in range(k+1):
        total += binomial_coefficient(n+1, j) * ((k - j + 1) ** n) * ((-1) ** j)

    return total


def generate_coefficients(n):
    if n == 0:
        return [1]
    
    coefficients = [0]*n

    for k in range(n):
        coefficients[k] = calculate_coefficient(n, k)
    
    return coefficients
