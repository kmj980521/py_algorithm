
import random, timeit


def find_index(A, first, i, num):  # quick sort와 insertion sort할 때 사용
    global QIc
    for k in range(i - 1, first - 1, -1):  # 인자로 받은 A[i-1]인덱스 전부터 A[0] 값을 비교하는 반복문

        if A[k] <= num:  # 만약 num이 특정 인덱스 k의 값 A[k]보다 크거나 같다면 그곳이 num이 위치할 곳
            QIc += 1  # quick insertion sort의 비교횟수 1증가
            return k + 1  # k다음으로 와야 하기 때문아 k+1
    return first  # 만약 반복문을 모두 돌았는데 return k+1이 실행되지 않는다면 num이 제일 작다는 의미이므로 리스트 첫 번쨰인 0을 반환


def insertion_sort(A, first, last):

    global QIs
    for i in range(first + 1, last + 1):  # 첫번째는 정렬되어 있다고 가정.즉 first+1부터 접근해서 last까지 진행
        m = find_index(A, first, i, A[i])  # find_index(A, first i, x)는 A[m-1] <= x < A[m]을 만족하는 배열 인덱스 m를 리턴함
        for j in range(i, m, -1):  # A[i]가 A[m]에 위치해야 하므로, A[m], ..., A[i-1] 원소는 오른쪽으로 한 칸씩 이동함.
            A[j], A[j - 1] = A[j - 1], A[j]
            QIs += 1



def find_index2(A, first, i, num):
    global MIc
    for k in range(i - 1, first - 1, -1):  # 인자로 받은 A[i-1]인덱스 전부터 A[0] 값을 비교하는 반복문
        if A[k] <= num:  # 만약 num이 특정 인덱스 k의 값 A[k]보다 크거나 같다면 그곳이 num이 위치할 곳
            MIc += 1  # quick insertion sort의 비교횟수 1증가
            return k + 1  # k다음으로 와야 하기 때문아 k+1
    return first  # 만약 반복문을 모두 돌았는데 return k+1이 실행되지 않는다면 num이 제일 작다는 의미이므로 리스트 첫 번쨰인 0을 반환


def insertion_sort2(A, first, last):
    global MIs
    for i in range(first + 1, last + 1):  # 첫번째는 정렬되어 있다고 가정.
        m = find_index2(A, first, i, A[i])  # find_index(A, i, x)는 A[m-1] <= x < A[m]을 만족하는 배열 인덱스 m를 리턴함

        for j in range(i, m, -1):  # A[i]가 A[m]에 위치해야 하므로, A[m], ..., A[i-1] 원소는 오른쪽으로 한 칸씩 이동함.
            A[j], A[j - 1] = A[j - 1], A[j]
            MIs += 1


def merge_two_sorted_list2(A, first, last):
    global MIc, MIs
    m = (first + last) // 2
    i, j = first, m + 1
    B = []  # 복사할 리스트 n만큼의 메모리를 추가 사용하기 때문에 Not-in-place!
    while i <= m and j <= last:  # 둘 중 하나라도 범위를 벗어나면 반복 종료
        MIc += 1
        if A[i] <= A[j]:  # 왼쪽 리스트의 값이 더 작은 수가 오면 B에 append
            B.append(A[i])
            i += 1
        else:  # 오른쪽 리스트의 값이 더 작은 수가 오면 B에 append
            B.append(A[j])
            j += 1

    for k in range(i, m + 1):  # 왼쪽 리스트의 남은 값들을 B에 append
        B.append(A[k])
    for k in range(j, last + 1):  # 오른쪽 리스트의 남은 값들을 B에 append
        B.append(A[k])
    # --- 여기까지 모든 리스트를 돌아가며 비교했기 때문에 cn

    # 둘 중 하나는 이미 특정 범위를 넘어서서 while을 벗어났기 때문에 둘 중 하나만 실행된다.
    for i in range(first, last + 1):
        A[i] = B[i - first]  # B[0]인 값이 A의 first로 가게 된다.
    # n개를 복사하기 때문에 O(n)
    MIs += 2 * (last - first + 1)  # last-fist+1로 리스트의 요소의 수를 구해주는데 2개의 리스트로 진행하기 때문에 *2


def special_merge(A, first, last):  # merge sort와 insertion sort를 실행하는 함수
    if last-first>10 and last - first < 40:
        insertion_sort2(A, first, last)
        return
    special_merge(A, first, (first + last) // 2)
    special_merge(A, (first + last) // 2 + 1, last)
    merge_two_sorted_list2(A, first, last)


def quick_sort(A, first, last):
    global Qs, Qc
    if first >= last: return  # 탈출조건
    p = A[first]  # 피봇을 리스트의 맨 처음으로 설정
    left = first + 1  # 피봇 바로 다음 값
    right = last
    while left <= right:
        while left <= last and A[left] < p:  # last보다 왼쪽에서 리스트를 탐색하고 p보다 큰 값을 만날 때까지 실행
            Qc += 1  # Quick_Sort의 비교횟수 1증가
            left += 1
        while A[right] > p:  # p보다 작은 값을 만날 떄까지 실행
            Qc += 1  # Quick_Sort의 비교횟수 1증가
            right -= 1
        if left <= right:  # left와 right가 바뀌면 크기 관계가 지나친 것이므로 left가 right보다 작거나 같을 때만 실행
            A[left], A[right] = A[right], A[left]
            Qs += 1  # Quick_Sort의 교환횟수 1증가
            left += 1
            right -= 1
    A[first], A[right] = A[right], A[first]  # 피봇의 값을 분류한 리스트의 가운데로 swap
    # 피봇보다 작은값, 큰값, 같은값 나누기
    Qs += 1  # Quick_Sort의 교환횟수 1증가
    quick_sort(A, first, right - 1)
    quick_sort(A, right + 1, last)

def special_quick(A,first,last):
    global QIc
    if len(A)<=1:
        return A
    if len(A)>10 and len(A)<40:
        insertion_sort(A, 0, len(A) - 1)
        return A
    pivot=A[len(A)//2]
    S,M,L=[], [], []
    for x in A:
        QIc+=1
        if x<pivot : S.append(x)
        elif x>pivot : L.append(x)
        else: M.append(x)

    return special_quick(S,0,len(S))+M+special_quick(L,0,len(S))


def merge_two_sorted_list(A, first, last):
    global Mc, Ms
    m = (first + last) // 2
    i, j = first, m + 1
    B = []  # 복사할 리스트 n만큼의 메모리를 추가 사용하기 때문에 Not-in-place!
    while i <= m and j <= last:  # 둘 중 하나라도 범위를 벗어나면 반복 종료
        Mc += 1
        if A[i] <= A[j]:  # 왼쪽 리스트의 값이 더 작은 수가 오면 B에 append
            B.append(A[i])
            i += 1
        else:  # 오른쪽 리스트의 값이 더 작은 수가 오면 B에 append
            B.append(A[j])
            j += 1

    for k in range(i, m + 1):  # 왼쪽 리스트의 남은 값들을 B에 append
        B.append(A[k])
    for k in range(j, last + 1):  # 오른쪽 리스트의 남은 값들을 B에 append
        B.append(A[k])
    # --- 여기까지 모든 리스트를 돌아가며 비교했기 때문에 cn

    # 둘 중 하나는 이미 특정 범위를 넘어서서 while을 벗어났기 때문에 둘 중 하나만 실행된다.
    for i in range(first, last + 1):
        A[i] = B[i - first]  # B[0]인 값이 A의 first로 가게 된다.
    # n개를 복사하기 때문에 O(n)
    Ms += 2 * (last - first + 1)  # last-fist+1로 리스트의 요소의 수를 구해주는데 2개의 리스트로 진행하기 때문에 *2


def merge_sort(A, first, last):
    if first >= last:
        return
    merge_sort(A, first, (first + last) // 2)
    merge_sort(A, (first + last) // 2 + 1, last)
    merge_two_sorted_list(A, first, last)
    # 강제로 2개로 나누고, 정렬된 두 리스트를 합병하는데 T(n)=2T(n/2) + cn


def heapify_down(A, idx, n):
    comp, swap = 0, 0
    while 2 * idx + 1 < n:  # idx번째 값에 있는 노드의 왼쪽 자식노드의 인덱스는 2*idx+1이다. idx*2+1<n을 해줌으로써 접근하는 idx가 자식노드를 가진다면 반복문을 실행하고, 리프노드라면 실행하지 않는다.
        # 즉 idx는 왼쪽으로 자식노드를 갖거나, 왼쪽 오른쪽 자식노드를 모두 가진다.
        L, R = 2 * idx + 1, 2 * idx + 2  # 한 노드의 왼쪽 자식은 2*idx+1, 오른쪽은 2*idx+2
        comp += 2  # 왼쪽 혹은 오른쪽 자식노드와 비교횟수 2
        if L < n and A[L] > A[idx]:  # 접근한 노드의 값이 왼쪽 자식노드의 값보다 크다면 실행
            m = L
        else:
            m = idx
        if R < n and A[m] < A[R]:  # idx노드의 오른쪽 자식의 노드의 인덱스가 리스트A의 길이보다 작다면 idx노드는 오른쪽 자식 노드를 갖기 때문에 R<n을 조건으로 사용,
            # 기존의 idx와 왼쪽 자식노드를 비교했기 때문에 더 큰 값이 들어가있고, 오른쪽 자식노드와 값을 비교
            # 또한 R<n이 먼저 해야하는 이유는 A[m] < A[R]를 먼저하면 오른쪽 자식 노드가 없을 때 접근하기 때문에 IndexError 오류 발생
            m = R
        if m != idx:  # 만약 기존에 접근한 idx노드의 값이 자식노드의 인덱스와 비교해서 같지 않다면(즉 자식노드들 중에서 더 큰 값이 있다면) 힙 성질을 위배한 것
            A[idx], A[m] = A[m], A[idx]
            idx = m  # 기존의 idx가 m인덱스로 옮겨졌기 때문에 swap
            swap += 1  # swap 횟수 1증가
        else:  # m==idx는 idx 노드의 값이 자기 자리를 찾은 것
            break
    return comp, swap


def make_heap(A, n):
    global Hc, Hs
    for i in range(n - 1, -1, -1):  # 마지막 요소부터 처음까지
        cmp, swp = heapify_down(A, i, n)  # A리스트의 i인덱스부터 heapify_down을 실행하는데 n번 반복한다.
        Hc += cmp
        Hs += swp


def heap_sort(A):
    global Hc, Hs
    n = len(A)
    make_heap(A, n)
    for i in range(n - 1, -1, -1):
        Hs += 1  # HeapSort swap 횟수 1증가
        A[0], A[i] = A[i], A[0]  # 힙 구조에서 제일 위에있는 값(제일 큰 값)을 마지막으로 swap
        n = n - 1  # 큰 값들은 마지막과 swap하기 때문에 1씩 줄여가며 sort / 가장 큰 값이 리스트 마지막에 들어갔기 때문에 n=n-1을 먼저 해준다
        cmp, swp = heapify_down(A, 0, n)  # 최상단에는 마지막인 노드가 올라왔으니 다시 heapify_down실행
        Hc += cmp
        Hs += swp


def check_sorted(A):
    for i in range(n - 1):  # 리스트 전체를 돌며 오름차순인지 비교
        if A[i] > A[i + 1]: return False
    return True


Qc, Qs, Mc, Ms, Hc, Hs, QIc, QIs, MIc, MIs = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000, 1000))

B = A[:]
C = A[:]
D = A[:]
E = A[:]
F = A[:]
G = A[:]
print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))

print("")
print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))

print("")
print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

print("")
print("Merge_insertion sort:")
print("time =", timeit.timeit("special_merge(D, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(MIc, MIs))

print("")
print("Quick_insertion sort:")
print("time =", timeit.timeit("special_quick(E, 0, n-1)", globals=globals(), number=1))
E=special_quick(E,0,n-1)
QIc=QIc//2
QIs=QIs//2
print("  comparisons = {:10d}, swaps = {:10d}\n".format(QIc, QIs))


assert (check_sorted(A))
assert (check_sorted(B))
assert (check_sorted(C))
assert (check_sorted(D))
assert (check_sorted(E))

