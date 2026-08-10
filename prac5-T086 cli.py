import random

def generate_private_key():
    return random.randint(2, 100)

def generate_public_key(private_key, g, p):
    return pow(g, private_key, p)

def generate_shared_key(public_key, private_key, p):
    return pow(public_key, private_key, p)

def main():
    print("DIFFIE-HELLMAN KEY EXCHANGE")
    print("=" * 40)

    p = int(input("Enter prime number p: "))
    g = int(input("Enter primitive root g: "))

    alice_private = generate_private_key()
    bob_private = generate_private_key()

    alice_public = generate_public_key(
        alice_private,
        g,
        p
    )

    bob_public = generate_public_key(
        bob_private,
        g,
        p
    )

    alice_shared = generate_shared_key(
        bob_public,
        alice_private,
        p
    )

    bob_shared = generate_shared_key(
        alice_public,
        bob_private,
        p
    )

    print("\nPurvi Private Key:", alice_private)
    print("Purvi Public Key:", alice_public)

    print("\nNeha Private Key:", bob_private)
    print("Neha Public Key:", bob_public)

    print("\nPurvi Shared Key:", alice_shared)
    print("Neha Shared Key:", bob_shared)

    print("\nResult:")

    if alice_shared == bob_shared:
        print("Key exchange successful")
        print("Both parties have the same shared secret.")
    else:
        print("Key exchange failed")

if __name__ == "__main__":
    main()
