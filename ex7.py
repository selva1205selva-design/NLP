import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def pos_tagging(text):
    words = word_tokenize(text)
    pos_tags = pos_tag(words)
    return pos_tags

example_text = "My name is Gokul"

pos_tags = pos_tagging(example_text)

print("Word\tPOS Tag")
print("-----------------")
for word, tag in pos_tags:
    print(word, "\t", tag)