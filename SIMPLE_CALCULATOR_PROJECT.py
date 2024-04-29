import tkinter as tk

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.geometry("300x400")

        # Create entry field for displaying the expression
        self.expression_entry = tk.Entry(self, width=30)
        self.expression_entry.grid(row=0, columnspan=4)

        # Create buttons for numbers and operators
        button_7 = tk.Button(self, text="7", command=lambda: self.press(7)).grid(row=1, column=0)
        button_8 = tk.Button(self, text="8", command=lambda: self.press(8)).grid(row=1, column=1)
        button_9 = tk.Button(self, text="9", command=lambda: self.press(9)).grid(row=1, column=2)
        button_divide = tk.Button(self, text="/", command=lambda: self.press("/")).grid(row=1, column=3)

        button_4 = tk.Button(self, text="4", command=lambda: self.press(4)).grid(row=2, column=0)
        button_5 = tk.Button(self, text="5", command=lambda: self.press(5)).grid(row=2, column=1)
        button_6 = tk.Button(self, text="6", command=lambda: self.press(6)).grid(row=2, column=2)
        button_multiply = tk.Button(self, text="*", command=lambda: self.press("*")).grid(row=2, column=3)

        button_1 = tk.Button(self, text="1", command=lambda: self.press(1)).grid(row=3, column=0)
        button_2 = tk.Button(self, text="2", command=lambda: self.press(2)).grid(row=3, column=1)
        button_3 = tk.Button(self, text="3", command=lambda: self.press(3)).grid(row=3, column=2)
        button_subtract = tk.Button(self, text="-", command=lambda: self.press("-")).grid(row=3, column=3)

        button_0 = tk.Button(self, text="0", command=lambda: self.press(0)).grid(row=4, column=0)
        button_clear = tk.Button(self, text="C", command=lambda: self.press("C")).grid(row=4, column=1)
        button_decimal = tk.Button(self, text=".", command=lambda: self.press(".")).grid(row=4, column=2)
        button_add = tk.Button(self, text="+", command=lambda: self.press("+")).grid(row=4, column=3)

        # Button to evaluate the expression
        button_equal = tk.Button(self, text="=", command=self.calculate).grid(row=5, columnspan=4)

        self.expression = ""  # Stores the current expression

    def press(self, key):
        """
        Handles button presses and updates the expression entry field.
        """
        if key == "C":
            self.expression = ""
        else:
            self.expression += str(key)
        self.expression_entry.delete(0, tk.END)
        self.expression_entry.insert(0, self.expression)

    def calculate(self):
        """
        Evaluates the expression and displays the result.
        """
        try:
            result = eval(self.expression)
            self.expression_entry.delete(0, tk.END)
            self.expression_entry.insert(0, result)
            self.expression = str(result)  # Update the expression for further calculations
        except SyntaxError:
            self.expression_entry.delete(0, tk.END)
            self.expression_entry.insert(0, "Error")

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()


