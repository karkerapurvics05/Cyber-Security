def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result
def decrypt(text, shift):
    return encrypt(text, -shift)
while True:
    print("\nPurvi.R.Karkera S086 - 1A cli")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        text = input("Enter plaintext: ")
        shift = int(input("Enter key: "))
        print("Cipher Text:", encrypt(text, shift))
    elif choice == '2':
        text = input("Enter ciphertext: ")
        shift = int(input("Enter key: "))
        print("Plain Text:", decrypt(text, shift))
    elif choice == '3':
        break
    else:
        print("Invalid Choice")



