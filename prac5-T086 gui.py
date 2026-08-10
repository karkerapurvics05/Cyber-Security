import tkinter as tk
from tkinter import messagebox
import random

def private_key():
    return random.randint(2, 10)

def public_key(private, g, p):
    return pow(g, private, p)

def shared_key(public, private, p):
    return pow(public, private, p)

def exchange():
    try:
        p = int(p_entry.get())
        g = int(g_entry.get())

        private1 = private_key()
        private2 = private_key()

        public1 = public_key(private1, g, p)
        public2 = public_key(private2, g, p)

        shared1 = shared_key(public2, private1, p)
        shared2 = shared_key(public1, private2, p)

        private1_entry.delete(0, tk.END)
        private1_entry.insert(0, private1)

        public1_entry.delete(0, tk.END)
        public1_entry.insert(0, public1)

        private2_entry.delete(0, tk.END)
        private2_entry.insert(0, private2)

        public2_entry.delete(0, tk.END)
        public2_entry.insert(0, public2)

        shared1_entry.delete(0, tk.END)
        shared1_entry.insert(0, shared1)

        shared2_entry.delete(0, tk.END)
        shared2_entry.insert(0, shared2)

        if shared1 == shared2:
            result.config(
                text="KEY EXCHANGE SUCCESSFUL\nPurvi and Neha have the same secret key.",
                fg="green"
            )
        else:
            result.config(
                text="KEY EXCHANGE FAILED",
                fg="red"
            )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")


root = tk.Tk()
root.title("Diffie-Hellman Key Exchange")
root.geometry("600x650")
root.config(bg="lightgray")

tk.Label(
    root,
    text="DIFFIE-HELLMAN KEY EXCHANGE",
    font=("Arial", 20, "bold"),
    bg="lightgray"
).pack(pady=15)

tk.Label(
    root,
    text="Prime Number (p)",
    bg="lightgray"
).pack()

p_entry = tk.Entry(root)
p_entry.pack()
p_entry.insert(0, "23")

tk.Label(
    root,
    text="Primitive Root (g)",
    bg="lightgray"
).pack()

g_entry = tk.Entry(root)
g_entry.pack()
g_entry.insert(0, "5")

person1_label = tk.Label(
    root,
    text="PURVI",
    font=("Arial", 14, "bold"),
    bg="lightgray"
)
person1_label.pack(pady=10)

private1_entry = tk.Entry(root, width=40)
private1_entry.pack()

tk.Label(
    root,
    text="Purvi Private Key",
    bg="lightgray"
).pack()

public1_entry = tk.Entry(root, width=40)
public1_entry.pack()

tk.Label(
    root,
    text="Purvi Public Key",
    bg="lightgray"
).pack()

person2_label = tk.Label(
    root,
    text="NEHA",
    font=("Arial", 14, "bold"),
    bg="lightgray"
)
person2_label.pack(pady=10)

private2_entry = tk.Entry(root, width=40)
private2_entry.pack()

tk.Label(
    root,
    text="Neha Private Key",
    bg="lightgray"
).pack()

public2_entry = tk.Entry(root, width=40)
public2_entry.pack()

tk.Label(
    root,
    text="Neha Public Key",
    bg="lightgray"
).pack()

shared1_entry = tk.Entry(root, width=40)
shared1_entry.pack(pady=5)

tk.Label(
    root,
    text="Purvi Shared Key",
    bg="lightgray"
).pack()

shared2_entry = tk.Entry(root, width=40)
shared2_entry.pack(pady=5)

tk.Label(
    root,
    text="Neha Shared Key",
    bg="lightgray"
).pack()

tk.Button(
    root,
    text="Perform Key Exchange",
    command=exchange,
    bg="blue",
    fg="white",
    font=("Arial", 11, "bold")
).pack(pady=15)

result = tk.Label(
    root,
    text="Click the button to perform key exchange",
    font=("Arial", 11, "bold"),
    bg="lightgray",
    fg="blue"
)
result.pack()
root.mainloop()
