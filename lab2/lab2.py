import random

def is_probable_prime(n, k=5):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def verify_fermat_theorem(candidate):
    a = random.randint(2, candidate - 2)
    if pow(a, candidate - 1, candidate) != 1:
        return False
    return True

def generate_large_prime(bits):
    while True:
        candidate = random.getrandbits(bits) | (1 << bits - 1) | 1
        if is_probable_prime(candidate) and verify_fermat_theorem(candidate):
            return candidate

bits = 64 
large_prime_number = generate_large_prime(bits)
large_prime_number2 = generate_large_prime(bits)

print(f"Large Prime Number: {large_prime_number}")
print(f"Large Prime Number: {large_prime_number2}")