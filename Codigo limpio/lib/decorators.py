def clean_data_decorator(func):
    """
        limpiar los parametros de la funcion.
        return: lista ordenada o str con error de validacion.
    """
    def wrapper(*args, **kwargs):
        int_check_lista = [x for x in args[0] if not isinstance(x, int)]
        if len(int_check_lista):
            return f'la lista debe de ser de enteros'
        res = func(*args, **kwargs)
        return res
        
    return wrapper