'''
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
示例 2:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
思路：二分查找 + 坐标转换：二维坐标转一维坐标求mid，再转二维坐标比较target
'''
class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        #特判
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        m,n = len(matrix),len(matrix[0])
        l, r = 0, m*n-1
        while l < r:
            mid = (l + r)//2
            x = mid // n
            y = mid % n
            if target > matrix[x][y]:
                l = mid + 1
            else:
                r = mid
        x = l // n
        y = l % n
        return matrix[x][y] == target

#测试
matrix = [[1]]

target = 50
res = Solution().searchMatrix(matrix,target)
print(res)