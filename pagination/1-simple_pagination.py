#!/usr/bin/env python3
"""
Module to paginate a dataset of popular baby names.
"""


import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
        Calculate the start and end indexes for pagination.

        Given a page number and the number of items per page, this function
        returns a tuple containing the start index (inclusive) and the end
        index (exclusive) to be used for slicing a dataset.

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            tuple: A tuple of two integers (start_index, end_index)
            representing the range of items for the given page.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a list of rows corresponding to
        the requested page and page size.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: The list of rows for the page or
            an empty list if out of range.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()
        page_data = data[start:end]

        return page_data
