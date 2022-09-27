import random

def puzzled(score: int, word: str) -> int:
    word1 = random.sample(word, k=len(word))
    word1 = ''.join(word1)
    print()
    print('Arrange the following to form meaningfull Word')
    print(word1)
    userInput = input()

    if userInput.upper() == word:
        print('Correct')
        score += 1
    else:
        print('Wrong')
        score -= 1
    return score


def mainFun():
    score = 0
    words = ['SCHOOL', 'COLLEGE', 'INDIA', 'MUMBAI']

    words = random.sample(words, k=len(words))
    print(words)

    for word in words:
        score = puzzled(score, word)

    print('Your score :', score)


mainFun()
