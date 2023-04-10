def calculate_coefficient(n, k, coefficients):
    coefficient = (k+1) * coefficients[n-1][k] + (n-k) * coefficients[n-1][k-1]
    return coefficient

  
def generate_coefficients(max_n):
    coefficients = [[1]+[0]*length for length in range(max_n+1)]

    for n in range(1, max_n+1):
        for k in range(1, n):
            coefficients[n][k] = calculate_coefficient(n, k, coefficients)
    
    return coefficients
