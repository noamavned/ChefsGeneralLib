import random


def generate_int_list(length: int = 0, minimum_random_number: int = 0, maximum_random_number: int = 100, order_min_max: bool = False) -> list:
    """Generates a list of random numbers.

    Args:
        length (int, optional): Length of the list. Defaults to 0.
        minimum_random_number (int, optional): Minimum random number. Defaults to 0.
        maximum_random_number (int, optional): Maximum random number. Defaults to 100.
        order_min_max (bool, optional): Whether or not to sort minimum and maximum in `minimum_random_number` and `maximum_random_number` and prevent an error. Defaults to False.

    Returns:
        list: List of random numbers.
    """
    if order_min_max:
        if minimum_random_number > maximum_random_number:
            minimum_random_number, maximum_random_number = maximum_random_number, minimum_random_number

    if minimum_random_number > maximum_random_number:
        raise Exception(
            "minimum_random_number has to be less than maximum_random_number")

    if length == 0:
        return []

    if minimum_random_number == maximum_random_number:
        return [minimum_random_number]*length

    return [random.randint(minimum_random_number, maximum_random_number) for _ in range(length)]


def generate_float_list(length: int = 0, minimum_random_number: float = 0, maximum_random_number: float = 100, order_min_max: bool = False) -> list:
    """Generates a list of random numbers.

    Args:
        length (int, optional): Length of the list. Defaults to 0.
        minimum_random_number (float, optional): Minimum random number. Defaults to 0.
        maximum_random_number (float, optional): Maximum random number. Defaults to 100.
        order_min_max (bool, optional): Whether or not to sort minimum and maximum in `minimum_random_number` and `maximum_random_number` and prevent an error. Defaults to False.

    Returns:
        list: List of random numbers.
    """
    if order_min_max:
        if minimum_random_number > maximum_random_number:
            minimum_random_number, maximum_random_number = maximum_random_number, minimum_random_number

    if minimum_random_number > maximum_random_number:
        raise Exception(
            "minimum_random_number has to be less than maximum_random_number")

    if length == 0:
        return []

    if minimum_random_number == maximum_random_number:
        return [minimum_random_number]*length

    return [random.uniform(minimum_random_number, maximum_random_number) for _ in range(length)]
