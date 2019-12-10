"""
Labour work #3
 Building an own N-gram model
"""

import math

REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()


class WordStorage:
    def put(self, word: str) -> int:
        pass

    def get_id_of(self, word: str) -> int:
        pass

    def get_original_by(self, id: int) -> str:
        pass

    def from_corpus(self, corpus: tuple):
        pass


class NGramTrie:
    def fill_from_sentence(self, sentence: tuple) -> str:
        pass

    def calculate_log_probabilities(self):
        pass

    def predict_next_sentence(self, prefix: tuple) -> list:
        pass


def encode(storage_instance, corpus) -> list:
    pass


def split_by_sentence(text: str) -> list:
    #gonna clear the text from symbols
    if text is " " or text is None:
        text_new = []
    else:
        forbidden_symbols = ['`', '~', '@', '', '#',
                             '№', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']',
                             '<', '>', '/', '|', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\n']
        punctuation = ['!', '?', '.', ',', ':', ';', '...', '?!', '!?', '?..', '!..']
        text_new = [i for i in text if i not in forbidden_symbols and i[0] is not '!']
        text_new = ''.join(text_new)
        text_new = text_new.split(".")
        text_new = [i for i in text_new if i is not '']
        print(text_new)
    return(text_new)

split_by_sentence(REFERENCE_TEXT)

