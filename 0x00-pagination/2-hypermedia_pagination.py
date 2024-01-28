#!/usr/bin/env python3
"""
    Server class file for pagination
"""
import csv
import math
from typing import List


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
            Finds the correct indexes to paginate dataset correctly
            and return the appropriate page of the dataset
            Args:
                page: int
                page_size: int
            Return:
                List[List]:
        """

        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        all_data = self.dataset()
        wanted_index = index_range(page, page_size)
        return [] if wanted_index[0] >= len(all_data) else\
            all_data[wanted_index[0]: wanted_index[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
            dictionary containing the following key-value pairs:

            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer

            Args:
                page: int
                page_size: int
            Return:
                dict
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        values = {
            'page_size': page_size,
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
        return values


def index_range(page: int, page_size: int) -> tuple:
    """
        Return a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters.
        Page numbers are 1-indexed, i.e. the first page is page 1.
        Returns:
            tuple: (start_index, end_index)
    """
    start_index: int = (page - 1) * page_size
    end_index: int = page * page_size
    return (start_index, end_index)
