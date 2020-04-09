# Count the number of prime numbers < n

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        
        primes = [1] * n
        
        for i in range(2):
            primes[i] = 0
        
        i = 1
        while i * i < n:
            i += 1
            if not primes[i]:
                continue
            for j in range(i * i, n, i):
                primes[j] = 0
        
        return sum(primes)