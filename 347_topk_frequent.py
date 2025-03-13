from typing import List
import pytest

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Attempt #1
        Make a counter dict with the int as the key and the frequency the value
        Find the k number of highest values from the dict and return the keys in an array

        Attempt #2 after looking at hints
        Use the bucket sort algorithm to create n buckets, grouping numbers based on 
        their frequencies from 1 to n. Then, pick the top k numbers from the buckets, 
        starting from n down to 1.
        '''
        num_dict = {}
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1

        n = len(set(nums)) + 1
        print(n)

        buckets = [[]] * n
        print(buckets)

        for key, value in num_dict.items():
            if not buckets[value - 1]:
                buckets[value - 1] = [key]
            else:
                buckets[value - 1].append(key)

        print(buckets)

        if [] in buckets:
            bucks = [x for x in buckets if x != []]

        print(bucks)

        # return buckets[-k:]

        ans = []

        while k > 0:
            for x in range(-1, -len(buckets), -1):
                print(f"x: {x}")
                if buckets[x] != []:
                    print(f"buck: {buckets[x]}")
                    ans.append(buckets[x].pop())
                else:
                    continue
            k -= 1

        return ans
    
    def topKFrequent_B(self, nums: List[int], k: int) -> List[int]:
        pass
    
class TestSolution:
    @pytest.mark.parametrize("input_arr, input_k, expected_output", [
        ([1, 1, 1, 2, 2, 3], 2, [[1, 2], [2, 1]]),
        ([1], 1, [[1]]),
        ([-1, -1], 1, [[-1]]),
        ([1, 2], 2, [[1, 2], [2, 1]])
    ])
    def test_topKFrequent_B(self, input_arr, input_k, expected_output):
        solution = Solution()
        assert solution.topKFrequent_B(input_arr, input_k) in expected_output