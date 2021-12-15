# LeetCode
# Level: Easy
# Date: 2021.11.16

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        S1 = set(nums1)
        S2 = set(nums2)
        S3 = set(nums3)
        
        # A = []
        # A.extend(list(S1 & S2))
        # for i in list(S3 & S2):
        #     if i not in A:
        #         A.append(i)
        # for i in list(S3 & S1):
        #     if i not in A:
        #         A.append(i)
        
        # # print(A)
        # return A
        
        # S4 = S1 & S2
        # S5 = S2 & S3
        # S6 = S1 & S3
        
        return list(S1 & S2 | S2 & S3 | S1 & S3)