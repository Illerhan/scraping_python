# import libraries
import sys
import re

# setting regular expression
regex = re.compile('[^a-zA-Z]')


# function that count letters in each paragraphs / chapters
def letters_counter(chapters, paragraphs):

    # define our output in the specified file
    sys.stdout = open("letters.txt", "w")

    # loop counters
    x = 1
    y = 0
    # loop into chapters
    while x < len(chapters):
        print("Chapitre " + str(x))
        count = 0
        # loop into paragraphs linked with the chapter
        while y < len(paragraphs[x]) - 1:
            print("Paragraphe " + str(y + 1))
            # using regular expression to clean string and keep only letters
            para = regex.sub('', str(paragraphs[x][y]))
            # using len to determine how much letters in the string (defined by is length)
            print("Nombre de lettres du paragraphe : " + str(len(para)))
            count = count + len(para)
            y = y + 1
        print("\nNombre de lettres du chapitre " + str(count) + "\n")
        y = 0
        x = x + 1
    # return in console output
    sys.stdout = sys.__stdout__
    print("Operation Done")


def words_counter(chapters, paragraphs):
    # define our output in the specified file
    sys.stdout = open("words.txt", "w")

    x = 1
    y = 0
    while x < len(chapters):
        print("Chapitre " + str(x))
        count = 0
        # loop into paragraphs linked with the chapter
        while y < len(paragraphs[x]) - 1:
            print("Paragraphe " + str(y + 1))
            # splitting with no argument to use whitespaces as separators
            para = paragraphs[x][y].split()
            # using len to determine how much letters in the string (defined by is length)
            print("Nombre de mots du paragraphe : " + str(len(para)))
            count = count + len(para)
            y = y + 1

        print("\nNombre de mots du chapitre " + str(count) + "\n")
        y = 0
        x = x + 1
    # return in console output
    sys.stdout = sys.__stdout__
    print("Operation Done")




