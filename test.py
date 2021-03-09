import zlib
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
        strings_dictionary[string] = zlib.compress(string.encode())
    return strings_dictionary


my_strings = [
    "louis", "la", "Grange", "works", "very", "hard",
    "LOoooooooooooooooooooooooooooooooooongs striiiiiiiiiiiiiiiinnnnnngggggggggggggg"
]

print(gen_dictionary(my_strings))


def decode_string(string):
    # print("\nsize of compressed text", sys.getsizeof(string))
    decoded_string = zlib.decompress(string).decode()
    # print("\nsize of original text", sys.getsizeof(decoded_string))
    return decoded_string


my_string = b"x\x9c\xf3\xf1\xcf'\x08\xf2\xd2\x8b\x15\x8aK\x8a2\xd1@\x1e\x18\xa4\xa3\x00\x00,n \xe1"

print(decode_string(my_string))
