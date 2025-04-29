import tkinter as tk
from tkinter import ttk, messagebox

from annuity import AnnuityPayment
from differentiated import DifferentiatedPayment


class LoanGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ипотечный калькулятор")

        tk.Label(self.root, text="Сумма кредита:").grid(row=0, column=0, sticky="e")
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Ставка (% годовых):").grid(row=1, column=0, sticky="e")
        self.rate_entry = tk.Entry(self.root)
        self.rate_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Срок (лет):").grid(row=2, column=0, sticky="e")
        self.term_entry = tk.Entry(self.root)
        self.term_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Тип платежа:").grid(row=3, column=0, sticky="e")
        self.payment_type = ttk.Combobox(self.root, values=["Аннуитетный", "Дифференцированный"])
        self.payment_type.current(0)
        self.payment_type.grid(row=3, column=1)

        tk.Button(self.root, text="Рассчитать", command=self.calculate).grid(row=4, columnspan=2, pady=10)

        self.tree = ttk.Treeview(self.root, columns=("Месяц", "Платеж", "Проценты", "Долг", "Остаток"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")
        self.tree.grid(row=5, column=0, columnspan=2, sticky="nsew")

    def calculate(self):
        try:
            amount = float(self.amount_entry.get())
            rate = float(self.rate_entry.get())
            term = int(self.term_entry.get())
            p_type = self.payment_type.get()

            if p_type == "Аннуитетный":
                calc = AnnuityPayment(amount, rate, term)
            else:
                calc = DifferentiatedPayment(amount, rate, term)

            schedule = calc.calculate_schedule()

            for item in self.tree.get_children():
                self.tree.delete(item)

            for row in schedule:
                self.tree.insert("", "end", values=(
                    row['month'], row['payment'], row['interest'], row['principal'], row['remaining']
                ))

        except Exception as e:
            messagebox.showerror("Ошибка", f"Проверьте ввод: {e}")

    def run(self):
        self.root.mainloop()