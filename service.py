# RPC Service using nameko

from nameko.rpc import rpc, RpcProxy

class SquareOddNums:
    name = "square_odd_nums"

    @rpc
    def sq_odd(nums):
        odd_nums_squared = []
        for num in nums:
            is_odd = num % 2 != 0
            if is_odd:
                odd_nums_squared.append(num ** 2)


        return odd_nums_squared

class GenerateStringDictionary:
    name = "generate_string_dictionary"

    # Call other remote service
    # y = RpcProxy("service_y")

    @rpc
    def gen_dictionary(strings):
        res = u"{}-x".format(value)
        return self.y.append_identifier(res)