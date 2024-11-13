"Converteer nummers naar Romeinse Cijfers"


def get_number_detail(number):
    """
    :param number: The input number that needs to be converted.
    :return: A list of digits, where the input number is padded with leading zeros to match the expected length.
    """
    expected_length = 4
    digits = [int(digit) for digit in str(number).zfill(expected_length)]
    return digits


assert get_number_detail(1255) == [1, 2, 5, 5], f"Test failed for 1255: {get_number_detail(1255)}"
assert get_number_detail(250) == [0, 2, 5, 0], f"Test failed for 250: {get_number_detail(250)}"
assert get_number_detail(15) == [0, 0, 1, 5], f"Test failed for 250: {get_number_detail(250)}"


def convert_to_romeinse(number):
    """
    :param number: The integer number to be converted into its Roman numeral representation.
    :return: The Roman numeral representation of the given integer number.
    """
    getallen = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X'}
    tientallen = {1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
    hondertallen = {1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}

    details = get_number_detail(number)

    result = 'M' if details[0] > 0 else ''
    result += hondertallen.get(details[1], '')
    result += tientallen.get(details[2], '')
    result += getallen.get(details[3], '')

    return result


assert convert_to_romeinse(15) == "XV"
assert convert_to_romeinse(20) == "XX"
assert convert_to_romeinse(34) == "XXXIV"
assert convert_to_romeinse(67) == "LXVII"
assert convert_to_romeinse(129) == "CXXIX"
assert convert_to_romeinse(670) == "DCLXX"
assert convert_to_romeinse(1100) == "MC"
assert convert_to_romeinse(1565) == "MDLXV"
assert convert_to_romeinse(4) == "IV"
