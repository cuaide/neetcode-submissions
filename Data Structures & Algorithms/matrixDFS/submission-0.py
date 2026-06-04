from typing import List, Set, Tuple
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        target = (rows - 1, cols - 1)
        # 시작점/도착점이 벽(1)이면 경로 없음
        if grid[0][0] == 1 or grid[target[0]][target[1]] == 1:
            return 0

        def helper(r: int, c: int, visit: Set[Tuple[int, int]]) -> int:
            # 경계/장애물/재방문 체크
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if grid[r][c] == 1 or (r, c) in visit:
                return 0

            # 목적지 도달
            if (r, c) == target:
                return 1

            visit.add((r, c))
            total = (
                helper(r + 1, c, visit) +
                helper(r - 1, c, visit) +
                helper(r, c + 1, visit) +
                helper(r, c - 1, visit)
            )
            visit.remove((r, c))
            return total

        return helper(0, 0, set())


