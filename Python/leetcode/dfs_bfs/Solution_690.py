from _ast import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance_dfs(self, employees: List['Employee'], id: int) -> int:
        emap = {e.id: e for e in employees}

        def dfs(eid):
            emp = emap[eid]
            return emp.importance + sum(dfs(eid) for eid in emp.subordinates)

        return dfs(id)

    def getImportance_bfs(self, employees: List['Employee'], id: int) -> int:
        emap = {e.id: e for e in employees}
        res = 0
        queue = [id]
        while queue:
            cur = queue.pop(0)
            e = emap[cur]
            res += e.importance
            queue.extend(e.subordinates)
        return res
