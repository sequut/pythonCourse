import tkinter as tk
from tkinter import messagebox, Scrollbar
from B.parser.news_parser import NewsParser
from B.analyzer.sentiment_analyzer import SentimentAnalyzer

class NewsApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("RIA News Sentiment Analyzer")
        self.root.geometry("600x500")

        self.get_news_button = tk.Button(self.root, text="Получить новости", command=self.get_news)
        self.get_news_button.pack(pady=10)

        self.analyze_button = tk.Button(self.root, text="Проанализировать тональность", command=self.analyze_sentiment)
        self.analyze_button.pack(pady=10)

        self.news_listbox = tk.Listbox(self.root, width=80, height=15)
        self.news_listbox.pack(pady=10)

        self.scrollbar = Scrollbar(self.root, orient="vertical", command=self.news_listbox.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.news_listbox.config(yscrollcommand=self.scrollbar.set)

        self.news = []
        self.sentiment_analyzer = SentimentAnalyzer()

    def get_news(self):
        news_parser = NewsParser('https://ria.ru/world/')
        self.news = news_parser.parse_news()

        if not self.news:
            messagebox.showerror("Ошибка", "Не удалось получить новости")
            return

        self.news_listbox.delete(0, tk.END)
        for sample in self.news:
            self.news_listbox.insert(tk.END, sample['title'], sample['link'])

    def analyze_sentiment(self):
        if not self.news:
            messagebox.showerror("Ошибка", "Нет новостей для анализа")
            return

        results = []
        for sample in self.news:
            text = sample['title']
            if text:
                sentiment = self.sentiment_analyzer.analyze(text)
                results.append(f"{text}: {sentiment}")

        result_window = tk.Toplevel(self.root)
        result_window.title("Результаты анализа")
        result_window.geometry("500x400")

        result_text = tk.Text(result_window, wrap="word")
        result_text.pack(expand=True, fill="both")
        result_text.insert(tk.END, "\n".join(results))
        result_text.config(state=tk.DISABLED)

    def run(self):
        self.root.mainloop()