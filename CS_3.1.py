import tkinter as tk
from tkinter import messagebox
import hmac
import hashlib

# Function to Generate MAC
def generate_mac():
    message = message_entry.get()
    key = key_entry.get()

    if not message or not key:
        messagebox.showerror("Error", "Please enter both Message and Secret Key")
        return

    mac = hmac.new(
        key.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()

    mac_entry.delete(0, tk.END)
    mac_entry.insert(0, mac)


# Function to Verify MAC
def verify_mac():
    message = message_entry.get()
    key = key_entry.get()
    entered_mac = mac_entry.get()

    if not message or not key or not entered_mac:
        messagebox.showerror("Error", "Please fill all fields")
        return

    generated_mac = hmac.new(
        key.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()

    if hmac.compare_digest(generated_mac, entered_mac):
        messagebox.showinfo("Verification", "MAC Verified Successfully!\nMessage is Authentic.")
    else:
        messagebox.showerror("Verification", "MAC Verification Failed!\nMessage has been modified or key is incorrect.")


# Function to Clear Fields
def clear_fields():
    message_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)
    mac_entry.delete(0, tk.END)


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Message Authentication Code (MAC)")
root.geometry("650x300")

# Title
title = tk.Label(
    root,
    text="Message Authentication Code (MAC) using HMAC-SHA256",
    font=("Arial", 14, "bold")
)
title.pack(pady=10)

# Message
tk.Label(root, text="Message:", font=("Arial", 11)).pack()
message_entry = tk.Entry(root, width=70)
message_entry.pack(pady=5)

# Secret Key
tk.Label(root, text="Secret Key:", font=("Arial", 11)).pack()
key_entry = tk.Entry(root, width=70, show="*")
key_entry.pack(pady=5)

# MAC
tk.Label(root, text="Generated / Enter MAC:", font=("Arial", 11)).pack()
mac_entry = tk.Entry(root, width=70)
mac_entry.pack(pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=15)

generate_button = tk.Button(button_frame, text="Generate MAC", width=15, command=generate_mac)
generate_button.grid(row=0, column=0, padx=10)

verify_button = tk.Button(button_frame, text="Verify MAC", width=15, command=verify_mac)
verify_button.grid(row=0, column=1, padx=10)

clear_button = tk.Button(button_frame, text="Clear", width=15, command=clear_fields)
clear_button.grid(row=0, column=2, padx=10)

root.mainloop()
