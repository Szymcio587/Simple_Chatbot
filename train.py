import json
import words

allWords = []
tags = []
xy = []
XTrain = []
YTrain = []

def LoadData():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data

def InterpretData():
    global tags
    data = LoadData()
    for response in data['responses']:
        tag = response['tag']
        tags.append(tag)
        for pattern in response['patterns']:
            w = words.Tokenize(pattern)
            allWords.extend(w)
            xy.append((w, tag))

    ignoreWords = ['?', '!', '.', ',']
    all_words = [words.Stem(w) for w in allWords if w not in ignoreWords]
    all_words = sorted(set(all_words))
    tags = sorted(set(tags))

    #print(len(xy), "patterns")
    #print(len(tags), "tags:", tags)
    #print(len(all_words), "unique stemmed words:", all_words)

    CreateTrainingData()

def CreateTrainingData():
    X_train = []
    y_train = []
    for (pattern_sentence, tag) in xy:
        bag = words.BagOfWords(pattern_sentence, allWords)
        X_train.append(bag)
        label = tags.index(tag)
        y_train.append(label)

