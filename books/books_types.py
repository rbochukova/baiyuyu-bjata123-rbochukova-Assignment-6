"""
XB_0082: Bestselling Books
Author: Emanuela Dumitru

Copyright (c) 2021-2022 - Eindhoven University of Technology - VU Amsterdam, The Netherlands
This software is made available under the terms of the MIT License.
"""

from typing import Dict, List
import csv
import statistics


class Book:
    """
    """

    FICTION: str = 'Fiction'
    NON_FICTION: str = 'Non Fiction'

    def __init__(self, title: str, author: str, rating: float = 0.0, reviews: int = 0, price: float = 0.0, years=list,
                 genre=str) -> None:
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


class Amazon:
    """
    Contains a list of bestselling books.
    """

    def __init__(self, bestsellers: list):
        self.bestsellers: list = bestsellers

#
# class FictionBook(Book):
#     """
#     """
#
#     def __init__(self, title, author, rating, reviews, price, years, genre) -> None:
#         """
#         """
#         self.genre = genre
#         genre = Book.FICTION
#         genre = Book.NON_FICTION
#         Book.__init__(self, title, author, rating, reviews, price, years, genre)
#
#     def __str__(self) -> str:
#         """
#         """
#         return f"{self.title}: {self.genre} {self.years}."
#
#
# class NonFictionBook(Book):
#     """
#     """
#
#     def __init__(self, title, author, rating, reviews, price, years, genre) -> None:
#         """
#         """
#         Book.__init__(self, title, author, rating, reviews, price, years, genre)
#         self.genre = genre
#         genre = Book.FICTION
#         genre = Book.NON_FICTION
#
#     def __str__(self) -> str:
#         """
#         Returns the string representation of a Book object.
#         :returns: string representation of the Book object.
#         """
#         return f"{self.title}: {self.genre} {self.years}."
