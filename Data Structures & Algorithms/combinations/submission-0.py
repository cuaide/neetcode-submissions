class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []
        self.help(1, [], combs, n, k)
        return combs

    def help(self, i, curcomb, combs, n, k):
        if len(curcomb) == k:
            combs.append(curcomb.copy())
            return 
        if i > n:
            return
        for j in range(i, n + 1):
            curcomb.append(j)
            self.help(j + 1, curcomb, combs, n, k)
            curcomb.pop()