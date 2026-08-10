import hashlib
import secrets
import math

def is_prime(n, k=10):
    if n < 2:
        return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return False

    d = n - 1
    r = 0
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = secrets.randbelow(n - 3) + 2
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

def generate_prime(bits):
    while True:
        n = secrets.randbits(bits)
        n |= (1 << bits - 1) | 1
        if is_prime(n):
            return n

def generate_keys():
    p = generate_prime(256)
    q = generate_prime(256)

    while p == q:
        q = generate_prime(256)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537

    while math.gcd(e, phi) != 1:
        e += 2

    d = pow(e, -1, phi)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

def hash_message(message):
    return int.from_bytes(
        hashlib.sha256(message.encode()).digest(),
        byteorder="big"
    )

def sign_message(message, private_key):
    d, n = private_key
    h = hash_message(message)
    signature = pow(h, d, n)
    return signature

def verify_signature(message, signature, public_key):
    e, n = public_key
    h = hash_message(message)
    recovered_hash = pow(signature, e, n)
    return h == recovered_hash

def main():
    print("T086 DIGITAL SIGNATURE")
    print("=" * 40)

    public_key, private_key = generate_keys()

    print("\nPublic Key:")
    print("e =", public_key[0])
    print("n =", public_key[1])

    print("\nPrivate Key:")
    print("d =", private_key[0])
    print("n =", private_key[1])

    message = input("\nEnter message: ")

    signature = sign_message(message, private_key)

    print("\nDigital Signature:")
    print(signature)

    result = verify_signature(message, signature, public_key)

    print("\nVerification Result:")
    if result:
        print("Signature is VALID")
        print("Message integrity and authenticity verified.")
    else:
        print("Signature is INVALID")

    choice = input("\nDo you want to test a modified message? (y/n): ")

    if choice.lower() == "y":
        modified_message = input("Enter modified message: ")

        result = verify_signature(
            modified_message,
            signature,
            public_key
        )

        print("\nVerification Result:")
        if result:
            print("Signature is VALID")
        else:
            print("Signature is INVALID")
            print("Message has been modified.")

if __name__ == "__main__":
    main()
    
