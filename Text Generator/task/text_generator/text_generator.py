import nltk
from nltk.tokenize import WhitespaceTokenizer
from collections import defaultdict, Counter

def main():
    fileName = input("Enter the file name: ")
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
    getToken(model)

def getToken(model):
    index = input()
    if index != "exit":
        try:
            print(f"Head: {index}")
            for key, value in model[index].items():
                print(f"Tail: {key} \t Count: {value}")
            print()
        except KeyError:
            print("Key Error. The requested word is not in the model. Please input another word.\n")
        finally:
            getToken(model)


main()

