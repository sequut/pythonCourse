import tkinter as tk
from tkinter import messagebox
from note import Note

class NoteAppGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Менеджер Заметок")
        self._build_interface()

    def _build_interface(self):
        tk.Label(self.root, text="Название заметки:").pack()
        self.entry_title = tk.Entry(self.root)
        self.entry_title.pack()

        tk.Label(self.root, text="Текст заметки:").pack()
        self.text_content = tk.Text(self.root, height=10, width=40)
        self.text_content.pack()

        tk.Button(self.root, text="Создать/Сохранить", command=self.create_note).pack(pady=2)
        tk.Button(self.root, text="Открыть", command=self.open_note).pack(pady=2)
        tk.Button(self.root, text="Удалить", command=self.delete_note).pack(pady=2)

    def create_note(self):
        title = self.entry_title.get()
        content = self.text_content.get("1.0", tk.END).strip()
        if not title or not content:
            messagebox.showwarning("Внимание", "Введите заголовок и текст")
            return
        note = Note(title, content)
        note.save_to_file()
        messagebox.showinfo("Успех", f"Заметка '{title}' сохранена")

    def open_note(self):
        title = self.entry_title.get()
        try:
            note = Note.load_from_file(title)
            self.text_content.delete("1.0", tk.END)
            self.text_content.insert(tk.END, note.content)
            messagebox.showinfo("Успех", f"Заметка '{title}' загружена")
        except:
            messagebox.showerror("Ошибка", "Файл не найден")

    def delete_note(self):
        title = self.entry_title.get()
        try:
            note = Note.load_from_file(title)
            note.delete_file()
            self.text_content.delete("1.0", tk.END)
            messagebox.showinfo("Успех", f"Заметка '{title}' удалена")
        except:
            messagebox.showerror("Ошибка", "Файл не найден")

    def run(self):
        self.root.mainloop()
