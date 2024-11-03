from cryptography.fernet import Fernet
import rsa
import ast
"""Caesar Cipher, by Al Sweigart al@inventwithpython.com
The Caesar cipher is a shift cipher that uses addition and subtraction
to encrypt and decrypt letters.
More info at: https://en.wikipedia.org/wiki/Caesar_cipher"""

# Every possible symbol that can be encrypted/decrypted:
# (!) You can add numbers and punctuation marks to encrypt those
# symbols as well.
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class CaesarCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, message):
        encrypted = ""
        for symbol in message:
            if symbol.upper() in SYMBOLS:
                num = SYMBOLS.index(symbol.upper())
                num = (num + self.key) % len(SYMBOLS)
                encrypted += SYMBOLS[num]
            else:
                encrypted += symbol
        return f"Encrypted message: {encrypted}"

    def decrypt(self, message):
        decrypted = ""
        for symbol in message:
            if symbol.upper() in SYMBOLS:
                num = SYMBOLS.index(symbol.upper())
                num = (num - self.key) % len(SYMBOLS)
                decrypted += SYMBOLS[num]
            else:
                decrypted += symbol
        return f"Decrypted message: {decrypted}"


class AESCipher:
    def __init__(self, key=None):
        if key is None:
            key = Fernet.generate_key()
        self.cipher = Fernet(key)
        self.key = key

    def encrypt(self, message):
        return self.cipher.encrypt(message.encode()).decode()

    def decrypt(self, message):
        return self.cipher.decrypt(message.encode()).decode()


class RSACipher:
    def __init__(self, public_key=None, private_key=None, key_size=512):
        if public_key is not None and private_key is not None:
            self.public_key = public_key
            self.private_key = private_key
        else:
            (self.public_key, self.private_key) = rsa.newkeys(key_size)

    def encrypt(self, message):
        return rsa.encrypt(message.encode(), self.public_key)

    def decrypt(self, message):
        return rsa.decrypt(message, self.private_key).decode()


def get_user_mode():
    while True:  # Keep asking until the user enters e or d.
        print("Do you want to (e)ncrypt or (d)ecrypt?")
        response = input("> ").lower()

        if response.startswith("e"):
            return "encrypt"
        elif response.startswith("d"):
            return "decrypt"
        else:
            print("Please enter the letter 'e' or 'd'.")


def get_user_key():
    while True:  # Keep asking until the user enters a valid key.
        max_key = len(SYMBOLS) - 1
        print(f"Please enter the key (0 to {max_key}) to use.")
        response = input("> ")

        if not response.isdecimal():
            continue

        response = int(response)

        if 0 <= response <= max_key:
            return response


def main():
    print("Select encryption method:\n1. Caesar Cipher\n2. AES Cipher\n3. RSA Cipher")
    choice = input("> ").strip()

    if choice == "1":
        mode = get_user_mode()  # Let the user enter if they are encrypting or decrypting
        key = get_user_key()  # Let the user enter the key to use

        coder = CaesarCipher(key)

        # Let the user enter the message to encrypt/decrypt
        print(f"Enter the message to {mode}.")
        message = input("> ").upper()  # Caesar cipher only works on uppercase letters

        if mode == "encrypt":
            # Stores the encrypted/decrypted form of the message
            translated = coder.encrypt(message)
        else:
            translated = coder.decrypt(message)

    # Display the encrypted/decrypted string to the screen
        print(translated)

    if choice == "2":
        print("Do you want to (g)enerate a new key or (u)se an existing key?")
        key_choice = input("> ").strip().lower()

        if key_choice == "g":
            key = Fernet.generate_key()
            print(f"Generated AES Key: {key.decode()}")
            aes = AESCipher(key)
        elif key_choice == "u":
            key = input("Enter your existing AES key: ").encode()
            aes = AESCipher(key)
        else:
            print("Invalid choice.")
            return

        mode = get_user_mode()
        print(f"Enter the message to {mode}.")
        message = input("> ")

        if mode == "encrypt":
            print("Encrypted message:", aes.encrypt(message))
        elif mode == "decrypt":
            print("Decrypted message:", aes.decrypt(message))
        else:
            print("Invalid choice.")

    elif choice == "3":
        try:
            with open('public_key.pem', 'rb') as f:
                public_key = rsa.PublicKey.load_pkcs1(f.read())
            with open('private_key.pem', 'rb') as f:
                private_key = rsa.PrivateKey.load_pkcs1(f.read())
            rsa_cipher = RSACipher(public_key=public_key, private_key=private_key)
            print("Loaded existing RSA keys.")
        except FileNotFoundError:
            rsa_cipher = RSACipher()
            with open('public_key.pem', 'wb') as f:
                f.write(rsa_cipher.public_key.save_pkcs1())
            with open('private_key.pem', 'wb') as f:
                f.write(rsa_cipher.private_key.save_pkcs1())
            print("Generated new RSA keys.")

        mode = get_user_mode()

        if mode == "encrypt":
            message = input("Enter the message: ")
            encrypted_message = rsa_cipher.encrypt(message)
            print("Encrypted message:", encrypted_message)
            print("Public Key:", rsa_cipher.public_key.save_pkcs1().decode())
        elif mode == "decrypt":
            encrypted_message = input("Enter the encrypted message (as bytes): ")
            encrypted_message = ast.literal_eval(encrypted_message)
            decrypted_message = rsa_cipher.decrypt(encrypted_message)
            print("Decrypted message:", decrypted_message)
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    print("Caesar Cipher")
    print("The algorithm encrypts letters by shifting them over by a")
    print("key number. For example, a key of 2 means the letter A is")
    print("encrypted into C, the letter B encrypted into D, and so on.")
    print()

    while True:
        main()

        print("\n\nDo you want to run cipher one more time? Y or N")
        repeat = input("> ").lower()

        if repeat != "y":
            print("Thank you for using Caesar Cipher.")
            break
