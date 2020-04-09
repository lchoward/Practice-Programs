# Convert a non-negative integer to its english words representation. Given input is
# guaranteed to be less than 231 - 1.
#
# Example 1:
# Input: 123
# Output: "One Hundred Twenty Three"
#
# Example 2:
# Input: 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
#
# Example 3:
# Input: 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
#
# Example 4:
# Input: 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand
#          Eight Hundred Ninety One"

class Solution:
	def numberToWords(self, num):
		"""
		:type num: int
		:rtype: str
		"""
		if num == 0:
			return "Zero"

		length = len(str(num))
		numbers = [0,1,2,3,4,5,6,7,8,9]
		ones = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
		teens = ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen",
		         "Seventeen","Eighteen","Nineteen"]
		tens = ["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy",
		        "Eighty","Ninety"]

		# method to convert three numbers to a word
		def threeNumToWords(x):
			res = ""
			if x > 99:
				hundred = x // 100
				res += ones[numbers.index(hundred)] + " Hundred"
				x -= hundred * 100
			if x > 19:
				ten = x // 10
				one = x % 10
				if res: res += " "
				if one:
					res += tens[numbers.index(ten)] + " " + ones[numbers.index(one)]
				else:
					res += tens[numbers.index(ten)]
				return res
			if x > 9:
				if res: res += " "
				one = x % 10
				res += teens[numbers.index(one)]
				return res
			if x > 0:
				if res: res += " "
				res += ones[numbers.index(x)]
				return res
			else:
				return res

		res = ""
		# check for billions
		if num > 999999999:
			billions = num // 1000000000
			res += threeNumToWords(billions) + " Billion"
			num -= billions * 1000000000
		
		# check for millions
		if num > 999999:
			millions = num // 1000000
			if res: res += " "
			res += threeNumToWords(millions) + " Million"
			num -= millions * 1000000

		# check for thousands
		if num > 999:
			thousands = num // 1000
			if res: res += " "
			res += threeNumToWords(thousands) + " Thousand"
			num -= thousands * 1000

		# check for hundreds
		if num > 0:
			if res: res += " "
			res += threeNumToWords(num)

		return res


if __name__ == '__main__':
	soln = Solution()
	test1 = soln.numberToWords(23000000000) # 23 billion
	test2 = soln.numberToWords(718000000000) # 718 billion
	test3 = soln.numberToWords(4000000000) # 4 billion
	test4 = soln.numberToWords(901000000000) # 901 billion
	test5 = soln.numberToWords(1000000) # 1 million
	test6 = soln.numberToWords(1234567) # 1 mil 234 thou 567
	test7 = soln.numberToWords(123456) # 123 thou 456
	test8 = soln.numberToWords(123) # 123
	test9 = soln.numberToWords(1) # 1
	test10 = soln.numberToWords(0) # 0
	test11 = soln.numberToWords(100) # 100

	print(test1)
	print(test2)
	print(test3)
	print(test4)
	print(test5)
	print(test6)
	print(test7)
	print(test8)
	print(test9)
	print(test10)
	print(test11)