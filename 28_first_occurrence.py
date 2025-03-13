# ONLY WORKS ON HALF of 83 TEST CASES
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        h_pointer = 0
        n_pointer = 0

        # while both pointers are less than or equal to the length of their word
        while n_pointer < len(needle) and h_pointer < len(haystack):
            # if the letter at h_pointer is the same as letter at n_pointer
            if haystack[h_pointer] == needle[n_pointer]:
                # move both pointers forward
                h_pointer += 1
                n_pointer += 1
            # if not the same
            else:
                # move the haystack pointer forward but start n_pointer at beginning again
                h_pointer += 1
                n_pointer = 0
                # if h_pointer reaches the end of the word without all matches, return -1
                if h_pointer == len(haystack):
                    return -1
        
        # if n_pointer reaches the end of the needle and there is a match
        # subtract the last index of needle from the index of haystack and return it
        return h_pointer - len(needle)