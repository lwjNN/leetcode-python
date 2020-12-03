from _ast import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        s = set()
        s.add(0)

        def helper(rooms: List[List[int]], room: List[int], set=set()):
            for index in room:
                if index in set:
                    continue
                set.add(index)
                helper(rooms, rooms[index], set)

        helper(rooms, rooms[0], s)

        if len(s) == len(rooms):
            return True
        return False
