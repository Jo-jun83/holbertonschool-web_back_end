#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Dataset indexed by sorting position, starting at 0
        """
        data = self.indexed_dataset()

        assert index is not None, "Index cannot be None"
        assert index >= 0, "Index must be a non-negative integer"
        assert index < len(data), "Index is out of range"

        current_page = []
        current_idx = index
        page_count = 0

        while page_count < page_size and current_idx < len(data):
            if current_idx in data:
                current_page.append(data[current_idx])
                page_count += 1
            current_idx += 1

        next_index = current_idx

        return {
            'index': index,
            'data': current_page,
            'page_size': page_size,
            'next_index': next_index
        }
