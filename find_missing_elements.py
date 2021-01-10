# -*- coding: utf-8 -*-
"""
TC : O(2N) where N is the no. of elements, and we go ove rthe array twice
SC : O(1) no extra space used
"""

class Solution:
    def findDisappearedNumbers(self, nums:[]):
        #edge case
        if not nums or len(nums) == 0:
            return []
        out = []
        #While going through the array, we take th absolute value of the element -1
        #We check if the element present after doing this is negative or positive
        #We change the sign
        
        #in the second traversal, we append the position of the missing elements into our output result
        #we retain the original array as it is, by changing its sign
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                out.append(i + 1)
            else:
                nums[i] *= -1
        
        return out
