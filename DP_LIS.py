def print_IS(seq,x):
    for i in range(len(seq)):
        if x[i]:
            print(seq[i],end="")
        else:
            print("_",end="")
    print()


def LIS_DP(seq):
    count = 1 #LIS를 구하기 위해 사용될 변수
    x = [0] * len(seq) #LIS를 확인하기 위한 리스트
    DP = [0] * len(seq) #DP table
    x[0]=1 #길이가 1인 요소의 LIS는 자기 자신이니 1을 체크
    DP[0]=1 # 1개의 요소의 최장 길이는 1

    for i in range(1,len(seq)): #문자열의 두 번재부터 판별을 시작
        for j in range(1,i+1): #두 번째 요소부터 i+1번째까지 반복문을 돌면서 최장길이가 무엇인지 찾아낸다.
            if seq[i-j]<seq[i]: #기준으로 정한 seq 리스트의 i번째 리스트의 문자를 기준으로 그 앞에 있는 문자들을 모두 비교한다.
                DP[i] = max(DP[i-j],DP[i])  
                #특정 기준을 정하고 바로 직전부터 비교를 하면서 마지막으로 seq[j]를 포함하는 LIS를 찾는다.
                #DP[i]를 구하기 위해서 if문을 통해 문자를 비교하고, 만약 실행이 된다면, i-j번째에 위치한 문자로 구한 LIS의 길이와 반복문을 돌며 LIS를 구해가는 DP[i]의 max의 값을 저장한다.
                
        DP[i]+=1 #그 전과 비교하면서 자신을 제외하고 가능한 LIS를 구했는데, 자기자신도 포함되어야 하기 때문에 +1을 해준다.
        if DP[i]>count: #count는 가능한 LIS를 구하기 위해서 사용. 처음 1로 초기화한 이유는 x[0]은 자기자신이 포함될 수 있기 때문에 1을 체크하고, 가장 긴 LIS의 수를 체크
            x[i]=1 # DP[i]가 count보다 클 때라는 것은 이전의 가장 긴 LIS보다 가능한 큰 LIS를 찾아냈다는 것이므로, i번째 요소가 기준이 된 것이기 때문에 x[i]를 1을 체크한다.
            count+=1 #최장 LIS의 길이를 1증가시켜 주는 것이라고 보면 된다.
    print(DP)
    return x,max(DP)





seq = input() #문자열 입력
lis, x = LIS_DP(seq)
print_IS(seq,lis)
print(x)

