# Write your code here
from nltk.tokenize import WhitespaceTokenizer
from nltk.probability import FreqDist

def main():
    fileName = input("Enter the file name: ")
    with open(fileName, encoding="utf-8") as inFile:
        text = inFile.read()
        tokens = WhitespaceTokenizer().tokenize(text)
        freq = FreqDist(tokens)
        print("Corpus statistics")
        print("All tokens: ", len(tokens))
        print("Unique tokens: ", len(set(tokens)))
        getToken(tokens)

def getToken(tokens):
    index = input()
    if index != "exit":
        try:
            index = int(index)
            print(tokens[index])
        except ValueError:
            print("Type Error. Please input an integer.")
        except IndexError:
            print("Index Error. Please input an integer that is in the range of corpus.")
        finally:
            getToken(tokens)


main()

