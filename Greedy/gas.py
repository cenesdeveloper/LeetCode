class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Solution
        1 - check if sum(gas) >= sum(cost) because if that is false then it is not possible
        2 - since there is single solution if a starting point fails start from next one it is guarenteed to be found if exists
        """

        tg = sum(gas) - sum(cost)
        if tg < 0:
            return -1

        cg = 0
        res = 0

        for i in range(len(gas)):
            cg += gas[i] - cost[i]

            if cg < 0:
                cg = 0
                res = i + 1
        return res
