import math
print("Purvi.R.Karkera T086 1B cli")
def encrypt(message, key):
    cipher = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            cipher[col] += message[pointer]
            pointer += key
    return ''.join(cipher)
def decrypt(cipher, key):
    num_cols = math.ceil(len(cipher) / key)
    num_rows = key
    shaded = (num_cols * num_rows) - len(cipher)
    plain = [''] * num_cols
    col = 0
    row = 0
    for symbol in cipher:
        plain[col] += symbol
        col += 1
        if (col == num_cols) or (col == num_cols - 1 and row >= num_rows - shaded):
            col = 0
            row += 1
    return ''.join(plain)
while True:
    print("\n1.Encrypt")
    print("2.Decrypt")
    print("3.Exit")
    ch = input("Choice: ")
    if ch == '1':
        msg = input("Message: ")
        key = int(input("Key: "))
        print("Cipher:", encrypt(msg, key))
    elif ch == '2':
        msg = input("Cipher: ")
        key = int(input("Key: "))
        print("Plain:", decrypt(msg, key))
    elif ch == '3':
        break
