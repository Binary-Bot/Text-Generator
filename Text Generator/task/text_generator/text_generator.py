# Write your code here
import nltk
from nltk.tokenize import WhitespaceTokenizer

def main():
    fileName = input("Enter the file name: ")
    with open(fileName, encoding="utf-8") as inFile:
        text = inFile.read()
        tokens = WhitespaceTokenizer().tokenize(text)
        bigrams = list(nltk.bigrams(tokens))
        print("Number of bigrams: ", len(bigrams))
        getToken(bigrams)

def getToken(bigrams):
    index = input()
    if index != "exit":
        try:
            index = int(index)
            print(f"Head: {bigrams[index][0]} \t\t Tail: {bigrams[index][1]}")
        except ValueError:
            print("Type Error. Please input an integer.")
        except IndexError:
            print("Index Error. Please input an integer that is in the range of corpus.")
        finally:
            getToken(bigrams)


main()

