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

    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0) -> None:
        """
        Initializes a Time object.
        :param hour: integer value for hour
        :param minute: integer value for minute
        :param second: integer value for second
        """
        self.hour: int = hour
        self.minute: int = minute
        self.second: int = second