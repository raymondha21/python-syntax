def print_upper_words(words):
    """Given a list of words, print each word on separate line in all uppercase"""

    for word in words:
        print (word.upper())

def print_upper_words2(words):
    """Given a list of words, print each word starting with the letter "E" on separate line in all uppercase"""

    for word in words:
        if word[0].upper() == "E":
            print (word.upper())

def print_upper_words3(words,letters):
    """Given a list of words, print each word starting with the given letter on separate line in all uppercase"""

    for word in words:
        for letter in letters:
            if (word[0].upper()) == letter.upper():
                print (word.upper())