"""
Labour work #2. Levenshtein distance.
"""


def generate_edit_matrix(num_rows: int, num_cols: int) -> list:
    column = []
    matrix = []
    while num_cols > 0:
        column.append(0)
        num_cols = num_cols - 1
    while num_rows > 0:
        matrix.append(column)
        num_rows = num_rows - 1
        return(matrix)


def initialize_edit_matrix(edit_matrix: tuple, add_weight: int, remove_weight: int) -> list:
    pass


def minimum_value(numbers: tuple) -> int:
    pass


def fill_edit_matrix(edit_matrix: tuple,
                     add_weight: int,
                     remove_weight: int,
                     substitute_weight: int,
                     original_word: str,
                     target_word: str) -> list:
    pass


def find_distance(original_word: str,
                  target_word: str,
                  add_weight: int,
                  remove_weight: int,
                  substitute_weight: int) -> int:
    pass
