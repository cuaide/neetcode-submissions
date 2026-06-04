class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = [(0,0)] # minHeap = [(cost, point_index)]
        n = len(points)
        visit = set()
        res = 0
        while len(visit) < n:
            cost, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            
            for j in range(1,n):
                if j not in visit:
                    dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                    heapq.heappush(minHeap,(dist,j))
        return res


            
            



            


