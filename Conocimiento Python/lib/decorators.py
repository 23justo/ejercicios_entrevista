def clean_data_decorator(func):
    """
        Decorator to clean the args passed to the function, making sure we receive a String
        return: list of tuples 
    """
    def wrapper(*args, **kwargs):
        if isinstance(args[0], str):
            "make sure params are str"
            res = func(*args, **kwargs)
            return order_word_count(res)
        else:
            return f'Value {args[0]} must be a String'
    return wrapper

def order_word_count(word_list: list) -> list:
    """
        function to sort and return the list of tuples ordered by the second key wich is the amount of repetitions
        :param word_list: list of tuples [("el", 2), ("muy", 2), ("es", 2), ("perro", 1), ("grande", 1), ("y", 1), ("gato", 1), ("pequeño", 1)]
        :return: list of tuples 
    """
    return sorted(word_list, key = lambda x: x[1], reverse=True)