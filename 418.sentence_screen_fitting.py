"""
Given a rows x cols screen and a sentence represented as a list of strings, return
the number of times the given sentence can be fitted on the screen.

The order of words in the sentence must remain unchanged, and a word cannot be split
into two lines. A single space must separate two consecutive words in a line.

Brilliant solution from dilit.

My attempted solution is not even worth reporting, it was so complicated.
"""
class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        s = ' '.join(sentence) + ' '
        start = 0
        for i in xrange(rows):
            start += cols - 1
            if s[start % len(s)] == ' ':
                start += 1
            elif s[(start + 1) % len(s)] == ' ':
                start += 2
            else:
                while start > 0 and s[ (start - 1) % len(s) ] != ' ':
                    start -= 1
        return start/ len(s)


