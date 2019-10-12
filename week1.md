
## Generate Parentheses: solution

- brute force

time complexcity: O(N)
space complexity:

```python
class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(A = []):
            if len(A) == 2 * n:
                if self.valid(A):
                    results.append("".join(A))
            else:
                A.append("(")
                generate(A)
                A.pop()
                A.append(")")
                generate(A)
                A.pop()

        results = []
        generate()
        return results
    
    
    def valid(self, A):
        bal = 0
        for c in A:
            if c == "(":
                bal += 1
            else:
                bal -= 1
                if bal < 0:
                    return False
        return bal == 0
```

- backtracking

time complexcity:
space complexity:


```python
class Solution:
    def generateParenthesis(self, N: int) -> List[str]:
        ans = []
        def backtrack(S = "", left = 0, right = 0):

            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S + "(", left + 1, right)
            if right < left:
                backtrack(S + ")", left, right + 1)
        
        backtrack()
        ans = set(ans)
        return ans
```


## Product of Array Except Self: solution 

time complexcity: O(N)
space complexity:


```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        results = [1] * len(nums)
        for i in range(1, len(nums)):
            results[i] = results[i-1] * nums[i-1]
        
        rightproduct = 1
        for i in range(len(nums) - 1, -1, -1):
            results[i] = results[i] * rightproduct
            rightproduct *= nums[i]
        return results
```


## Game of Life: solved

time complexcity: O(MN)
space complexity:

```python
import copy
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nrows = len(board)
        ncols = len(board[0])
        total_sum = []
        
        original = copy.deepcopy(board)
        for row in range(nrows):
            
            row_sum = []
            for col in range(ncols):
                queue = []
                high_row = min(row + 1, nrows - 1)
                low_row = max(row - 1, 0)
                high_col = min(col + 1, ncols - 1)
                low_col = max(col - 1, 0)
                height = high_row - low_row
                width = high_col - low_col
                
                temp = self.get_sum(original, low_row, high_row, low_col, high_col)

                if original[row][col] == 1:
                    temp -= 1
                    if temp < 2 or temp > 3:
                        board[row][col] = 0
                    else:
                        continue
                else:
                    if temp == 3:
                        board[row][col] = 1
                # print("#" * 6)
                # print(low_row, high_row)
                # print(low_col, high_col)
                # print(temp)
                # print(row, col)
          
    def get_sum(self, matrix, low_row, high_row, low_col, high_col):
        temp = 0
        for i in range(low_row, high_row+1):
            for j in range(low_col, high_col+1):
                temp += matrix[i][j]
        return temp

```


## Reorder Data in Log Files: solved

time complexcity: O(N)
space complexity:

```python
import re
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        digit = []
        letter = []
        p = re.compile("[0-9]+")
        for i in range(len(logs)):
            words = logs[i].split(" ")
            identifier = p.findall(words[1][0])
            if len(identifier) > 0:
                digit.append(logs[i])
            else:
                letter.append(logs[i])
        
        letter = sorted(letter, key=lambda x:x[len(x.split(" ")[0]):])
        
        for i in range(len(letter) - 1):
            temp1 = letter[i].split(" ")[1:]
            temp2 = letter[i + 1].split(" ")[1:]
            if temp1 == temp2:
                total = sorted([letter[i], letter[i+1]], key=lambda x:x.split(" ")[0])
                letter[i], letter[i + 1] = total           
        return letter + digit
```

