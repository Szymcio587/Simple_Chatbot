import nltk
from nltk.stem.porter import PorterStemmer

#nltk.download('punkt')

def Tokenize(sentence):
    return nltk.word_tokenize(sentence)

def Stem(word):
    stemmer = PorterStemmer()
    return stemmer.stem(word.lower())

def BagOfWords(allWords, tokenizedSentence):
    pass