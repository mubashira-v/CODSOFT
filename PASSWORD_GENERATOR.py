import tkinter as tk
import random
import string

class PasswordGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator")
        self.geometry("350x200")

        # Label for password length
        self.length_label = tk.Label(self, text="Password Length:")
        self.length_label.grid(row=0, column=0)

        # Entry field for password length
        self.length_entry = tk.Entry(self, width=10)
        self.length_entry.grid(row=0, column=1)

        # Checkboxes for character sets
        self.lowercase_checkbox = tk.Checkbutton(self, text="Lowercase Letters")
        self.lowercase_checkbox.grid(row=1, column=0)
        self.uppercase_checkbox = tk.Checkbutton(self, text="Uppercase Letters")
        self.uppercase_checkbox.grid(row=1, column=1)
        self.digits_checkbox = tk.Checkbutton(self, text="Digits")
        self.digits_checkbox.grid(row=2, column=0)
        self.symbols_checkbox = tk.Checkbutton(self, text="Symbols")
        self.symbols_checkbox.grid(row=2, column=1)

        # Button to generate password
        self.generate_button = tk.Button(self, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=3, columnspan=2)

        # Label for generated password
        self.password_label = tk.Label(self, text="Generated Password:")
        self.password_label.grid(row=4, column=0)

        # Entry field for displaying the password
        self.password_entry = tk.Entry(self, width=30)
        self.password_entry.grid(row=4, column=1)

    def generate_password(self):
        """
        Generates a random password based on the specified length and user-selected character sets.
        """
        length = int(self.length_entry.get())
        if length < 8:
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, "Password must be at least 8 characters long.")
            return

        # Define character sets based on user selection
        character_sets = []
        if self.lowercase_checkbox.var.get():
            character_sets.append(string.ascii_lowercase)
        if self.uppercase_checkbox.var.get():
            character_sets.append(string.ascii_uppercase)
        if self.digits_checkbox.var.get():
            character_sets.append(string.digits)
        if self.symbols_checkbox.var.get():
            character_sets.append(string.punctuation)

        # Combine character sets and generate password
        if not character_sets:
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, "Please select at least one character set.")
            return

        all_characters = "".join(character_sets)
        password = "".join(random.sample(all_characters, length))

        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.mainloop()
