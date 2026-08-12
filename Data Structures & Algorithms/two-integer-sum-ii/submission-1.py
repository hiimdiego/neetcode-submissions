class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx1 = 1
        idx2 = len(numbers)
        for i in range(len(numbers)):
            if (numbers[idx1 - 1] + numbers[idx2 - 1] > target):
                idx2 -=1
            elif (numbers[idx1 - 1] + numbers[idx2 - 1] < target):
                idx1 += 1
            else:
                break

        return [idx1, idx2]