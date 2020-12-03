import math


def relax(u, v):  # 특정노드 u를 거쳐서 가는 것이 이득이면 업데이트 해주는 함수
    if dist[v] > dist[u] + cost[u, v]:
        dist[v] = dist[u] + cost[u, v]


class AdaptedHeap:
    class Locator:
        def __init__(self, key, j):
            self.key = key  # key값. 즉 d[v]값
            self.index = j  # key값에 저장된 index / 노드번호

    def __init__(self, L=[]):
        self.A = L  # distance를 받아옴
        self.keys = {}  # 각 노드가 A리스트 어디에 위치하고 있는지 딕셔너리로 저장.
        for i in range(len(L)):  # n개의 노드에 대해서 Locator를 만들기 때문에 O(n)의 수행시간을 가진다.
            self.A[i] = self.Locator(self.A[i],
                                     i)  # A[i]의 원소(distance값을 받아서 계속 pop할 원소들)는 자신의 key값(d[i])와 노드 번호를 표현하는 index값을 속성으로 가진다.
            self.keys[i] = i  # 각 노드가 A의 어느 위치에 있는지 딕셔너리로 저장. 예를 들면 0번노드(A)는 A리스트의 0번째에 위치 ...

    def __str__(self):
        return str(self.A)

    def __len__(self):
        return len(self.A)

    def make_heap(self):  # n개의 노드에 대해서 heapify_down을 거쳐 min_heap구조로 만든다.
        n = len(self.A)
        for k in range(n - 1, -1, -1):  # n개의 노드에 대해서 heapify_down을 거쳐 min_heap구조로 만든다. 수행시간은 O(nlogn)
            self.heapify_down(k, n)

    def heapify_up(self, k):  # 인덱스 i에 저장된 item을 up 수행시간은 O(logn)
        while k > 0 and self.A[(k - 1) // 2].key > self.A[k].key:  # 현재 노드와 부모노드의 key값을 비교
            self.A[k], self.A[(k - 1) // 2] = self.A[(k - 1) // 2], self.A[k]  # 이동

            # k번째와 (k-1)//2번째 노드를 바꿔줬기 때문에 A리스트에서 (k-1)//2와 k에 해당하는 인덱스에 위치한 노드의 index(노드 번호)가 저장된 딕셔너리에서 value값을  swap
            self.keys[self.A[k].index], self.keys[self.A[(k - 1) // 2].index] = self.keys[self.A[(k - 1) // 2].index], \
                                                                                self.keys[self.A[k].index]
            k = (k - 1) // 2  # 부모 노드로 이동

    def heapify_down(self, idx, n):  # 수행시간은 O(logn)
        while 2 * idx + 1 < n:  # idx번째 값에 있는 노드의 왼쪽 자식노드의 인덱스는 2*idx+1이다. idx*2+1<n을 해줌으로써 접근하는 idx가 자식노드를 가진다면 반복문을 실행하고, 리프노드라면 실행하지 않는다.
            # 즉 idx는 왼쪽으로 자식노드를 갖거나, 왼쪽 오른쪽 자식노드를 모두 가진다.
            L, R = 2 * idx + 1, 2 * idx + 2  # 왼쪽 자식노드는 자신의 idx에 2를 곱하고 1을 더함 / 오른쪽 자식노드는 자신의 idx에 2를 곱하고 2를 더함
            if L < n and self.A[L].key < self.A[
                idx].key:  # 접근한 노드의 값이 왼쪽 자식노드의 값보다 크다면 실행 -> 내려가야함 / <인 이유 ->최소힙을 구현하기 위해서
                m = L
            else:
                m = idx  # 아니라면 그자리 그대로
            if R < n and self.A[m].key > self.A[R].key:  # R번 노드가 n보다 작을 때 즉, 노드가 존재할 때 이번엔 오른쪽 자식 노드와 비교
                m = R  # 키값이 더 크다면 새로 업데이트
            if m != idx:  # 새로 배정받은 위치가 기존의 idx와 다르다면 이동
                self.A[idx], self.A[m] = self.A[m], self.A[idx]
                ##idx번째와 m번째 노드를 바꿔줬기 때문에 A리스트에서 idx와 m에 해당하는 인덱스에 위치한 노드의 index(노드 번호)가 저장된 딕셔너리에서 value값을  swap
                self.keys[self.A[idx].index], self.keys[self.A[m].index] = self.keys[self.A[m].index], self.keys[
                    self.A[idx].index]
                idx = m
            else:  # 자기 자리를 찾았으면 break
                break

    def delete_min(self):  # heapify_down연산으로 인해 수행시간은 O(logn)
        if len(self.A) == 0: return None
        key = self.A[0]  # 제일 위의 노드의 정보를 백업
        self.A[0], self.A[len(self.A) - 1] = self.A[len(self.A) - 1], self.A[0]  # 제일 위의 노드와 마지막 노드를 바꿔준다.
        ##0번째와 A리스트의 마지막 노드를 바꿔줬기 때문에 A리스트에서 m번째와 마지막에 해당하는 인덱스에 위치한 노드의 index(노드 번호)가 저장된 딕셔너리에서 value값을  swap
        self.keys[self.A[0].index], self.keys[self.A[len(self.A) - 1].index] = self.keys[self.A[len(self.A) - 1].index], \
                                                                               self.keys[self.A[0].index]
        self.A.pop()  # 기존에 위에 있던 노드가 제일 마지막으로 왔기 때문에 pop
        self.heapify_down(0, len(self.A))  # 새로 올라간 0번 노드에 대해서 heapify_down을 거치면서 힙구조 유지 O(nlogn)
        return key.index  # 맨 위에 있는 노드 몇번 인덱스에 있었는지를 반환

    def decrease_key(self, v,
                     distance):  # index를 얻는 연산은 상수시간 O(1)이고, heapify_up하는 과정은 O(logn)이기 때문에 O(logn)의 수행시간을 갖는다.
        idx = self.keys[v]  # 딕셔너리를 통해서 v노드가 현재 A리스트 어디에 위치해 있는지 정보를 얻는다. 상수시간 O(1)
        self.A[idx].key = distance  # 그 노드에 새로운 distance를 부여한다.
        self.heapify_up(idx)  # 그 노드의 key값이 바뀌었기 때문에 min_heap 구조를 위해 heapify_up을 거친다. O(logn)의 수행시간을 가진다.


def Dijkstra():
    n = int(input())  # 노드 개수
    m = int(input())  # 에지 개수
    cost = {}  # u에서 v로 가는 간선의 가중치가 담길 딕셔너리
    edges = [[] for _ in range(n)]  # n개의 노드의 인접성을 알기위한 연결리스트
    # 간선의 개수만큼 u,v,w (시작점, 종점, 가중치)를 입력받아서 u에서 v로가는 가중치 w는 cost 딕셔너리에 저장 및 u와 v는 인접하기 때문에 u번 노드가 v에 연결됨
    for i in range(m):  # m개의 에지만큼 반복문을 돌기 때문에 O(m)이다. m은 노드의 개수(n)의 ^2개 까지 되기 때문에 O(n^2)의 수행시간을 가진다.
        u, v, w = map(int, input().split())
        cost[u, v] = w
        edges[u].append(v)

    dist = [math.inf] * n  # 소스부터의 거리
    dist[0] = 0  # 소스 0번부터 자기 자신까지의 거리

    dist2 = dist[:]  # dist리스트를 복사해서 힙에서 사용
    h1 = AdaptedHeap(dist[:])  # h1이라는 적응형 힙을 만들어줌 /n개의 노드 개수만큼 Locator를 만들기 때문에 O(n)의 수행시간을 가진다.
    h1.make_heap()  # h1을 min_heap구조로 만든다.  / n개의 노드 개수만큼 heapfity_down을 거쳐 min_heap 구조를 만들기 때문에 O(nlogn)의 수행시간을 가진다.

    while len(h1):
        u = h1.delete_min()  # 힙의 가장 위의 값 즉 d[v]가 작은 노드의 index(노드 번호)를 반환받는다. / n개의 노드 개수만큼 pop하고 heapify_down을 거쳐 min_heap 구조를 만들기 때문에 O(nlogn)의 수행시간을 가진다.

        # 각 에지에 대해서 decrease_key연산을 하는데, decrease_key는 O(logn)의 시간복잡도를 가진다. 에지는 최대 (노드의 수)^2개 까지 가능하기 때문에 이 연산의 수행시간은 O(n^2logn)이다.
        for v in edges[u]:  # u(노드번호)와 인접한 노드에 대해서 실행
            if (u, v) in cost:  # 만약 u에서 v로 갈 수가 있다면
                if dist[v] > dist[u] + cost[u, v]:  # relax과정을 실행
                    dist[v] = dist[u] + cost[u, v]
                    # v노드에 대해서 d[v]가 바뀌었으므로 decrease_key연산을 진행
                    h1.decrease_key(v, dist[
                        v])  # n개의 노드에 대해서 현재 A리스트 어디에 위치해있는지 얻는 수행시간은 상수시간 O(1), heapify_up과정을 거치기 때문에 O(logn)의 수행시간을 가진다.

    for i in dist:  # 최종 결과를 출력 #n개의 노드만큼 출력을 하기 때문에 O(n)의 수행시간을 가진다.
        print(i, end=' ')


Dijkstra()
'''
1.m개의 에지만큼 반복문을 돌면서 cost와 인접리스트를 만드는 수행시간은 에지 개수는 최대 (노드의 수)^2만큼 가능하기 때문에 최대 O(n^2)의 수행시간을 가진다

2.h1의 힙을 만드는 과정은 각 노드마다 Locator를 만들고 A,B,C와 같은 노드를 0번, 1번, 2번을 부여해서 힙의 A리스트 어디에 위치하는지 기록하는 딕셔너리를 만들고, n개의 노드의 수만큼 반복문이 돌아가기 때문에 O(n)의 수행시간을 가진다.

3.h1을 min_heap으로 만드는 과정은 노드의 수만큼 heapify_down과정을 거치며 min_heap을 구현하는데, heapify_down은 O(logn)인데 이것이 n번 반복되므로 O(nlog)의 수행시간을 가진다.

4.h1.delete_min()은 n개의 노드의 수만큼 반복하면서 요소를 pop하고, 다시 heapify_down과정을 거치는데, heapfiy_down은 O(logn)이며 이것 또한 n번 반복되므로 O(nlogn)의 수행시간을 가진다.

5. 새로운 v노드에 대해서 새로운 dist[v]가 업데이트 되었으므로 decrease_key연산을 수행하는데, v노드가 힙의 어디에 위치하는지는 기존에 구현한 딕셔너리를 통해서 얻기 때문에 상수시간 O(1)이 걸리고, 노드의 key값을 새로 업데이트 해준 후, key값이 변경되었기 때문에 min_hewap을 위해 heapify_up을 수행하는데, heapify_up은 O(logn)시간을 가지기 때문에 decrease_key의 최종 수행시간은 O(logn)이다.

5. delete_min()을 통해 d[v]가 가장 작은 값을 가지는 노드를 받아온 후 이 노드에 인접한 노드들에 대해서 연산을 수행하는데, 모든 에지의 수는 최대 (노드의 수)^2까지 가능하고, 각각의 에지마다 decrease_key가 실행될 수 있기 때문에 최종 수행시간은 O(n^2logn)이다. 

6. 최종적으로 dist리스트에 대해서 모든 노드에 대해서 update된 값을 출력하는 것이기 때문에 O(n)의 수행시간을 가진다.

7. 각종 연산에 비교 및 교환은 상수 C로 생각한다.

최종 : 1~5에서 구한 수행시간을 모두 따졌을 때 가장 최고차항은 n^2logn이므로 이 알고리즘의 수행시간은 O(n^2logn)이다.
'''

