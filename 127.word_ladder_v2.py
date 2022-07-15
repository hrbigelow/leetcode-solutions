"""
A transformation sequence from word beginWord to word endWord using a
dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk
such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to
be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the
number of words in the shortest transformation sequence from beginWord to
endWord, or 0 if no such sequence exists.

"""


"""
What is going on here?

nw are 'next words', looks like a list of 78 words

we iterate as long as both fw and bw are not empty
they are swapped occasionally, so that bw is the larger of the two

at each iteration, ns is initialized to the empty set,

wd consists of the entire set of words except the last one.
wd doubles as a validity test that the word being tested exists,
and as a visited array.

ns represents the temporary set that will be assigned to fw
we use fw at each iteration to search for neighbors

for each word in fw, generate all 78 possible neighbors
for each neighbor, if we find it in bw, we are done
if it is not in wd, it's irrelevant (wd is the filtering criterion)
if it is, we have now visited it, so remove it from wd.

we now add in the next word

This solution has O(A * L) complexity in the inner loop.



"""

# 200 ms
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        wd = set(wordList)
        wd.remove(endWord)
        fw = {beginWord}
        bw = {endWord}
        lvl = 0
        ns = set()
        
        while fw and bw:
            lvl+=1
            
            if len(bw) < len(fw):
                bw, fw = fw, bw
            
            ns = set()
            
            for w in fw:
                nw = [
                    w[:i]+t+w[i+1:]
                    for t in ascii_lowercase
                    for i in range(len(beginWord))
                ]
                for word in nw:
                    if word in bw: return lvl+1 
                    if word not in wd: continue
                    wd.remove(word)
                    ns.add(word)
            
            fw = ns
        
        return 0

# 88 ms
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        ws=set(wordList)
        if endWord not in ws:
            return 0
        ws.discard(beginWord)
        ws.discard(endWord)
        step=1
        s1,s2={beginWord},{endWord}
        while s1 and s2:
            if len(s1)>len(s2): s1,s2=s2,s1
            # print(f's1={s1},s2={s2},step={step}')
            s3=set()
            while s1:
                w=s1.pop()
                for i in range(len(w)):
                    for c in string.ascii_lowercase:
                        t=w[:i]+c+w[i+1:]
                        if t in s2:
                            return step+1
                        if t in ws:
                            s3.add(t)
                            ws.discard(t)
            s1,step=s3,step+1
        return 0


#how to print path???
#https://leetcode.com/problems/word-ladder/discuss/175476/BFS-Java-with-Path-Print

# 76 ms
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0 
        step = 2 
        wordListSet = set(wordList)
        forward, backward = {beginWord}, {endWord}
        direction = 1
        #res = collections.deque([])
        while forward and backward:
            if len(forward) > len(backward):
                forward, backward = backward, forward 
                direction *= -1 
            wordListSet -= forward 
            nextForward = set()
            #res.append(forward)
            for w in forward:
                for i in range(len(w)):
                    first, second = w[:i], w[i+1:]
                    for ch in string.ascii_lowercase:
                        combined = first + ch + second 
                        if combined in wordListSet:
                            if combined in backward:
                                #res.append(combined)
                                #print(res)
                                return step
                            nextForward.add(combined)
            forward = nextForward
            #res.append(forward)
            step += 1
        return 0 

