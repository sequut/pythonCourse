import tkinter as tk
from tkinter import ttk, messagebox
from .cb_api import fetch_cbr_rates
from .parser import parse_cbr_xml

class CurrencyApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Курсы валют ЦБ РФ")
        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.root, columns=('code', 'name', 'value', 'nominal'), show='headings')
        self.tree.heading('code', text='Код')
        self.tree.heading('name', text='Валюта')
        self.tree.heading('value', text='Курс к рублю')
        self.tree.heading('nominal', text='Номинал')

        self.tree.column('code', width=80)
        self.tree.column('name', width=200)
        self.tree.column('value', width=100)
        self.tree.column('nominal', width=80)

        self.tree.pack(fill=tk.BOTH, expand=True)

    def load_data(self):
        try:
            xml = fetch_cbr_rates()
            data = parse_cbr_xml(xml)
            for item in data:
                self.tree.insert('', tk.END, values=(item['code'], item['name'], item['value'], item['nominal']))
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def run(self):
        self.root.mainloop()