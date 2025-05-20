import os
import string
from collections import Counter

def clean_text(text):
    text = text.lower()
    return text.translate(str.maketrans("", "", string.punctuation))

def count_words(file_path, top_n=5):
    if not os.path.exists(file_path):
        print(f"{file_path} does not exist. Please create it.")
        with open(file_path, "w") as f:
            paragraph = input("Enter a paragraph to create the file: ")
            f.write(paragraph)

    with open(file_path, "r") as f:
        text = f.read()

    cleaned = clean_text(text)
    words = cleaned.split()
    total_words = len(words)

    word_counts = Counter(words)
    top_words = word_counts.most_common(top_n)

    print(f"\nTotal words: {total_words}")
    print(f"Top {top_n} most common words:")
    for word, count in top_words:
        print(f"{word} - {count} times")

    with open("word_count_report.txt", "w") as report:
        report.write("Word Count Report\n")
        report.write(f"Total Words: {total_words}\n")
        report.write(f"Top {top_n} Words:\n")
        for word, count in top_words:
            report.write(f"{word} - {count}\n")