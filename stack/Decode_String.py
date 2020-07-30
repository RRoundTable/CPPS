'''
link: https://leetcode.com/problems/decode-string/
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''
class Solution:
    def decodeString(self, s: str) -> str:
        digits, stack, ans = [str(s) for s in range(0, 10)], [], ''
        for ele in s:
            if ele == ']':
                inside, num = '', ''
                while True:
                    top = stack.pop()
                    if top == '[': break
                    inside = top + inside
                while stack and stack[-1] in digits: 
                    num = stack.pop() + num
                inside = inside * int(num) if num else inside
                stack.append(inside)
            else:
                stack.append(ele)
        for ele in stack: ans += ele
        return ans

class Solution:
    def decodeString(self, s: str) -> str:
        stack, ans = [], ''
        for c in s:
            if c in ']':
                sub = ''
                while stack:
                    if stack[-1] == '[':
                        stack.pop()
                        k = ''
                        while stack and stack[-1] in '1234567890':
                            k = stack.pop() + k
                        stack.append(int(k) * sub)
                        break
                    sub = stack.pop() + sub
            else:
                stack.append(c)
                
        return "".join(stack)