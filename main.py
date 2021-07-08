# import libraries
import re
import sys
import functions
import unidecode
import requests
from bs4 import BeautifulSoup

# specify the url
url = 'https://www.hplovecraft.com/writings/texts/fiction/mm.aspx'

# setting our translation conditions
translation = {ord('—'): ' ', ord('′'): None, ord("”"): ".", ord("“"): None}

# query the website and return the html to the variable 'response'
response = requests.get(url)

# checking if we get a response from the website before continue
if response.ok:

    # parse the html using beautiful soup and store in variable 'soup'
    soup = BeautifulSoup(response.text,features="html.parser")

    # select the part we need in the html, here the division with the book content
    book = soup.find('div', attrs={"align": "justify"})

    # get the text without tags
    book = book.getText()
    # using the translation to replace wrong characters selected before
    book = book.translate(translation)
    book = unidecode.unidecode(book)

    # first split to get the chapters
    chapters = book.split(".\r\n\r\n")

    # using the chapters to get paragraphs
    paragraphs = [ele.split(".\n") for ele in chapters]

    # launching the main loop to ask until the answer is correct with our conditions
    while __name__ == "__main__":
        choice = input("Consulter le nombre de lettres (1) ou le nombre de mots (2) ? \n")
        if choice == '1':
            functions.letters_counter(chapters, paragraphs)
            exit(0)
        if choice == '2':
            functions.words_counter(chapters, paragraphs)
            exit(0)



