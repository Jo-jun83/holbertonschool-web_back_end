#!/usr/bin/env python3
"""This module provides a helper function for calculating the start
and end indices for pagination."""
import csv
import math
from typing import Tuple, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page of the dataset.
        """
        assert isinstance(page, int) and page > 0, \
            "page doit être un entier positif"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size doit être un entier positif"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        return dataset[start_index:end_index]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices for pagination.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
