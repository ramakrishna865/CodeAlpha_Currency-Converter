import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates, RatesNotAvailableError

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        self.from_label = ttk.Label(root, text="From Currency:")
        self.from_label.pack(pady=10)

        self.from_var = tk.StringVar()
        self.from_combo = ttk.Combobox(root, textvariable=self.from_var, values=CurrencyRates().get_rates("").keys())
        self.from_combo.pack(pady=5)

        self.to_label = ttk.Label(root, text="To Currency:")
        self.to_label.pack()

        self.to_var = tk.StringVar()
        self.to_combo = ttk.Combobox(root, textvariable=self.to_var, values=CurrencyRates().get_rates("").keys())
        self.to_combo.pack(pady=5)

        self.amount_label = ttk.Label(root, text="Amount:")
        self.amount_label.pack()

        self.amount_var = tk.DoubleVar()
        self.amount_entry = ttk.Entry(root, textvariable=self.amount_var)
        self.amount_entry.pack(pady=5)

        self.convert_button = ttk.Button(root, text="Convert", command=self.convert)
        self.convert_button.pack()

        self.result_label = ttk.Label(root, text="Result:")
        self.result_label.pack(pady=5)

        self.result_var = tk.StringVar()
        self.result_label = ttk.Label(root, textvariable=self.result_var)
        self.result_label.pack()

    def convert(self):
        from_currency = self.from_var.get()
        to_currency = self.to_var.get()
        amount = self.amount_var.get()

        if not from_currency or not to_currency or amount <= 0:
            self.result_var.set("Invalid input")
            return

        try:
            c = CurrencyRates()
            converted_amount = c.convert(from_currency, to_currency, amount)
            self.result_var.set(f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
        except RatesNotAvailableError:
            self.result_var.set("Currency rates are not available. Please try again later.")
        except Exception as e:
            self.result_var.set(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
