class Solution(object):
    def merge(self, nums1, m, nums2, n):
        
        p1, p2, p = m - 1, n - 1, m + n - 1

    # Merge in reverse order
        while p1 >= 0 and p2 >= 0:
             if nums1[p1] > nums2[p2]:
                 nums1[p] = nums1[p1]
                 p1 -= 1
             else:
                 nums1[p] = nums2[p2]
                 p2 -= 1
             p -= 1

    # Fill nums1 with remaining elements from nums2, if any
        nums1[:p2 + 1] = nums2[:p2 + 1]