import hashlib
import sys
sys.path.append('../lab2')

from lab2 import generate_large_prime 

def gcd_extended(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = gcd_extended(b % a, a)
        return (g, y - (b // a) * x, x)

def mod_inverse(a, m):
    g, x, _ = gcd_extended(a, m)
    if g != 1:
        raise Exception("Inverse doesn't exist")
    else:
        return x % m

def generate_key_pair(bits):
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537

    d = mod_inverse(e, phi)

    public_key = (n, e)
    private_key = (n, d)

    return public_key, private_key

def encrypt(message, public_key):
    n, e = public_key
    encrypted_message = pow(message, e, n)
    return encrypted_message

def decrypt(encrypted_message, private_key):
    n, d = private_key
    decrypted_message = pow(encrypted_message, d, n)
    return decrypted_message

def write_to_file(filename, data):
    with open(filename, 'wb') as file:
        file.write(data)

def read_from_file(filename):
    with open(filename, 'rb') as file:
        return file.read()

def get_key_pair_from_user():
    bits = int(input("Enter the desired key length (e.g., 64, 128, 256): "))
    public_key, private_key = generate_key_pair(bits)
    
    print("\nPublic Key:")
    print("n:", public_key[0])
    print("e:", public_key[1])

    print("\nPrivate Key:")
    print("n:", private_key[0])
    print("d:", private_key[1])

    return public_key, private_key

def hash_data(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data)
    return sha256_hash.hexdigest()

def main():
    public_key, private_key = get_key_pair_from_user()

    input_filename = input("\nEnter the name of the file to encrypt: ")
    encrypted_filename = input("Enter the name of the file to save the encrypted data: ")

    input_data = read_from_file(input_filename)

    encrypted_message = encrypt(int.from_bytes(input_data, 'big'), public_key)

    write_to_file(encrypted_filename, encrypted_message.to_bytes((encrypted_message.bit_length() + 7) // 8, 'big'))

    print("\nEncryption successful! Encrypted data saved to", encrypted_filename)

    decrypted_message = decrypt(encrypted_message, private_key)

    if hash_data(input_data) == hash_data(decrypted_message.to_bytes((decrypted_message.bit_length() + 7) // 8, 'big')):
        print("Decryption successful! Result matches the input.")
    else:
        print("Decryption Failed! Result does not match the input.")

if __name__ == "__main__":
    main()
