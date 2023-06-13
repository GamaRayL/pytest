def get_val(collection, key, default="git"):
    """
    Возвращает из переданного словаря значение по ключу (ключ - второй аргумент).
    Если ключ не существует, то - возврат значения по-умолчанию.

    :param collection: исходный словарь
    :param key: исходный ключ
    :param default: значение по-умолчанию
    :return: значение по ключу или значение по-умолчанию
    """
    # assert get_val(data, "key") == "value"
    # assert get_val(data, "key", "git") == "value"
    # assert get_val({}, "list") == "git"
    # assert get_val({}, "dict", "git") == "git"
    # assert get_val({}, "dict", "npm") == "npm"

    if len(collection) == 0:
        return default

    return collection[key]

