from lib.decorators import *


@clean_data_decorator
def get_count_words(sentence: str) -> list:
    """
        split a string by blank spaces and check how many times words repeat.
        :param sentence:  Sentece of type string
        :return: list of tuples with no particular order, must be cleaned by the decorator.
    """
    word_count_list = []
    sentece_split = sentence.split(' ')
    sentece_unique_values = set(sentece_split)
    word_count_list = [(x, sentece_split.count(x)) for x in sentece_unique_values]
    return word_count_list


if __name__ == '__main__':
    print(get_count_words("el perro es muy grande y el gato es muy pequeño"))
