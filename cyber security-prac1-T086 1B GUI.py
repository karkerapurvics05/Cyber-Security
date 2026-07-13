from tkinter import *
import math
BG_DARK = "#1E1E24"       
BG_CARD = "#2A2A32"       
TEXT_LIGHT = "#E1E1E6"    
TEXT_MUTED = "#A8A8B2"    
ACCENT_CYAN = "#00ADB5"   
ALERT_RED = "#FF2E63"     
def encrypt():
    msg = txt.get()
    try:
        key = int(k.get())
        if key <= 0: raise ValueError
    except ValueError:
        output.config(text="Enter a positive number key!", fg=ALERT_RED)
        return
    cipher = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(msg):
            cipher[col] += msg[pointer]
            pointer += key
    output.config(text=''.join(cipher), fg=ACCENT_CYAN)
def decrypt():
    msg = txt.get()
    try:
        key = int(k.get())
        if key <= 0: raise ValueError
    except ValueError:
        output.config(text="Enter a positive number key!", fg=ALERT_RED)
        return
    num_cols = math.ceil(len(msg) / key)
    num_rows = key
    shaded_boxes = (num_cols * num_rows) - len(msg)

    plaintext = [''] * num_cols
    col = 0
    row = 0
    for char in msg:
        plaintext[col] += char
        col += 1
        if (col == num_cols) or (col == num_cols - 1 and row >= num_rows - shaded_boxes):
            col = 0
            row += 1
    output.config(text=''.join(plaintext), fg=TEXT_LIGHT)
root = Tk()
root.title("Purvi.R.Karkera T086 - 1B gui")
root.config(bg=BG_DARK, padx=25, pady=25)
Label(root, text="MESSAGE", bg=BG_DARK, fg=TEXT_MUTED, font=("Arial", 10, "bold")).pack(anchor="w", pady=(0, 5))
txt = Entry(root, width=40, bg=BG_CARD, fg=TEXT_LIGHT, insertbackground=TEXT_LIGHT, bd=0, relief=FLAT, font=("Arial", 11))
txt.pack(ipady=6, pady=(0, 15))
Label(root, text="KEY (NUMBER)", bg=BG_DARK, fg=TEXT_MUTED, font=("Arial", 10, "bold")).pack(anchor="w", pady=(0, 5))
k = Entry(root, width=15, bg=BG_CARD, fg=TEXT_LIGHT, insertbackground=TEXT_LIGHT, bd=0, relief=FLAT, font=("Arial", 11), justify="center")
k.pack(ipady=6, pady=(0, 20))
Button(root, text="Encrypt", command=encrypt, bg=ACCENT_CYAN, fg=BG_DARK, activebackground="#00888F", activeforeground=BG_DARK, bd=0, font=("Arial", 11, "bold"), width=15, cursor="hand2").pack(pady=5, ipady=4)
Button(root, text="Decrypt", command=decrypt, bg=BG_CARD, fg=TEXT_LIGHT, activebackground="#3E3E4A", activeforeground=TEXT_LIGHT, bd=0, font=("Arial", 11, "bold"), width=15, cursor="hand2").pack(pady=5, ipady=4)
Label(root, text="RESULT", bg=BG_DARK, fg=TEXT_MUTED, font=("Arial", 9, "bold")).pack(pady=(20, 5))
output = Label(root, text="", bg=BG_DARK, fg=TEXT_LIGHT, font=("Consolas", 13, "bold"), wraplength=300, justify="center")
output.pack()
root.mainloop()
