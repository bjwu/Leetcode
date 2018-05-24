class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5)+1):
            primes[i*2::i] = [False] * len(primes[i*2::i])
        return sum(primes)
        