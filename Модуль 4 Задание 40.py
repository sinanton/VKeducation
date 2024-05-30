from collections import deque
from typing import List


def rotate_list(nums: List[int], n: int):
    nums = deque(nums)
    nums.rotate(n)
    return list(nums)


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)