class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Solution
        1 - Model it as a directed graph
        2 - if there is a cycle we return False else True because it looks for cyclic dependency
        3 - Create a dictionary where each course -> prerequisites for easier traversal
        4 - recursively go through each course and check if prerequisites can be completed meaning if it can be emptied if a course has no prerequisites it can be completed and remove completed courses from prerequisites
        5 - Use a set for keeping track of current cycle we are checking at so if a course enters twice it means there is a cyclic dependency and we cannot complete the courses return False
        6 - Once the course is completed remove from set and set its pres to []
        7 - run dfs for each course

        [[1,0][2,1]] -> {0: [], 1: [0], 2: [1]}
        """

        pres = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pres[crs].append(pre)
        
        visiting = set()
        def dfs(i):
            if pres[i] == []:
                return True
            
            if i in visiting:
                return False
            
            visiting.add(i)
            for pre in pres[i]:
                if not dfs(pre):
                    return False
            visiting.remove(i)

            pres[i] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True