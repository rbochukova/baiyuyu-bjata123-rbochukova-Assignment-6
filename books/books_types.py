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

    def __init__(self, title:str, author: str, rating: float = 0, reviews:int = 0, price:float = 0, years=list[int], genre:str) -> None:
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
        self.years: List = years
        self.genre: str = genre

