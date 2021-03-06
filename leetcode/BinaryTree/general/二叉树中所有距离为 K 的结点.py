'''
863. 二叉树中所有距离为 K 的结点
给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。

返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。

示例 1：

输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

输出：[7,4,1]

解释：
所求结点为与目标结点（值为 5）距离为 2 的结点，
值分别为 7，4，以及 1



注意，输入的 "root" 和 "target" 实际上是树上的结点。
上面的输入仅仅是对这些对象进行了序列化描述。
 
提示：

给定的树是非空的，且最多有 K 个结点。
树上的每个结点都具有唯一的值 0 <= node.val <= 500 。
目标结点 target 是树上的结点。
0 <= K <= 1000.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
思路：先树转图，在用的图的BFS
'''
from leetcode.BinaryTree.NodeAndBuildTree import *

class Solution:
    def distanceK(self, root: TreeNode, target:int, k: int) -> list:
        #建图
        from collections import defaultdict
        g = defaultdict(list)       #字典的键对应的值是一个List,便于a:[1,2,3]这种键值对
        def dfs(root):
            if root.left:
                g[root.val].append(root.left.val)
                g[root.left.val].append(root.val)
                dfs(root.left)
            if root.right:
                g[root.val].append(root.right.val)
                g[root.right.val].append(root.val)
                dfs(root.right)
        dfs(root)
        print(g)
        #图的BFS
        queue = [target]
        visited = [target]
        for i in range(k):  #距离
            nbr_nodes = []  #将同一层次的节点的临节点储存在一起，便于下次遍历和返回结果
            while queue:
                cur = queue.pop(0)
                for nbr in g[cur]:
                    if nbr not in visited:
                        nbr_nodes.append(nbr)
                        visited.append(nbr)
            queue = nbr_nodes
        return queue

#测试
root_lst = [3,5,1,6,2,0,8,None,None,7,4]
target = 5
K = 2

root = list_buildTree(root_lst)
res = Solution().distanceK(root,5,2)
print(res)
