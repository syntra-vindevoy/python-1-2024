from typing import List

class Solution:
    def runningsum(self, nums: List[int]) -> List[int]:
        """
        Running sum of 1d array

        parameters
        ----------

        nums: List[int]
            Any given list of numbers, can be any length or in any order

        returns
        -------

        results: List[int]
            Returns a list of running sums of the input list

        author
        ------
            Chiel

        Date
        ----
            16-11-2024


        """

        results = [nums[0]]

        for i in range (1, len(nums)):
            results.append(results[i-1] + nums[i])

        return results

def main():
    nums = [1,2,3,4]
    print(Solution().runningsum(nums))

    assert Solution().runningsum([1,2,3,4]) == [1,3,6,10]

if __name__ == "__main__":
    main()