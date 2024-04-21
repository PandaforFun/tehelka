import random
import math

class RSA:
    def __init__(self, bit_length):
        self.private_key, self.public_key, self.modulus = self.generate_keys(bit_length)

    def generate_keys(self, bit_length):
        rnd = random.SystemRandom()
        p = self.generate_prime(bit_length, rnd)
        q = self.generate_prime(bit_length, rnd)
        modulus = p * q

        phi = (p - 1) * (q - 1)

        public_key = 65537
        private_key = self.mod_inverse(public_key, phi)
        
        return private_key, public_key, modulus

    def generate_prime(self, bit_length, rnd):
        prime_candidate = 4
        while not self.is_prime(prime_candidate):
            prime_candidate = rnd.getrandbits(bit_length)
            prime_candidate |= (1 << bit_length - 1) | 1

        return prime_candidate

    def is_prime(self, n, k=5):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False

        d = n - 1
        while d % 2 == 0:
            d //= 2

        for _ in range(k):
            a = random.randint(2, n - 2)
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(int(math.log(n, 2))):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

    def encrypt(self, message):
        return pow(message, self.public_key, self.modulus)

    def decrypt(self, encrypted_message):
        return pow(encrypted_message, self.private_key, self.modulus)

    def mod_inverse(self, a, m):
        m0 = m
        y = 0
        x = 1

        if m == 1:
            return 0

        while a > 1:
            q = a // m
            a, m = m, a % m
            x, y = y, x - q * y

        if x < 0:
            x += m0

        return x

def main():
    rsa = RSA(1024)

    message = input("Enter the message to Send: ")
    plaintext = int.from_bytes(message.encode(), "big")

    encrypted = rsa.encrypt(plaintext)
    decrypted = rsa.decrypt(encrypted)

    print("Original message:", message)
    print("Encrypted message:", encrypted)
    print("Decrypted message:", decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big").decode())

main()
