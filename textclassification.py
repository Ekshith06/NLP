import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

class TextClassificationGUI:

    def __init__(self, master):
        self.master = master
        master.title("Text Classification")

        self.file_path = tk.StringVar()
        self.classification_result = tk.StringVar()

        self.label = tk.Label(master, text="Select a text file to classify:")
        self.label.pack()

        self.browse_button = tk.Button(master, text="Browse", command=self.browse_file)
        self.browse_button.pack()

        self.classify_button = tk.Button(master, text="Classify", command=self.classify_text)
        self.classify_button.pack()

        self.result_label = tk.Label(master, textvariable=self.classification_result)
        self.result_label.pack()

    def browse_file(self):
        self.file_path.set(filedialog.askopenfilename(filetypes=[("Text files", "*.txt")]))
        if self.file_path.get() == "":
            messagebox.showerror("Error", "Please select a file")

    def classify_text(self):
        if self.file_path.get() == "":
            messagebox.showerror("Error", "Please select a file")
            return
        try:
            with open(self.file_path.get(), "r") as f:
                text = f.read()
        except:
            messagebox.showerror("Error", "Could not read file")
            return

        vectorizer = CountVectorizer(stop_words="english")
        X = vectorizer.fit_transform([text])

        clf = MultinomialNB()
        clf.fit(X, [0])

        y_pred = clf.predict(X)

        if y_pred[0] == 0:
            self.classification_result.set("The text is negative")
        else:
            self.classification_result.set("The text is positive")

root = tk.Tk()
gui = TextClassificationGUI(root)
root.mainloop()
