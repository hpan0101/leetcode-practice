# https://leetcode.com/problems/exclusive-time-of-functions/
'''
Approach: stack simulation
- Use a stack to track the currently running function (only the top is executing).
- Track prev_time: the timestamp of the last event processed.
- On "start": credit elapsed time (timestamp - prev_time) to the function currently
  on top of the stack (it was running since prev_time), then push the new function.
- On "end": pop the finished function, credit it (timestamp - prev_time + 1) — the
  +1 is because end timestamps are inclusive. Set prev_time = timestamp + 1.
'''
from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            parts = log.split(":")
            func_id = int(parts[0])
            action = parts[1]
            timestamp = int(parts[2])

            if action == "start":
                if stack:
                    res[stack[-1]] += timestamp - prev_time
                stack.append(func_id)
                prev_time = timestamp
                
            else:
                finished_func = stack.pop()
                res[finished_func] += timestamp - prev_time + 1
                prev_time = timestamp + 1

        return res