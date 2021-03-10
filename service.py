# RPC Service using nameko

from nameko.rpc import rpc, RpcProxy
import zlib, base64

class RpcAssignment:
    name = "rpc_assignment_service"

    @rpc
    def sq_odd(self, nums):
        odd_nums_squared = []
        for num in nums:
            is_odd = num % 2 != 0
            if is_odd:
                odd_nums_squared.append(num**2)

        return odd_nums_squared

    @rpc
    def gen_dictionary(self, strings):
        strings_dictionary = {}
        for string in strings:
            strings_dictionary[string] = base64.b64encode(zlib.compress(string.encode())).decode()
        return strings_dictionary

    @rpc
    def decode_string(self, string):
        decoded_string = zlib.decompress(base64.b64decode(string)).decode()
        return decoded_string
    