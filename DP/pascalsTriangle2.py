class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def pascal(i):
            if i == 0:
                return [1]
            
            old = pascal(i-1)
            arr = [1]

            for j in range(1, i):
                arr.append(old[j-1] + old[j])

            arr.append(1)
            return arr
        return pascal(rowIndex)