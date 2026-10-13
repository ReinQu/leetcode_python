"""
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
"""
class Solution1:#判断是否有环：使用深度优先+邻接表
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        def dfs(i,adjacency,flags):
            if flags[i]==-1:return True
            if flags[i]==1: return False
            flags[i]=1
            for j in adjacency[i]:#adjacency[i]是课程i指向的所有课程
                if not dfs(j,adjacency,flags):return False
            flags[i]=-1
            return True


        adjacency=[[] for _ in range(numCourses)]#每个下标代表一个课程，下标指向的内容代表结点指向的结点
        flags=[0 for _ in range(numCourses)]
        for a,b in prerequisites:
            adjacency[b].append(a)
        for i in range(numCourses):
            if not dfs(i,adjacency,flags):return False
        return True



    
import collections
class Solution2:#拓扑排序+入度表：若存在环，则一定有结点的入度始终不为0
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adjacency=[[] for _ in range(numCourses)]
        indegrees=[0 for _ in range(numCourses)]
        for a,b in prerequisites:
            indegrees[a]+=1
            adjacency[b].append(a)
        
        queue=collections.deque()
        for i in range(len(indegrees)):
            if not indegrees[i]:queue.append(i)#入度为0，就放到队列中

        while queue:
            pre=queue.popleft()
            numCourses-=1
            for cur in adjacency[pre]:
                indegrees[cur]-=1
                if not indegrees[cur]:queue.append(cur)#入度为0，就放到队列中
        return not numCourses


