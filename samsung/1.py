

def solve(matrix):
    possible = [[True] * len(matrix) for _ in range(len(matrix))]
    cores = []
    
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == '1':
                cores.append([i,j])
     
    def restore(possible, history):
        for i, j in history:
            possible[i][j] = True
                
    def backtracking(count, length, possible):
        nonlocal maxcount
        ans[count] = min(ans.get(count, float('inf')), length)
        maxcount = max(maxcount, count)
        try:
            i, j = cores[count]
        except:
            return
        if i == 0 or j == 0:
            if possible[i][j]:
            	possible[i][j] = False
            	backtracking(count + 1, length, possible)
        else:
            history = []
            if possible[i][j]:
                for r in range(i+1):
                    if possible[r][j]:
                        possible[r][j] = False
                        history.append([r, j])
                    else: break
                if r == i:
                    backtracking(count + 1, length + i - 1, possible)
                restore(possible, history)
                
                history = []
                for r in range(i, n):
                    if possible[r][j]:
                        possible[r][j] = False
                        history.append([r, j])
                    else: break
                if  r == n - 1:
                    backtracking(count + 1, length + n - i - 1, possible)
                restore(possible, history)
                history = []
                for c in range(j+1):
                    if possible[i][c]:
                        possible[i][c] = False
                        history.append([i, c])
                    else:
                        break
                if c == j:
                    backtracking(count + 1, length + j - 1, possible)
                restore(possible, history)
                
                history = []
                for c in range(j, n):
                    if possible[i][c]:
                        possible[i][c] = False
                        history.append([i, c])
                    else:
                        break
                if c == n - 1:
                    backtracking(count + 1, length + n - j - 1, possible)
                restore(possible, history)
        
    ans, maxcount, n = {}, 0, len(matrix)
    backtracking(0, 0, possible)
    return ans[maxcount] + 1


if __name__ == "__main__":
    n = int(input().strip())
    samples = []
    for i in range(n):
        nrow = int(input().strip())
       	temp = []
        for _ in range(nrow):
            row = input()
            row = row.split()
            temp.append(row)
        samples.append(temp)
        # print(solve(temp))
        print("#{}".format(i+1), solve(temp))
    
        