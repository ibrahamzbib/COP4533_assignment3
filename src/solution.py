import sys


def parse_input(filename):
    
    if filename is not None:
        f = open(filename, "r")
        lines = f.read().split()
        f.close()
    else:
        print("invalid file name\n")
        sys.exit(1)
        

    idx = 0

    k = int(lines[idx])
    idx += 1

    char_values = {}
    for i in range(k):
        char = lines[idx]
        val = int(lines[idx + 1])
        char_values[char] = val
        idx += 2

    a = lines[idx]
    b = lines[idx + 1]

    return char_values, a, b


def solve(char_values, a, b):
    m = len(a)
    n = len(b)
 
    # dp[i][j] = best value achievable from a common subsequence of a[:i] and b[:j]
    dp = []
    for i in range(m + 1):
        row = []
        for j in range(n + 1):
            row.append(0)
        dp.append(row)
 
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + char_values.get(a[i - 1], 0)
            else:
                if dp[i - 1][j] >= dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]
 
    # walk back through the table to reconstruct the actual subsequence
    result = []
    i = m
    j = n
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            result.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
 
    result.reverse()
    subseq = "".join(result)
 
    return dp[m][n], subseq
 
def main():
    filename = None
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    char_values, a, b = parse_input(filename)
    max_val, subseq = solve(char_values, a, b)
 
    print(max_val)
    print(subseq)
 


if __name__ == "__main__":
    main()