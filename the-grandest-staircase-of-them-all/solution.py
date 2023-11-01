def solution(n):
    stairs = [None]*(n+1)
    for i in range(n+1):
        stairs[i] = [None]*(n+1)
        for j in range(n+1):
            stairs[i][j] = 0

    stairs[0][0] = 1
    for i in range(1, n+1):
        for j in range(n+1):
            stairs[i][j] = stairs[i-1][j]
            if j >= i:
                stairs[i][j] += stairs[i-1][j-i]
    return stairs[n][n] - 1


if __name__ == "__main__":
    print(solution(3))
    print(solution(4))
    print(solution(5))
    print(solution(200))

