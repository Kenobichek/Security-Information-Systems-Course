from decimal import Decimal, getcontext

getcontext().prec = 50

def decimal_add(a, b):
    return Decimal(a) + Decimal(b)

def decimal_multiply(a, b):
    return Decimal(a) * Decimal(b)

def decimal_square(a):
    return Decimal(a) ** 2

def decimal_remainder_by_module(a, b):
    return Decimal(a) % Decimal(b)

def multiply(a, b):
    a = list(map(int, a[::-1]))
    b = list(map(int, b[::-1]))

    result = [0] * (len(a) + len(b))

    for i in range(len(a)):
        carry = 0
        for j in range(len(b)):
            temp = a[i] * b[j] + result[i + j] + carry
            carry = temp // 10
            result[i + j] = temp % 10
        if carry > 0:
            result[i + len(b)] += carry
    
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    result = result[::-1]
    result_str = "".join(map(str, result))
    return result_str

def add(a, b):
    len_a, len_b = len(a), len(b)
    max_len = max(len_a, len_b)
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    carry = 0
    result = []
    for i in range(max_len - 1, -1, -1):
        sum_digits = int(a[i]) + int(b[i]) + carry
        carry = sum_digits // 10
        result.append(str(sum_digits % 10))
    
    if carry:
        result.append(str(carry))
    
    return ''.join(result[::-1])

def square(a):
    return multiply(a, a)

def remainder_by_module(a, b):
    a = int(a)
    b = int(b)
    if b == 0:
        raise ValueError("Division by zero is impossible!!!")
    
    return str(a % b)

num1 = "12345678901234567890123456789012345678901234567890"
num2 = "98765432109876543210987654321098765432109876543210"

print("Multiplying (manual vs library decimal):\n", multiply(num1, num2), "\n", decimal_multiply(num1, num2))
print("Adding (manual vs decimal library):\n", add(num1, num2), "\n", decimal_add(num1, num2))
print("Squaring (manual vs library decimal):\n", square(num1), "\n", decimal_square(num1))
print("Remainder by module (manual vs library decimal):\n", remainder_by_module(num1, num2), "\n", decimal_remainder_by_module(num1, num2))
