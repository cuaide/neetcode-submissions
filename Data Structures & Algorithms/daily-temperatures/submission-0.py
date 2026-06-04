class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        num = len(temperatures)
        result = [0] * num

        for i in range(num):
            for j in range(i + 1, num):
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i
                    break
        
        return result







        