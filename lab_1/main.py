"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""


def calculate_frequences(text: str) -> dict:
    if isinstance(text, str):
        text = "It is8 w&hat it( is"
        new_text = " "
        stop_marks = ['.', ',', ':', '"', '`', '[', ']', '?', '!', '@',
                      '&', "'", '-', '$', '^', '*', '(', ')', '_', '“',
                      '”', '’', '#', '%', '<', '>', '*', '~', '0', '1',
                      '2', '3', '4', '5', '6', '7', '8', '9', '\n']
        for item in text:
            if not item in stop_marks:
                new_text += item
        new_text = new_text.lower().split()
        # print(sep_text)

        frequency_word = {}
        for i in new_text:
            count = frequency_word.get(i, 0)
            frequency_word[i] = count + 1
            return (frequency_word)


def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:
    dictionary_stop = {}
    dictionary_stop = frequency_word.copy()
    stop_words = ['it', 'what']
    if dictionary_stop is not None and stop_words is not None:
        for k in stop_words:
            if k in dictionary_stop.keys():
                del dictionary_stop[k]
                return (dictionary_stop)


def get_top_n(frequencies: dict, top_n: int) -> tuple:
    """
    Takes first N popular words
    """
    pass
