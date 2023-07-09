import tkinter as tk
from textblob import TextBlob

def extract_sentiment():
    text = text_input.get("1.0", "end-1c")
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        result_label.config(text="Positive")
    elif sentiment == 0:
        result_label.config(text="Neutral")
    else:
        result_label.config(text="Negative")

root = tk.Tk()
root.geometry("400x300")

text_label = tk.Label(root, text="Enter text:")
text_label.pack()

text_input = tk.Text(root, height=8)
text_input.pack()

extract_button = tk.Button(root, text="Extract Sentiment", command=extract_sentiment)
extract_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
