class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        list = []
        for num in nums:
            if num in result:
                result[num] += 1
            else:
                result[num] = 1
        val_key = [(i, j) for j, i in result.items()]
        val_key.sort(reverse=True)
        for i in range(k):
            list.append(val_key[i][1])
        return list