class WordCount:
    def __init__(self, words):
        self.words = words

    def countWords(self, wordInput):
        wordcount = 0
        for i in wordInput:
            if i == ' ':
                wordcount += i
            
        self.words == wordcount

wordInput = input("Input words to count: ", )

words = WordCount(0).countWords(wordInput)