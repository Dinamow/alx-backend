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
            """ Finds the correct indexes to paginate dataset correctly
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
            return [] if wanted_index[0] >= len(all_data) else all_data[wanted_index[0]: wanted_index[1]]


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
