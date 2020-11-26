K = 8#int(input())  # 배낭의 크기
n = 5#int(input())  # 아이템 갯수
size_n = [4,3,2,4,3]#[int(x) for x in input().split()]  # n개의 크기
value_n = [12,9,4,8,12]#[int(x) for x in input().split()]  # n개의 가치

copy_size_n = size_n[:]
copy_value_n = value_n[:]
MaxProfit = 0  # 최대 가치


def quick_sort(A, first, last):  # 가성비를 기준으로 QuickSort를 진행하는데, 내림차순으로 정렬을 할 것이다.
    if first >= last:  # 탈출조건
        return
    p = A[first]  # 첫번쨰를 피봇으로
    left = first + 1  # 피봇을 제외하고 나머지 리스트에서 왼쪽 끝
    right = last  # 피봇을 제외하고 나머지 리스트에서 오른쪽 끝
    while left <= right:  # 교차되기 전까지 실행
        while left <= last and A[left] > p:  # 피봇보다 작은 값들을 찾음
            left += 1
        while A[right] < p:  # 피봇보다 큰 값들을 찾음
            right -= 1
        if left <= right:  # 바뀌면 서로 지나쳤다는 것이 되므로 교환을 실행
            A[left], A[right] = A[right], A[left]  # left는 피봇보다 작은 값, right는 피봇보다 큰 값을 swap

            # 가성비 리스트를 기준으로 해서 매칭되는 기존의 n개의 크기리스트와 n개의 가치 리스트도 서로 swap
            size_n[left], size_n[right] = size_n[right], size_n[left]
            value_n[left], value_n[right] = value_n[right], value_n[left]
            left += 1
            right -= 1

        # 가성비 리스트를 기준으로 해서 매칭되는 기존의 n개의 크기리스트와 n개의 가치 리스트도 서로 swap
    A[first], A[right] = A[right], A[first]
    size_n[first], size_n[right] = size_n[right], size_n[first]
    value_n[first], value_n[right] = value_n[right], value_n[first]
    # 나머지 부분에 대해서 QuickSort를 실행
    quick_sort(A, first, right - 1)
    quick_sort(A, right + 1, last)


# x리스트(어떤 아이템을 선택했는지 정보가 담겨있는 리스트)를 기준으로 Knapsack에서 파라미터로 받은 idx의 바로 직전 idx까지 배낭에 담긴 아이템의 크기, 가치의 합을 구한다.
def get_pv_sv(x, idx):
    result_p = 0  # 가치의 합을 구하기 위한 변수
    result_s = 0  # 크기의 합을 구하기 위한 변수
    for i in range(0, idx):  # x리스트의 처음부터 idx바로 직전까지 for loop을 돌며 p(v)와 s(v)를 구해준다.
        if x[i] == 1:  # 만약 특정 아이템을 선택했을 경우
            result_p += value_n[i]  # 그 아이템의 가치를 +
            result_s += size_n[i]  # 그 아이템의 크기를 +
    return result_p, result_s  # return


# 가성비에 따라서 가방의 남은 크기에 들어갈 수 있는 최대 가치를 반환할 함수. Knapsack 함수에서 i+1로 넘겨주기 때문에 Knapsack에서 접근한 바로 다음 아이템들부터 계산한다.
def get_fraction_sum(idx, size):
    result = 0  # 가방의 남은 크기에 따라 가능한 최대 가치를 저장할 변수
    for i in range(idx, n):  # Knapsack에서 접근한 아이템 바로 다음 아이템부터 판별을 시작
        # 만약 남은 크기보다 지금 접근한 아이템의 크기가 더 클 경우. 전체가 들어갈 수 없으니 남은 부분만큼만 들어간다고 생각한다.
        # 가성비를 기준으로 오름차순으로 정렬되어 있어서 바로 구해주면 최대 가치가 계산될 것이다.
        if size <= size_n[i]:
            result += size * cost_perfomance[i]  # 사이즈를 넘어버리는 아이템을 남은 사이즈만큼 넣어준다고 생각하고, 해당 아이템의 가성비를 구하고, 그것이 남은 size의 크기만큼 들어갈 수 있으니 둘을 곱해서 기존의 result와 더한 값을 result에 update
            break  # size를 이미 넘어버린다고 했기 때문에 굳이 더 계산할 필요가 없으므로 break
        result += value_n[i]  # 남은 사이즈보다 지금 접근한 아이템의 사이즈가 더 작아서 그대로 들어갈 수 있기 때문에 지금 접근한 아이템의 가치를 result에 더해서 update
        size -= size_n[i]  # i번째 아이템의 사이즈를 빼줌으로써 i번째 아이템이 들어가고 난 후의 size로 업데이트
    return result  # 나머지 size로 가능한 최대 가치의 값을 return


def Knapsack(i, size):
    global MaxProfit  # 최대 가치의 값
    if i >= n or size <= 0:  # i가 모든 아이템의 순회를 마쳤거나, size가 꽉 찬 경우 종료. 즉 바닥조건
        return
    pv, sv = get_pv_sv(x, i)  # i의 바로 직전 아이템까지 배낭에 담긴 아이템의 크기, 가치의 합을 구한다.
    if size_n[i] <= size:  # 접근한 아이템의 크기보다 배낭의 남은 크기가 더 크다면
        B = get_fraction_sum(i + 1, size - size_n[i])  # 접근한 아이템을 선택했을 떄 가방의 남은 사이즈에 나머지 아이템들로 구할 수 있는 최대 가치
        if MaxProfit < pv + value_n[
            i] + B:  # 기존에 담긴 아이템들로 구할 수 있는 가치(pv)와 fraction_sum을 거쳐 얻을 수 있을 것이라고 예상되는 가치(B)와 현재 아이템을 선택한다고 했을 때(value_n[i]) 가치가 MaxProfit보다 작으면 굳이 실행될 필요가 없으므로 MaxProfit이 더 작을 때 실행
            x[i] = 1  # 현재 접근한 아이템을 선택했다고 표시
            MaxProfit = max(MaxProfit, pv + value_n[
                i])  # i번째 아이템 바로 직전까지 아이템들의 가치의 합과 현재 선택한 아이템의 가치를 더한 것과 기존의 MaxProfit중 더 큰 값으로 update
            Knapsack(i + 1,
                     size - size_n[i])  # 다음 아이템을 접근하고, 현재 접근한 아이템을 선택했기 때문에 size에서 현재 아이템의 사이즈(value_n[i])를 빼준다.

    B = get_fraction_sum(i + 1, size)  # 접근한 아이템을 선택하지 않았을 떄 가방의 남은 사이즈에 나머지 아이템들로 구할 수 있는 최대 가치
    if MaxProfit < pv + B:  # 기존에 담긴 아이템들로 구할 수 있는 가치(pv)와 fraction_sum을 거쳐 얻을 수 있을 것이라고 예상되는 가치(B)가 MaxProfit보다 작으면 굳이 실행될 필요가 없으므로 MaxProfit이 더 작을 때 실행
        x[i] = 0  # 현재 접근한 아이템을 선택하지 않았다고 설정
        Knapsack(i + 1, size)  # 다음 아이템을 접근하고, 현재 접근한 아이템을 선택하지 않았기 때문에 size는 그대로


x = [0] * n  # n개의 아이템 갯수 중 선택한 것을 0/1로 표현하기 위한 리스트
cost_perfomance = [a / b for (a, b) in zip(value_n, size_n)]  # 각 아이템에 대해 가치/크기로 가성비의 값들이 담겨있는 리스트를 구성한다.

quick_sort(cost_perfomance, 0, len(cost_perfomance) - 1)  # 가성비를 기준으로 내림차순으로 정렬한다.

Knapsack(0, K)  # K크기의 배낭에 담을 수 있는 아이템의 최대 가치를 찾는 Knapsack 실행
print(int(MaxProfit))  # 최대 가치를 정수형으로 출력

