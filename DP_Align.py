
import math
W=int(input())
words = input().split()

DP_table = [[0]*(len(words)) for _ in range(len(words))]

for i in range(len(words)):
    DP_table[i][i]=(W-len(words[i]))**3 #대각선 패널티 구하기. 일종의 바닥조건

def DP_Align(n):
    for start in range(1,n):
        for row in range(n-start):
            w=W
            col=row+start
            DP_table[row][col]=math.inf
            for k in range(row,col):
                w = w - len(words[k]) - 1
                cost1 = (w-len(words[k+1]))**3
                cost2 = DP_table[row][k]+DP_table[k+1][col]
                if DP_table[row][col]>cost2:
                    DP_table[row][col]=cost2
            if cost1>=0:
                DP_table[row][col]=cost1
    return DP_table[0][n-1]


min_cost = DP_Align(len(words))
print(min_cost)






