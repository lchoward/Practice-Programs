# description: You are given coins of different denominations and a total amount of money
# amount. Write a function to compute the fewest number of coins that you need to make up
# that amount. If that amount of money cannot be made up by any combination of the coins,
# return -1.

from typing import List

class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:
		numDenoms = len(coins)
		# corner cases
		if (amount == 0):
			return 0
		if (numDenoms == 0 or amount < 0):
			return -1

		# otherwise, sort the list of coins
		sortedCoins = sorted(coins, reverse=True)
		# remove duplicate denomination values
		redCoins = []
		for denom in coins:
			if denom not in redCoins:
				redCoins.append(denom)

		numDenoms = len(redCoins)
		# print(str(coins))
		# print("amount is: " + str(amount))

		# start a memo, where memo[i] = min # coins to produce value i
		memo = [0] * (amount + 1)

		# add the denoms we have to the memo as 1
		for currDenom in redCoins:
			if (currDenom <= amount):
				memo[currDenom] = 1

		# iterate through all values 1 to amount
		for value in range(1, amount + 1):
			for currDenom in range(numDenoms):
				prevAmount = value - redCoins[currDenom]
				# skip this denom, check smaller denoms (if possible)
				if (prevAmount<0):
					continue
				# the amount is a denom, keep as 1 and go to next value
				elif (prevAmount==0):
					break
				# if there's already a value, we only update if it's an improvement
				elif (memo[prevAmount] > 0):
					if (memo[value] > 0):
						if (memo[prevAmount] + 1 < memo[value]):
							memo[value] = memo[prevAmount] + 1
					else:
						memo[value] = memo[prevAmount] + 1
			if (memo[value] == 0):
				memo[value] = -1

		# print(memo[3])
		# print(memo[amount])
		return memo[amount]


if __name__ == '__main__':
	soln = Solution()
	test1 = soln.coinChange([1,2,5],11) #should return 3
	test2 = soln.coinChange([1,2,5],1) #should return 1
	test3 = soln.coinChange([],5) #should return -1
	test4 = soln.coinChange([2,3,5],1) #should return -1
	test5 = soln.coinChange([2,5,10],3) #should return -1
	test6 = soln.coinChange([5,10,25],90) #should return 5
	test7 = soln.coinChange([186,419,83,408],6249) #should return 20

	assert test1 == 3
	assert test2 == 1
	assert test3 == -1
	assert test4 == -1
	assert test5 == -1
	assert test6 == 5
	assert test7 == 20