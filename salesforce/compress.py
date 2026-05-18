# https://leetcode.com/problems/string-compression/
'''
Approach: two-pointer in-place compression
- Use pointer i to scan groups of consecutive identical characters.
- Use pointer write to overwrite chars in-place with the compressed result.
- For each group: write the character, then write the digit(s) of the count
  only if the group length > 1 (single chars are written without a count).
- Return write, which is the new length of the compressed array.
'''
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        i = 0
        while i < len(chars):
            c = chars[i]
            start = i
            while i < len(chars) and chars[i] == c:
                i += 1
            group_len = i - start
            chars[write] = c
            write += 1
            if group_len > 1:
                for digit in str(group_len):
                    chars[write] = digit
                    write += 1
        return write