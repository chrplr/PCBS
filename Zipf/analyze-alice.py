import string
import word_count
import matplotlib.pyplot as plt

def remove_punctuation(text):
    punct = string.punctuation + chr(10)
    return text.translate(str.maketrans(punct, " " * len(punct)))


textori = open('alice.txt', 'r').read().lower()
text = remove_punctuation(textori)
words = text.split()

wc = word_count.frequency_table(words)
word_count.zipf_plot(wc, logx=True, logy=True)
plt.show()

b = word_count.frequency_spectrum(words)
print('Frequency spectrum:')
print(b)

plt.plot(b.counts, b.ntypes, '-o')
plt.title('Frequency spectrum')
plt.show()

