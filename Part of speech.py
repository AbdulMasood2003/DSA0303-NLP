from nltk.tokenize import word_tokenize
from nltk  import pos_tag
import nltk
text="this is my pen"
words=word_tokenize(text)
print(words)
tag1=pos_tag(words)
print(tag1)