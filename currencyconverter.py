import requests
import tkinter as tk
from tkinter import ttk

def con_currency(amount, fcurrency, tcurrency):
    base_url = "https://api.exchangerate-api.com/v4/latest/"    
    response = requests.get(base_url + fcurrency)
    data = response.json()

    if 'rates' in data:
        rates = data['rates']
        if fcurrency == tcurrency:
            return amount

        if fcurrency in rates and tcurrency in rates:
            conversion_rate = rates[tcurrency] / rates[fcurrency]
            converted_amount = amount * conversion_rate
            return converted_amount
        else:
            raise ValueError("Invalid currency!")
    else:
        raise ValueError("Unable to fetch exchange rates!")

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        self.amount_label = ttk.Label(root, text="Amount:",font=("Arial", 15))
        self.amount_label.grid(row=0, column=0, padx=30, pady=30)

        self.amount_entry = ttk.Entry(root)
        self.amount_entry.grid(row=0, column=1, padx=30, pady=30)

        self.fcurrency_label = ttk.Label(root, text="From Currency:",font=("Arial", 15))
        self.fcurrency_label.grid(row=1, column=0, padx=30, pady=30)

        self.fcurrency_combobox = ttk.Combobox(root, values=["INR", "USD", "EUR", "GBP", "JPY", "CAD", "AUD", "CNY", "HKD", "SGD", "NZD", "CHF"])
        self.fcurrency_combobox.grid(row=1, column=1, padx=30, pady=30)

        self.tcurrency_label = ttk.Label(root, text="To Currency:",font=("Arial", 15))
        self.tcurrency_label.grid(row=2, column=0, padx=30, pady=30)

        self.tcurrency_combobox = ttk.Combobox(root, values=["INR", "USD", "EUR", "GBP", "JPY", "CAD", "AUD", "CNY", "HKD", "SGD", "NZD", "CHF"])
        self.tcurrency_combobox.grid(row=2, column=1, padx=30, pady=30)

        self.con_button = ttk.Button(root, text= "Convert", width=30, command=self.conversion)
        self.con_button.grid(row=3, columnspan=2, padx=30, pady=30)

        self.result_label = ttk.Label(root, text="")
        self.result_label.grid(row=4, columnspan=2, padx=30, pady=30)

    def conversion(self):
        amount = float(self.amount_entry.get())
        fcurrency = self.fcurrency_combobox.get()
        tcurrency = self.tcurrency_combobox.get()

        try:
            converted_amount = con_currency(amount, fcurrency, tcurrency)
            self.result_label.config(text=f"{amount:.2f} {fcurrency} is equal to {converted_amount:.2f} {tcurrency}",font=("Arial", 20))
        except ValueError as e:
            self.result_label.config(text=str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
