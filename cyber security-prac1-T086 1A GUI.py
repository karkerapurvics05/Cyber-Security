from tkinter import *
BG_COLOR = "#2C3E50"       
TEXT_COLOR = "#ECF0F1"     
ENTRY_BG = "#34495E"      
ENC_BTN = "#2ECC71"        
DEC_BTN = "#E74C3C"        
BTN_TEXT = "#FFFFFF"       
def encrypt():
    text = txt.get()
    try:
        shift = int(key.get())
    except ValueError:
        output.config(text="Please enter a valid number key!", fg=DEC_BTN)
        return
        
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char)-start+shift)%26+start)
        else:
            result += char
    output.config(text=result, fg=ENC_BTN)
def decrypt():
    text = txt.get()
    try:
        shift = int(key.get())
    except ValueError:
        output.config(text="Please enter a valid number key!", fg=DEC_BTN)
        return
        
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char)-start-shift)%26+start)
        else:
            result += char
    output.config(text=result, fg=TEXT_COLOR)
root = Tk()
root.title("Purvi R Karkera T086 - 1A gui")
root.config(bg=BG_COLOR, padx=20, pady=20)
Label(root, text="Message", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 11, "bold")).pack(pady=(0, 5))
txt = Entry(root, width=40, bg=ENTRY_BG, fg=TEXT_COLOR, insertbackground=TEXT_COLOR, bd=0, relief=FLAT)
txt.pack(ipady=5, pady=(0, 15))
Label(root, text="Key (Number)", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 11, "bold")).pack(pady=(0, 5))
key = Entry(root, width=10, bg=ENTRY_BG, fg=TEXT_COLOR, insertbackground=TEXT_COLOR, bd=0, relief=FLAT, justify="center")
key.pack(ipady=5, pady=(0, 20))
Button(root, text="Encrypt", command=encrypt, bg=ENC_BTN, fg=BTN_TEXT, activebackground="#27AE60", activeforeground=BTN_TEXT, bd=0, font=("Arial", 10, "bold"), width=15).pack(pady=5, ipady=3)
Button(root, text="Decrypt", command=decrypt, bg=DEC_BTN, fg=BTN_TEXT, activebackground="#C0392B", activeforeground=BTN_TEXT, bd=0, font=("Arial", 10, "bold"), width=15).pack(pady=5, ipady=3)
Label(root, text="Result:", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 10, "italic")).pack(pady=(20, 5))
output = Label(root, text="", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 12, "bold"), wraplength=300)
output.pack()
root.mainloop()
