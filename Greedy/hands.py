class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        Solution
        1 - if len(hand) % groupSize != 0:
        2 - create a minHeap from the keys and create a hashmap to record count of all elements
        3 - while MminHeap is not empty go over in for loops of length starting point + groupSize decrement the count of number and if count is 0 pop from minheap
        4 - if count is equal to zero and not first element in heap it means not possible to make consecutive anymore return False
        5 - if able to complete loop return True 
        """
        if len(hand) % groupSize:
            return False
        
        count = {}
        for num in hand:
            count[num] = 1 + count.get(num, 0)
        
        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            start = minH[0]
            for i in range(start, start + groupSize):
                if i not in minH:
                    return False
                count[i] -= 1

                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True

