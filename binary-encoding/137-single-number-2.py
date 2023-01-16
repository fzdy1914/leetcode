class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = 0
        for i in range(32):
            mask, count = 1 << i, 0
            for x in A:
                count = count + 1 if mask&x else count
            count = count % 3
            result = result - (2**31)*count if i == 31 else result | (count << i)
        return int(result)