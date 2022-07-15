"""
Design a logger system that receives a stream of messages along with their
timestamps. Each unique message should only be printed at most every 10 seconds
(i.e. a message printed at timestamp t will prevent other identical messages
from being printed until timestamp t + 10).

All messages will come in chronological order. Several messages may arrive at
the same timestamp.

Implement the Logger class:

Logger() Initializes the logger object.
bool shouldPrintMessage(int timestamp, string message) Returns true if the
message should be printed in the given timestamp, otherwise returns false.
"""

class Logger:
    from collections import deque

    def __init__(self):
        self.dq = deque()  # deque of messages printed in the last 10 seconds. left is oldest
        self.ts = {} # message -> timestamp map for messages printed in the last 10 seconds
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        do_print = False
        if message not in self.ts or self.ts[message] <= timestamp - 10:
            self.ts[message] = timestamp
            self.dq.append(message)
            do_print = True
        
        # clean out all print records older than 10 seconds
        while self.dq and (self.dq[0] not in self.ts or self.ts[self.dq[0]] <= timestamp - 10):
            oldest_msg = self.dq[0]
            if oldest_msg not in self.ts or self.ts[oldest_msg] <= timestamp - 10:
                if oldest_msg in self.ts:
                    del self.ts[oldest_msg]
                self.dq.popleft()
        
        return do_print
    

"""
?? min: first draft



"""

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
