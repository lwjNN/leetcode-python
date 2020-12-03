from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    for num in nums2:
        nums1[m] = num
        m += 1
    nums1.sort()
    print(nums1)

def merge_1(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    nums1[:] = sorted(nums1[:m] + nums2)
    print(nums1)

print(merge_1([1, 2, 3, 0, 0, 0], 3, [2, 4, 6], 3))
