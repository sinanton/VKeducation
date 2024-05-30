from typing import List

def get_indexes(nums1: List[int], nums2: List[int]) -> List[int]:
    return [i for i, (num1, num2) in enumerate(zip(nums1, nums2)) if num1 < num2]

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)