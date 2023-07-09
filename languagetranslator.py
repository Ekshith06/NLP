from googletrans import LANGUAGES, Translator
import tkinter as tk
from tkinter import ttk

class TranslatorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x150")
        self.root.title("Language Translator")
        self.input_label = tk.Label(self.root, text="Input Text:")
        self.input_label.pack()
        self.input_text = tk.Text(self.root, height=5)
        self.input_text.pack()
        self.input_combo_label = tk.Label(self.root, text="Select Input Language:")
        self.input_combo_label.pack()
        self.input_combo = ttk.Combobox(self.root, values=list(LANGUAGES.values()))
        self.input_combo.current(0)
        self.input_combo.pack()
        self.output_combo_label = tk.Label(self.root, text="Select Output Language:")
        self.output_combo_label.pack()
        self.output_combo = ttk.Combobox(self.root, values=list(LANGUAGES.values()))
        self.output_combo.current(1)
        self.output_combo.pack()
        self.output_label = tk.Label(self.root, text="Output Text:")
        self.output_label.pack()
        self.output_text = tk.Text(self.root, height=5)
        self.output_text.pack()
        self.translate_button = tk.Button(self.root, text="Translate", command=self.translate)
        self.translate_button.pack()
        self.root.mainloop()

    def translate(self):
        input_lang = [k for k, v in LANGUAGES.items() if v == self.input_combo.get()][0]
        output_lang = [k for k, v in LANGUAGES.items() if v == self.output_combo.get()][0]
        input_text = self.input_text.get("1.0", "end-1c")
        translator = Translator()
        output_text = translator.translate(input_text, src=input_lang, dest=output_lang).text
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", output_text)

if __name__ == "__main__":
    app = TranslatorApp()
