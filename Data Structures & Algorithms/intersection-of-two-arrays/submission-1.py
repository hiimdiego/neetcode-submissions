class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = min(len(nums1), len(nums2))
        output = []
        for i in range(n):
            if nums1[i] in nums2 and nums1[i] not in output:
                output.append(nums1[i])

            if nums2[i] in nums1 and nums2[i] not in output:
                output.append(nums2[i])
        return output