import zlib, base64
import sys


def sq_odd(nums):
    odd_nums_squared = []
    for num in nums:
        is_odd = num % 2 != 0
        if is_odd:
            odd_nums_squared.append(num**2)
    return odd_nums_squared


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(sq_odd(my_list))


def gen_dictionary(strings):
    strings_dictionary = {}
    for string in strings:
        strings_dictionary[string] = base64.b64encode(zlib.compress(string.encode())).decode()
    return strings_dictionary


my_strings = [
    'louis', 'la', 'Grange', 'works', 'very', 'hard',
    'LOoooooooooooooooooooooooooooooooooongs striiiiiiiiiiiiiiiinnnnnngggggggggggggg'
]

print(gen_dictionary(my_strings))


def decode_string(string):
    # print("\nsize of compressed text", sys.getsizeof(string))
    # decoded_string = zlib.decompress(string).decode()
    # print("\nsize of original text", sys.getsizeof(decoded_string))
    decoded_string = zlib.decompress(base64.b64decode(string)).decode()
    return decoded_string


my_string = 'eJzz8c8nCPLSixWKS4oy0UAeGKSjAAAsbiDh'

print(decode_string(my_string))
