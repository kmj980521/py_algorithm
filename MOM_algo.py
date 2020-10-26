

#n,k=map(int, input('숫자 두 개를 입력하세요: ').split())

#L= list(map(int,input().split()))
def find_median_five(L):
    left_win, left_lose, right_win, right_lose = 0, 0, 0, 0

    if L[0]>L[1]:
        left_win=L[0]
        left_lose=L[1]
    else:
        left_win=L[1]
        left_lose=L[0]

    if L[2] > L[3]:
        left_win = L[2]
        left_lose = L[3]
    else:
        left_win = L[3]
        left_lose = L[2]


    if left_win > right_win:
        if L[4]>left_lose:
            left_win = L[4]
        else:
            left_win = left_lose
            left_lose = L[4]
    else:
        if L[4]>right_lose:
            right_win = L[4]
        else:
            right_win = right_lose
            right_lose = L[4]
    if left_win>right_win:
        if right_win > left_lose: return right_win
        else: return left_lose
    else:
        if left_win > right_lose: return left_win
        else: return right_lose

def MoM(L,k):
    if len(L)==1:
        return L[0]
    i =0
    A, B, M, medians = [], [], [], [] # A는 피봇보다 작은 집합, B는 큰 집합, M은 같은 집합
    while i + 4 < len(L):
        medians.append(find_median_five(L[i:i+5]))
        i += 5
    if i<len(L) and i+4>=len(L):
       p= L[i]
       for a in L:
           if a < p:A.append(a)#i는 0이므로 리스트 첫번째 값과 돈다.
           elif a>p: B.append(a)
           else: M.append(a)
       if k<=len(A):return MoM(A,k)
       elif k>len(A)+len(M):return MoM(B,k-len(A)-len(M))
       else: return p

    mom = MoM(medians,len(medians)//2)
    for v in L:
        if v< mom: A.append(v)
        elif v>mom: B.append(v)
        else: M.append(v)
    if k<=len(A): return MoM(A,k)
    elif k> len(A) + len(M): return MoM(B,k-len(A)-len(M))
    else: return mom
##주석##
L= [1,5,7,2,3,6]

result = MoM(L,3)
print(result)

if k > 10 and k < 40 or first >= last:
    insertion_sort(A, first, last)
    return
