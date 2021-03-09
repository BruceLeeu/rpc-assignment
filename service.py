# RPC Service using nameko

from nameko.rpc import rpc, RpcProxy
import zlib

class SquareOddNums:
    name = "square_odd_nums"

    @rpc
    def sq_odd(nums):
        odd_nums_squared = []
        for num in nums:
            is_odd = num % 2 != 0
            if is_odd:
                odd_nums_squared.append(num**2)

        return odd_nums_squared

class GenerateStringDictionary:
    name = "generate_string_dictionary"

    @rpc
    def gen_dictionary(strings):
        strings_dictionary = {}
        for string in strings:
            strings_dictionary[string] = zlib.compress(string.encode())
        return strings_dictionary

class DecodeString:
    name = "decode_string"

    @rpc
    def decode_string(string):
        decoded_string = zlib.decompress(string).decode()
        return decoded_string