# RPC Service using nameko

# import nameko framework and required dependencies
from nameko.rpc import rpc, RpcProxy
import zlib, base64


class RpcAssignment:
    name = "rpc_assignment_service"

    @rpc
    # nums ==> list of integers
    def sq_odd(self, nums):
        odd_nums_squared = []
        for num in nums:
            # Check if num is an odd integer
            is_odd = num % 2 != 0
            if is_odd:
                # Square odd num and add to new list
                odd_nums_squared.append(num**2)
        return odd_nums_squared

    @rpc
    # strings ==> list of strings
    def gen_dictionary(self, strings):
        strings_dictionary = {}
        for string in strings:
            # Add string and encoded string to dictionary as key and value, respectively
            strings_dictionary[string] = base64.b64encode(
                zlib.compress(string.encode())).decode()
        return strings_dictionary

    @rpc
    def decode_string(self, string):
        # Decode given string - using same algorithm as encode in reverse
        decoded_string = zlib.decompress(base64.b64decode(string)).decode()
        return decoded_string


# Author: Louis la Grange | louis@louislagrange.co.za
