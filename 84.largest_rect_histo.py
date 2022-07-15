"""
Given an array of integers heights representing the histogram's bar height
where the width of each bar is 1, return the area of the largest rectangle in
the histogram.

"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = [(0,0)]
        m = 0
        heights.append(0)
        
        for i, h in enumerate(heights):
            pi = i
            while st[-1][1] > h:
                pi, ph = st.pop()
                m = max(m, ph * (i - pi))
            
            if st[-1][1] < h:
                st.append((pi, h))
        
        return m
    
"""
The main idea here is, we know that any candidate for a maximal rectangle must
have its upper corners touch the graph defined by the histogram.  This graph is
a piece-wise constant function.

But, to build intuition, imagine an arbitrary continuous function R -> R on
some interval which starts and ends at zero, and searching for the maximal
rectangle under that function.  Note then that the top edge of all candidate
rectangles will be all horizontal lines that touch this graph.  You could
produce all of those lines by scanning upwards from zero, filling in, until you
get to the maximal value of the graph.

Note that each such line has an l, r position and a height, defining the
rectangle.  If you could efficiently enumerate all of these lines, then you can
find the maximal rectangle.

But, note that in this entire set of line segments, there is not one pair which
are not either disjoint or nested.  Either the line segment pairs look like:
() ()  or (()).  The entire set of line segments can be expressed as a nested
structure.


Now, note that a stack is used to represent the forward traversal of a nested
interval structure.  A call stack does this, where each 'interval' is a
'enter/exit' event of a function call.  The push to the stack represents the
start of the interval, and the pop signifies the end of that interval.  The
advantage is that it allows one to retrieve information about the interval
while popping.


The reasoning process for solving this is as follows:

To set things up, note that the heights array defines a piecewise constant
function of line segments (i, heights[i]) -> (i+1, heights[i+1]).

Then we can consider all possible rectangles that fit under the graph.  Each of
these will be defined by l, r, h coordinates (left boundary, right boundary,
and height).  Any maximal rectangle must be 'blocked' in the left, right, and
height directions, meaning it runs up against a wall defined by the graph.  If
it didn't, then it could be expanded in that direction and would not be
maximal.

The maximal rectangle overall must be in the set of maximal rectangles that end
at a particlar right boundary i.  Partitioning this set by right boundary is an
example of the MEE (Mutually Exclusive and Exhaustive) partitioning.

Since the partitioning is exhaustive, we are guaranteed to find the optimal
answer.  Since it is mutually exclusive, we are guaranteed not to do any extra
work.

So, this problem reduces to 1) finding the maximal rectangle that ends at
position i, and 2) repeating this for all i and taking the maximum among these
solutions.

Then, how do you find the maximal rectangle ending at a particular i?  First
note that only positions i where the graph descends contain maximal rectangles.
If the graph ascends at i, then any rectangles ending there could be extended
to the right, and thus would not be maximal.

Second, the process of finding the maximal rectangle then involves "snaking"
backwards, maximizing height for a given left bound, then lowering height while
maximizing left bound (pushing it as far left as possible).  We do this as long
as the height stays above the graph's right boundary.  
"""

