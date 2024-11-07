class Solution(object):
    def intersection(self, nums1, nums2):
        
        set1 = set(nums1)
        set2 = set(nums2)
        result = set1 & set2  # Intersection of two sets
    
    # Return the result as a list
        return list(result)