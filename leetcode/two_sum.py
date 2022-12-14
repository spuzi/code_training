from typing import List


class Solution:

    def twoSum(
        self,
        nums: List[int],
        target: int
    ) -> List[int]:
        index_map = {}
        for index, num in enumerate(nums):
            searched_value = target - num
            if searched_value in index_map:
                return index_map[searched_value], index
            else:
                index_map[num] = index


if __name__ == '__main__':
    solution = Solution()
    res = solution.twoSum(nums=[2, 7, 11, 15],
                          target=9)

    assert res == [0, 1]

    res = solution.twoSum(nums=[3, 3],
                          target=6)

    assert res == [0, 1]
