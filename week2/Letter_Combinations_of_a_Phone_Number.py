"""

link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.


"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """O(4 ^ N)/ O(S)"""
        num2alpha = {
            "1": [],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        letters = []
        for i in range(len(digits)):
            if digits[i] != "1":
                letters.append(num2alpha[digits[i]])

        ans = []
        length = len(letters)

        if length < 1:
            return []

        def generate(L, idx):
            if len(L) == length:
                ans.append(L)
                return
            for i in range(len(letters[idx])):
                generate(L + letters[idx][i], idx + 1)

        generate("", 0)
        return ans
