#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination server for baby names dataset."""

import csv
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset as a list of lists."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return the dataset indexed by position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
        self, index: int = None, page_size: int = 10
    ) -> Dict[str, Any]:
        """
        Returns a deletion-resilient page of the dataset starting
        from the given index.

        Args:
            index (int): The starting index of the page (default: None)
            page_size (int): Number of items per page (default: 10)

        Returns:
            Dict[str, Any]: Dictionary with index, next_index,
            page_size, and data
        """
        assert index is not None and index >= 0
        indexed_dataset = self.indexed_dataset()
        assert index < len(indexed_dataset)

        data = []
        current = index
        count = 0
        while count < page_size and current < len(indexed_dataset):
            if current in indexed_dataset:
                data.append(indexed_dataset[current])
                count += 1
            current += 1

        next_index = current if current < len(indexed_dataset) else None
        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index
        }
