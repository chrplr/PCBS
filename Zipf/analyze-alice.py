import string


def remove_punctuation(text):
    punct = string.punctuation + chr(10)
    return text.translate(str.maketrans(punct, " " * len(punct)))


textori = open('alice.txt').read().lower()
text = remove_punctuation(textori)
words = text.split()
print(words)
