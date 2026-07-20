import tkinter as tk
from tkinter import messagebox
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

def encrypt():
    message = input_box.get()

    if message == "":
        messagebox.showwarning("Warning", "Please enter a message.")
        return

    cipher = [str(pow(ord(ch), e, n)) for ch in message]
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, " ".join(cipher))

def decrypt():
    try:
        cipher = list(map(int, input_box.get().split()))
        message = "".join(chr(pow(num, d, n)) for num in cipher)

        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, message)

    except:
        messagebox.showerror("Error", "Invalid encrypted data.")

def clear():
    input_box.delete(0, tk.END)
    output_box.delete("1.0", tk.END)

root = tk.Tk()
root.title("RSA Encryption and Decryption")
root.geometry("500x320")
root.resizable(False, False)
root.configure(bg="#F5F5F5")

title = tk.Label(
    root,
    text="RSA Encryption and Decryption",
    font=("Arial", 16, "bold"),
    bg="#F5F5F5"
)
title.pack(pady=15)

label = tk.Label(
    root,
    text="Enter Message or Encrypted Numbers",
    font=("Arial", 11),
    bg="#F5F5F5"
)
label.pack()

input_box = tk.Entry(root, width=55, font=("Arial", 11))
input_box.pack(pady=10)

button_frame = tk.Frame(root, bg="#F5F5F5")
button_frame.pack()

tk.Button(
    button_frame,
    text="Encrypt",
    width=12,
    command=encrypt
).grid(row=0, column=0, padx=8)

tk.Button(
    button_frame,
    text="Decrypt",
    width=12,
    command=decrypt
).grid(row=0, column=1, padx=8)

tk.Button(
    button_frame,
    text="Clear",
    width=12,
    command=clear
).grid(row=0, column=2, padx=8)

output_box = tk.Text(
    root,
    width=58,
    height=7,
    font=("Arial", 11)
)
output_box.pack(pady=20)

root.mainloop()
