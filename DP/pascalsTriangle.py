class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = []

        for r in range(numRows):
            row = [None for _ in range(r+1)]
            row[0], row[-1] = 1, 1

            for i in range(1, len(row)-1):
                row[i] = tri[r-1][i-1] + tri[r-1][i]
            tri.append(row)
        return tri