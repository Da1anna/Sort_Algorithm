'''
有 N 个房间，开始时你位于 0 号房间。每个房间有不同的号码：0，1，2，...，N-1，并且房间里可能有一些钥匙能使你进入下一个房间。

在形式上，对于每个房间 i 都有一个钥匙列表 rooms[i]，每个钥匙 rooms[i][j] 由 [0,1，...，N-1] 中的一个整数表示，其中 N = rooms.length。 钥匙 rooms[i][j] = v 可以打开编号为 v 的房间。

最初，除 0 号房间外的其余所有房间都被锁住。

你可以自由地在房间之间来回走动。

如果能进入每个房间返回 true，否则返回 false。

示例 1：

输入: [[1],[2],[3],[]]
输出: true
解释:
我们从 0 号房间开始，拿到钥匙 1。
之后我们去 1 号房间，拿到钥匙 2。
然后我们去 2 号房间，拿到钥匙 3。
最后我们去了 3 号房间。
由于我们能够进入每个房间，我们返回 true。
示例 2：

输入：[[1,3],[3,0,1],[2],[0]]
输出：false
解释：我们不能进入 2 号房间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/keys-and-rooms
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def canVisitAllRooms(self, rooms: [[int]]) -> bool:
        visited = [0] * len(rooms)
        queue = [0]

        while queue:
            cur = queue.pop(0)
            #钥匙全拿，再考虑去过的房间
            if visited[cur] == 0:
                queue.extend(rooms[cur])
                visited[cur] = 1
        if 0 in visited:
            return False
        return True

    def canVisitAllRooms_1(self, rooms: [[int]]) -> bool:
        '''
        逻辑优化版
        '''
        visited,queue = {0},[0]

        while queue:
            cur_room = queue.pop(0)
            #只拿没去过房间的钥匙
            for key in rooms[cur_room]:
                if key not in visited:
                    queue.append(key)
                    visited.add(key)
        return len(visited) == len(rooms)

    def canVisitAllRooms_dfs(self, rooms: [[int]]) -> bool:
        visited,stack = {0},[0]

        while stack:
            cur = stack.pop()
            for key in rooms[cur]:
                if key not in visited:
                    stack.append(key)
                    visited.add(key)
        return len(visited) == len(rooms)

    def canVisitAllRooms_dfs_R(self, rooms: [[int]]) -> bool:
        visited = {0}
        def dfs(cur,visited):
            visited.add(cur)
            for key in rooms[cur]:
                if key not in visited:
                    dfs(key,visited)
        dfs(0,visited)
        return len(visited) == len(rooms)


#测试
rooms = [[1,3],[3,2,1],[2],[0]]
res = Solution().canVisitAllRooms_dfs_R(rooms)
print(res)