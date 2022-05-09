class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        self.ans = []
        self.per = []
        self.n = len(nums)
        self.used = [False] * self.n
        self.find(0)
        self.tmp = []
        for i in self.ans:
            if i not in self.tmp:
                self.tmp.append(i)
        return self.tmp

    
    def find(self, index):
        if index == self.n:
            self.ans.append(self.per[:])
            return
        for i in range(self.n):
            if not self.used[i]:
                self.used[i] = True
                self.per.append(self.nums[i])
                self.find(index+1)
                self.used[i] = False
                self.per.pop()


