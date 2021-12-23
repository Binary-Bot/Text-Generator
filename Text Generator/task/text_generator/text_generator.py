import re
import nltk
import random
from nltk.tokenize import WhitespaceTokenizer
from collections import defaultdict, Counter

def main():
    fileName = input()
    with open(fileName, encoding="utf-8") as inFile:
        text = inFile.read()
        tokens = WhitespaceTokenizer().tokenize(text)
        trigrams = list(nltk.trigrams(tokens))

    model = {}
    headTail = defaultdict(list)
    for pair in trigrams:
        headTail[pair[0] + " " + pair[1]].append(pair[2])
    for key, value in headTail.items():
        model[key] = Counter(value)
    generatePseudo(model, text)

def generatePseudo(model, text):
    r = re.compile("([A-Z]\w*)\s")
    capitalLetters = list(filter(r.match, model.keys()))
    for i in range(10):
        currentWord = random.choice(capitalLetters)
        sentence = ""
        sentence = generateASentence(sentence, currentWord, capitalLetters, model)
        print(sentence)

def generateASentence(sentence, currentWord, capitalLetters, model):
    while True:
        word = currentWord.split()
        sentence += word[0] + " "
        if currentWord[-1] in ".?!":
            if len(sentence.split()) > 3:
                break
            else:
                try:
                    currentWord = word[1] + " " + random.choice(list(set(capitalLetters).intersection(set(model[currentWord].keys()))))
                except IndexError:
                    currentWord = word[1] + " " + random.choices(population=list(model[currentWord].keys()), weights=list(model[currentWord].values()))[0]
                finally:
                    continue
        currentWord = word[1] + " " + random.choices(population=list(model[currentWord].keys()), weights=list(model[currentWord].values()))[0]
    sentence += currentWord.split()[1]
    return sentence
main()