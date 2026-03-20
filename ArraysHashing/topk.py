class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Example
        [1,2,3,4,4,5,5,5] k = 3 -> [1, 2]

        Solution
        1 - use buckets where the bucket length is max element
        2 - fill the bucket by their count (create counter)
        3 - from reverse read the bucket and decrease k and append to res array
        4 - when k == 0 return res
        """

        count = {}
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        
        bucket = [[] for _ in range(len(nums) + 1)] 

        for key, value in count.items():
            bucket[value].append(key)
        
        res = []
        for i in range(len(bucket)-1, -1, -1):
            for num in bucket[i]:
                if k != 0:
                    res.append(num)
                    k -= 1
        return res


        