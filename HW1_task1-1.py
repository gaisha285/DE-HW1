class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        longest = 1
        current_length = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  # If it's strictly increasing
                 current_length += 1
            else:
                 longest = max(longest, current_length)  # Update longest if current sequence ends
                 current_length = 1  # Reset for a new sequence

    # Final comparison in case the longest sequence is at the end
        return max(longest, current_length)
        