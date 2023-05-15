from math import comb as binomial_coefficient


def format_term(power, coefficient):
    string = ""
    
    if coefficient != 1 or power == 0:
        string += str(coefficient)

    if power > 0:
        string += 'x'
    if power > 1:
        string += '^' + str(power)

    return string

  
def print_polynomial(polynomial):
    terms = []

    for power, coefficient in enumerate(polynomial):
        if coefficient != 0:
            term = format_term(power, coefficient)
            terms.append(term)

    formatted_string = ' + '.join(terms[::-1])

    print(f"A_{n}(x) = {formatted_string}")


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



if __name__ == "__main__":
    
    n = int(input())
    coefficients = generate_coefficients(n)
    print_polynomial(coefficients)