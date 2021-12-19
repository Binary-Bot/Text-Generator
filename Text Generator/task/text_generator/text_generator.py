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
    generatePseudo(model)

def generatePseudo(model):
    currentWord = random.choice(list(model.keys()))
    for i in range(10):
        for j in range(10):
            print(currentWord, end=" ")
            currentWord = random.choices(population=list(model[currentWord].keys()), weights=list(model[currentWord].values()))[0]
        print()

main()
