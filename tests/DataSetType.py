from enum import Enum


class DataSetType(Enum):
    RANDOM = 1  # elements are completely random
    UNIQUE_RANDOM = 2  # elements are random but all unique
    ORDERED = 3  # elements are an ordered set from 1 to size
    REVERSED = 4  # like ORDERED but elements are reversed
