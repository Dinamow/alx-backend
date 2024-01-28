#!/usr/bin/env python3
"""
    index_range function file for pagination
"""


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
