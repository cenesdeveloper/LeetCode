class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Solution
        1 - check if sum(gas) >= sum(cost) because if that is false then it is not possible
        2 - since there is single solution if a starting point fails start from next one it is guarenteed to be found if exists
        """
        curg = 0
        totg = 0
        res = 0

        for i in range(len(gas)):
            totg += gas[i] - cost[i]
            curg += gas[i] - cost[i]

            if curg < 0:
                res = i + 1
                curg = 0
        return res if totg >= 0 else -1