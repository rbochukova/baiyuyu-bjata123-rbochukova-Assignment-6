"""
XB_0082: Bestselling Books
Author: Emanuela Dumitru

Copyright (c) 2021-2022 - Eindhoven University of Technology - VU Amsterdam, The Netherlands
This software is made available under the terms of the MIT License.
"""

from typing import Dict, List
import csv
import statistics

from books.books_utils import get_absolute_path


class Book:
    """
    """

    FICTION: str = 'Fiction'
    NON_FICTION: str = 'Non Fiction'
    recommended = False

    def __init__(self, title, author, rating, reviews, price, years, genre) -> None:
        """
        Initializes a Book object.
        :param title: string value for title of book
        :param author: string value for title of book
        :param rating: string value for title of book
        :param reviews: string value for title of book
        :param price: string value for title of book
        :param years: list of integers
        :param genre: string value for genre
        """

        self.title: str = title
        self.author: str = author
        self.rating: float = rating
        self.reviews: int = reviews
        self.price: float = price
        self.years: list = years
        self.genre: str = genre

    def __str__(self) -> str:
        """
        Returns the string representation of a Book object.
        :returns: string representation of the Book object.
        """
        return f"{self.title}"

    def recommend(self,ratingtst:int, reviewstst:int) -> None:
        if self.rating >= ratingtst and self.reviews >= reviewstst:
            Book.recommended = True
        else:
            Book.recommended = False


class Amazon:
    """
    Contains a list of bestselling books.
    """

    def __init__(self, bestsellers: list) ->None:
        """
        """
        self.bestsellers: list = bestsellers

    def read_books_csv(path: str) -> None:
        """
        """
        entry:Dict = {}
        res: Dict = {}
        name = ''
        dataset = []
        with open(path, encoding='utf-8-sig') as CSV_file:
            reader = csv.DictReader(CSV_file, delimiter=";")

            # title = row[0]
            # author = row[1]
            # rating = line[2]
            # reviews = line[3]
            # price = line[4]
            # years = line[5]
            # genre = line[6]
            #print(Book(title, author, rating, reviews, price, years, genre))

            for dct in reader:
                for key, value in dct.items():
                    line = key.split(',')
                    row = value.split(',')

                for i in range(len(dct)):
                    for j in range(len(line) - 1):
                        entry.update({line[i]:row[i]})
                        i +=1
                    j += 1
                for k, v in entry.items():
                    if (k == 'User Rating' or k == 'Price') and v == float:
                        v = float(v)
                    if k == 'Reviews' and v.isdigit():
                        v = int(v)
                    if k == 'Name':
                        print(entry[k])
                    res.update({k:v})

    # def recommend_book(ratingtst:int, reviewstst:int) -> None:


Amazon.read_books_csv(get_absolute_path('data/books.csv'))

class FictionBook(Book):
    """
    """

    def __init__(self, title, author, rating, reviews, price, years, genre=Book.FICTION) -> None:
        """
        """
        Book.__init__(self, title, author, rating, reviews, price, years, genre)

    def __str__(self) -> str:
        """
        """
        for i in self.years:
            return f"{self.title}: {self.genre} ({i})"


class NonFictionBook(Book):
    """
    """

    def __init__(self, title, author, rating, reviews, price, years, genre=Book.NON_FICTION) -> None:
        """
        """
        Book.__init__(self, title, author, rating, reviews, price, years, genre)

    def __str__(self) -> str:
        """
        Returns the string representation of a Book object.
        :returns: string representation of the Book object.
        """
        for i in self.years:
            return f"{self.title}: {self.genre} ({i})"
