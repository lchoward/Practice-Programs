# Write a program that outputs the string representation of numbers from 1 to n.
# But for multiples of three it should output “Fizz” instead of the number and for the
# multiples of five output “Buzz”. For numbers which are multiples of both three and five
# output “FizzBuzz”.

class Solution:
    def fizzBuzz(self, n):
    	"""
    	:type n: int
    	:rtype: List[str]
    	"""
        res = [""] * n
        for i in range(1, n+1):
            three = i % 3 == 0
            five = i % 5 == 0
            if three:
                if five:
                    res[i - 1] = "FizzBuzz"
                else:
                    res[i - 1] = "Fizz"
            elif five:
                res[i - 1] = "Buzz"
            else:
                res[i - 1] = str(i)
        return res