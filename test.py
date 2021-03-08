
def sq_odd(nums):
        odd_nums_squared = []
        for num in nums:
            is_odd = num % 2 != 0
            if is_odd:
                odd_nums_squared.append(num ** 2)


        return odd_nums_squared
        
my_list = [1,2,3,4,5,6,7,8,9]

print (sq_odd(my_list))