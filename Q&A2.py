import openai
from transformers import pipeline
import tkinter as tk
openai.api_key = "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"
qa_pipeline = pipeline('question-answering', model='distilbert-base-cased-distilled-squad', tokenizer='distilbert-base-cased')
contexts = ["Context 1", "Context 2", "Context 3"]
def get_answer():
    question = question_entry.get()
    search_results = openai.Completion.create(engine="davinci", prompt=f"Please provide some context for the question: {question}", max_tokens=100)
    context = search_results["choices"][0]["text"]
    answer = qa_pipeline({'question': question, 'context': context})
    if not answer['answer']:
        for c in contexts:
            answer = qa_pipeline({'question': question, 'context': c})
            if answer['answer']:
                break
    if not answer['answer']:
        answer_label.config(text="I'm sorry, I couldn't find an answer to that question. Please try asking a more specific question or providing more context.")
    else:
        answer_label.config(text=answer['answer'])
    question_entry.delete(0, tk.END)
root = tk.Tk()
root.title("Question Answering System")
question_label = tk.Label(root, text="Please enter your question:")
question_label.pack(side=tk.TOP)
question_entry = tk.Entry(root, width=50)
question_entry.pack(side=tk.TOP)
submit_button = tk.Button(root, text="Submit", command=get_answer)
submit_button.pack(side=tk.TOP)
answer_label = tk.Label(root, text="")
answer_label.pack(side=tk.TOP)
root.mainloop()
