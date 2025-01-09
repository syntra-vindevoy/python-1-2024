#https://leetcode.com/problems/median-of-two-sorted-arrays/description/
class Solution(object):
    def findmedian(self, a1, a2):
        p = 0
        p1 = 0
        p2 = 0

        while (p1 + p2) < ((len(a1) + len(a2)) // 2) - 1:
            if a1[p1] < a2[p2]:
                p1 += 1
                p = a1[p1]
            else:
                p2 += 1
                p = a2[p2]

        return p

a1 = [1,3,5]
a2 = [2,4,6,8]

s = Solution()
r = s.findmedian(a1,a2)

print(r)