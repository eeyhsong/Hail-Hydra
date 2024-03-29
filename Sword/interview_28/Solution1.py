class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        list1 = []
        while matrix:
            list1 += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return list1
