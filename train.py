import json
import words


def LoadData():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data

def InterpretData():
    data = LoadData()
    allWords = []
    tags = []
    xy = []
    for response in data['responses']:
        tag = response['tag']
        tags.append(tag)
        for pattern in response['patterns']:
            w = words.Tokenize(pattern)
            allWords.extend(w)
            xy.append((w, tag))

ignoreWords = ['?', '!', '.', ',']