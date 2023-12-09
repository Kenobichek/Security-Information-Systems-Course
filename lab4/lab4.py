from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

def encrypt_message(message, key):
    cipher = DES.new(key, DES.MODE_ECB)
    encrypted_message = cipher.encrypt(message)
    return encrypted_message

def decrypt_message(encrypted_message, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message

def generate_signature(message, key):
    cipher = DES.new(key, DES.MODE_CBC, IV=b'\x00\x00\x00\x00\x00\x00\x00\x00')
    padded_message = pad(message, DES.block_size)
    signature = cipher.encrypt(padded_message)
    return signature

def main():
    key = input("Введіть ключ шифрування (8 символів): ")[:8].encode('utf-8')

    mode = input("Виберіть режим (encrypt/decrypt/sign): ")
    
    if mode == "encrypt" or mode == "decrypt":
        input_file = input("Введіть ім'я файлу для обробки: ")
        output_file = input("Введіть ім'я файлу результату: ")

        with open(input_file, 'rb') as file:
            data = file.read()

        if mode == "encrypt":
            encrypted_data = encrypt_message(data, key)
            with open(output_file, 'wb') as file:
                file.write(encrypted_data)
            print("Файл успішно зашифровано.")
        elif mode == "decrypt":
            decrypted_data = decrypt_message(data, key)
            with open(output_file, 'wb') as file:
                file.write(decrypted_data)
            print("Файл успішно розшифровано.")
    
    elif mode == "sign":
        input_file = input("Введіть ім'я файлу для обробки: ")
        signature_file = input("Введіть ім'я файлу підпису: ")

        with open(input_file, 'rb') as file:
            data = file.read()

        signature = generate_signature(data, key)
        with open(signature_file, 'wb') as file:
            file.write(signature)
        print("Цифровий підпис сформовано успішно.")

if __name__ == "__main__":
    main()