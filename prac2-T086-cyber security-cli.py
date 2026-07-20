from math import gcd

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d

p = 61
q = 53

n = p * q
phi = (p - 1) * (q - 1)

e = 17
while gcd(e, phi) != 1:
    e += 2

d = mod_inverse(e, phi)

def encrypt(message):
    return [pow(ord(ch), e, n) for ch in message]

def decrypt(cipher):
    return ''.join(chr(pow(i, d, n)) for i in cipher)

while True:
    print("\n----- RSA MENU -----")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        message = input("Enter message: ")
        cipher = encrypt(message)
        print("Encrypted Data:")
        print(*cipher)

    elif choice == "2":
        data = input("Enter encrypted numbers (space separated): ")
        try:
            cipher = list(map(int, data.split()))
            print("Decrypted Message:", decrypt(cipher))
        except:
            print("Invalid input.")

    elif choice == "3":
        print("Program Closed.")
        break

    else:
        print("Invalid Choice.")
