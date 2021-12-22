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
        bigrams = list(nltk.bigrams(tokens))

    model = {}
    headTail = defaultdict(list)
    for pair in bigrams:
        headTail[pair[0]].append(pair[1])
    for key, value in headTail.items():
        model[key] = Counter(value)
    generatePseudo(model, text)

def generatePseudo(model, text):
    capitalLetters = re.findall("([A-Z]\w*)\s", text)
    # punctuatedLetters = re.findall(f"\w*[.?!]", text)
    for i in range(10):
        currentWord = random.choice(capitalLetters)
        sentence = ""
        sentence = generateASentence(sentence, currentWord, capitalLetters, model)
        print(sentence)

def generateASentence(sentence, currentWord, capitalLetters, model):
    while True:
        sentence += currentWord + " "
        if currentWord[-1] in ".?!":
            if len(sentence.split()) > 4:
                break
            else:
                try:
                    currentWord = random.choice(list(set(capitalLetters).intersection(set(model[currentWord].keys()))))
                except IndexError:
                    currentWord = random.choices(population=list(model[currentWord].keys()), weights=list(model[currentWord].values()))[0]
                finally:
                    continue
        currentWord = random.choices(population=list(model[currentWord].keys()), weights=list(model[currentWord].values()))[0]

    return sentence
main()