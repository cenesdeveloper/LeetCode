class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Solution
        1 - create a hashmap where we map presrequisites of each course to the course
        2 - Run dfs on each course and use 2 sets: one for completed courses and one for the courses we are visiting at the moment if we see a course that is in visiting course it means we have a cycle in our graph and we cannot complete it
        3 - add each course we completed to a list
        """
        pres = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            pres[crs].append(pre)
        
        visited = set()
        visiting = set()
        res = []

        def dfs(crs):
            if crs in visiting:
                return False
            
            if crs in visited:
                return True
            
            visiting.add(crs)
            for pre in pres[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)

            visited.add(crs)
            res.append(crs)
            pres[crs] = []

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res

                