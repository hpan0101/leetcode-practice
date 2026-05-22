# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/?envType=company&envId=visa&favoriteSlug=visa-thirty-days
'''
Approach: greedy one-pass counting
- Traverse the string tracking unmatched '[' brackets (open counter).
- On '[': increment open.
- On ']': if there's an unmatched '[' available, match and cancel it (open--).
          Otherwise, this ']' is unmatched — it will need a swap.
- After the full pass, open = number of unmatched '[' remaining.
- Each swap fixes one '[' and one ']' at once, so swaps needed = ceil(open / 2)
  = (open + 1) // 2.
'''
class Solution:
    def minSwaps(self, s: str) -> int:
        open = 0
        for c in s:
            if c == '[':
                open += 1
            elif c == ']':
                if open > 0:
                    open -= 1
        return (open + 1) // 2

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("][][", 1),     # 1 swap: ][][ -> [][]
        ("]]][[[", 2),   # 2 swaps needed
        ("[]", 0),       # already balanced
        ("[][]", 0),     # already balanced
        ("[[]]", 0),     # already balanced
        ("]][[", 1),     # 2 unmatched [ -> ceil(2/2) = 1 swap
    ]

    for s, expected in tests:
        result = sol.minSwaps(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] minSwaps({s!r}) = {result} (expected {expected})")
