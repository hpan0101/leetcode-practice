# https://leetcode.com/problems/minimum-seconds-to-remove-all-occurrences-of-substring/
'''
Approach: greedy one-pass simulation
- Each second, every '1' simultaneously swaps left past an adjacent '0'.
- Track zeros: count of '0's seen so far (= how far left the current '1' must travel).
- Track seconds: time taken so far for previous '1's.
- For each '1' encountered: seconds = max(seconds + 1, zeros)
    - seconds + 1: must wait at least one more second than the previous '1'
                   (1s cannot pass each other, so they move in sequence)
    - zeros: minimum swaps this '1' needs to clear all zeros before it
- Return seconds after scanning the full string.
'''
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        seconds = 0
        zeros = 0
        for c in s:
            if c == '0':
                zeros += 1
            elif zeros > 0:
                seconds = max(seconds + 1, zeros)
        return seconds