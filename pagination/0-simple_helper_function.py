#!/usr/bin/env python3
"""
    Calculate the start and end indexes for pagination.
"""


def index_range(page: int, page_size: int) -> tuple:
    """

    Given a page number and the number of items per page, this function
    returns a tuple containing the start index (inclusive) and the end
    index (exclusive) to be used for slicing a dataset.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple of two integers (start_index, end_index) representing
        the range of items for the given page.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
