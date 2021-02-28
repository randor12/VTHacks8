import string
import argparse

def process(newspaper_array):
    with open("models/testfile.txt", "w", encoding="utf-8") as f:
        for entry in newspaper_array:
            entry = entry.translate(str.maketrans('', '', string.punctuation))
            if (entry is not None):
                f.write(entry + ".\n")
    f.close()
