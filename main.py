import words
import train

if __name__ == "__main__":
    sentence = "This is an example sentence."
    print(sentence)
    train.LoadData()
    print(words.Tokenize(sentence))
