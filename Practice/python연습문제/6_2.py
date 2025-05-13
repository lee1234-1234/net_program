def parse_to_dict(input_string, delimiter1, delimiter2):
    """
    Parses a string into a dictionary based on two delimiters.

    :param input_string: The input string to parse.
    :param delimiter1: The first delimiter separating key-value pairs.
    :param delimiter2: The second delimiter separating keys and values.
    :return: A dictionary with keys and values extracted from the string.
    """
    result = {}
    pairs = input_string.split(delimiter1)
    for pair in pairs:
        key, value = pair.split(delimiter2)
        result[key] = value
    return result

# Example usage
input_string = 'led=on&motor=off&switch=off'
delimiter1 = '&'
delimiter2 = '='
parsed_dict = parse_to_dict(input_string, delimiter1, delimiter2)
print(parsed_dict)