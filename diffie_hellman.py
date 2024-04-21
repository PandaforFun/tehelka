def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus
    return result

def diffie_hellman(p, g, a, b):
    A = mod_exp(g, a, p)
    B = mod_exp(g, b, p)
    key_A = mod_exp(B, a, p)
    key_B = mod_exp(A, b, p)
    return key_A, key_B

def main():
    # Public parameters
    p = 23  # Prime number
    g = 5   # Generator

    # Private keys
    a = 6
    b = 15

    # Key exchange
    key_A, key_B = diffie_hellman(p, g, a, b)

    print("Shared secret key A:", key_A)
    print("Shared secret key B:", key_B)

main()
