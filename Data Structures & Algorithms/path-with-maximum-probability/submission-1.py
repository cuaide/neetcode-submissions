class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = collections.defaultdict(list)

        for (u, v), p in zip(edges, succProb):
            graph[u].append((v, p))
            graph[v].append((u, p))

        maxHeap = [(-1.0, start_node)]  
        visited = set()
        while maxHeap:
            prob, node = heapq.heappop(maxHeap)
            prob = -prob
            if node == end_node:
                return prob
            if node in visited:
                continue
            visited.add(node)

            for node2,prob2 in graph[node]:
                if node2 not in visited:
                    heapq.heappush(maxHeap,(-(prob2*prob),node2))

        return 0.0



            

            

