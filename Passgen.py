import random
import string
import tkinter as tk
from tkinter import messagebox

class PasswordGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator")
        self.geometry("400x300")
        self.resizable(False, False)

        self.title_label = tk.Label(self, text="Password Generator", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        self.length_label = tk.Label(self, text="Password Length:", font=("Arial", 12))
        self.length_label.pack()

        self.length_entry = tk.Entry(self, font=("Arial", 12))
        self.length_entry.pack()

        self.uppercase_var = tk.IntVar()
        self.uppercase_checkbutton = tk.Checkbutton(self, text="Include Uppercase Letters", variable=self.uppercase_var)
        self.uppercase_checkbutton.pack()

        self.lowercase_var = tk.IntVar()
        self.lowercase_checkbutton = tk.Checkbutton(self, text="Include Lowercase Letters", variable=self.lowercase_var)
        self.lowercase_checkbutton.pack()

        self.digits_var = tk.IntVar()
        self.digits_checkbutton = tk.Checkbutton(self, text="Include Digits", variable=self.digits_var)
        self.digits_checkbutton.pack()

        self.punctuation_var = tk.IntVar()
        self.punctuation_checkbutton = tk.Checkbutton(self, text="Include Punctuation", variable=self.punctuation_var)
        self.punctuation_checkbutton.pack()

        self.generate_button = tk.Button(self, text="Generate Password", font=("Arial", 12), command=self.generate_button_clicked)
        self.generate_button.pack(pady=10)

        self.password_label = tk.Label(self, text="Generated Password:", font=("Arial", 12))
        self.password_label.pack()

        self.password_entry = tk.Entry(self, font=("Arial", 12), state="readonly")
        self.password_entry.pack()

        self.copy_button = tk.Button(self, text="Copy to Clipboard", font=("Arial", 12), command=self.copy_button_clicked)
        self.copy_button.pack(pady=10)

    def generate_password(self, length=12):
        characters = ""
        if self.uppercase_var.get():
            characters += string.ascii_uppercase
        if self.lowercase_var.get():
            characters += string.ascii_lowercase
        if self.digits_var.get():
            characters += string.digits
        if self.punctuation_var.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Please select at least one character type!")
            return None

        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def generate_button_clicked(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError
            password = self.generate_password(length)
            if password:
                self.password_entry.config(state="normal")
                self.password_entry.delete(0, tk.END)
                self.password_entry.insert(0, password)
                self.password_entry.config(state="readonly")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid password length!")

    def copy_button_clicked(self):
        password = self.password_entry.get()
        self.clipboard_clear()
        self.clipboard_append(password)
        messagebox.showinfo("Password Generator", "Password copied to clipboard!")

if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.mainloop()