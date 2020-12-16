import math

class AdaptedHeap:
    class Locator:
        def __init__(self, key, j):
            self.key = key  # key값. 즉 d[v]값
            self.index = j  # key값에 저장된 index / 노드번호

    def __init__(self, L=[]):
        self.A = L  # distance를 받아옴
        self.keys = {}  # 각 노드가 A리스트 어디에 위치하고 있는지 딕셔너리로 저장.
        for i in range(len(L)):  # n개의 노드에 대해서 Locator를 만들기 때문에 O(n)의 수행시간을 가진다.
            self.A[i] = self.Locator(self.A[i],i)  # A[i]의 원소(distance값을 받아서 계속 pop할 원소들)는 자신의 key값(d[i])와 노드 번호를 표현하는 index값을 속성으로 가진다.
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
            self.keys[self.A[k].index], self.keys[self.A[(k - 1) // 2].index] = self.keys[self.A[(k - 1) // 2].index], self.keys[self.A[k].index]
            k = (k - 1) // 2  # 부모 노드로 이동

    def heapify_down(self, idx, n):  # 수행시간은 O(logn)
        while 2 * idx + 1 < n:  # idx번째 값에 있는 노드의 왼쪽 자식노드의 인덱스는 2*idx+1이다. idx*2+1<n을 해줌으로써 접근하는 idx가 자식노드를 가진다면 반복문을 실행하고, 리프노드라면 실행하지 않는다.
            # 즉 idx는 왼쪽으로 자식노드를 갖거나, 왼쪽 오른쪽 자식노드를 모두 가진다.
            L, R = 2 * idx + 1, 2 * idx + 2  # 왼쪽 자식노드는 자신의 idx에 2를 곱하고 1을 더함 / 오른쪽 자식노드는 자신의 idx에 2를 곱하고 2를 더함
            if L < n and self.A[L].key < self.A[idx].key:  # 접근한 노드의 값이 왼쪽 자식노드의 값보다 크다면 실행 -> 내려가야함 / <인 이유 ->최소힙을 구현하기 위해서
                m = L
            else:
                m = idx  # 아니라면 그자리 그대로
            if R < n and self.A[m].key > self.A[R].key:  # R번 노드가 n보다 작을 때 즉, 노드가 존재할 때 이번엔 오른쪽 자식 노드와 비교
                m = R  # 키값이 더 크다면 새로 업데이트
            if m != idx:  # 새로 배정받은 위치가 기존의 idx와 다르다면 이동
                self.A[idx], self.A[m] = self.A[m], self.A[idx]
                ##idx번째와 m번째 노드를 바꿔줬기 때문에 A리스트에서 idx와 m에 해당하는 인덱스에 위치한 노드의 index(노드 번호)가 저장된 딕셔너리에서 value값을  swap
                self.keys[self.A[idx].index], self.keys[self.A[m].index] = self.keys[self.A[m].index], self.keys[self.A[idx].index]
                idx = m
            else:  # 자기 자리를 찾았으면 break
                break

    def delete_min(self):  # heapify_down연산으로 인해 수행시간은 O(logn)
        if len(self.A) == 0: return None
        key = self.A[0]  # 제일 위의 노드의 정보를 백업
        self.A[0], self.A[len(self.A) - 1] = self.A[len(self.A) - 1], self.A[0]  # 제일 위의 노드와 마지막 노드를 바꿔준다.
        ##0번째와 A리스트의 마지막 노드를 바꿔줬기 때문에 A리스트에서 m번째와 마지막에 해당하는 인덱스에 위치한 노드의 index(노드 번호)가 저장된 딕셔너리에서 value값을  swap
        self.keys[self.A[0].index], self.keys[self.A[len(self.A) - 1].index] = self.keys[self.A[len(self.A) - 1].index], self.keys[self.A[0].index]
        self.A.pop()  # 기존에 위에 있던 노드가 제일 마지막으로 왔기 때문에 pop
        self.heapify_down(0, len(self.A))  # 새로 올라간 0번 노드에 대해서 heapify_down을 거치면서 힙구조 유지 O(nlogn)
        return key.index  # 맨 위에 있는 노드 몇번 인덱스에 있었는지를 반환

    def decrease_key(self, v,distance):  # index를 얻는 연산은 상수시간 O(1)이고, heapify_up하는 과정은 O(logn)이기 때문에 O(logn)의 수행시간을 갖는다.
        idx = self.keys[v]  # 딕셔너리를 통해서 v노드가 현재 A리스트 어디에 위치해 있는지 정보를 얻는다. 상수시간 O(1)
        self.A[idx].key = distance  # 그 노드에 새로운 distance를 부여한다.
        self.heapify_up(idx)  # 그 노드의 key값이 바뀌었기 때문에 min_heap 구조를 위해 heapify_up을 거친다. O(logn)의 수행시간을 가진다.

				
def Prim():
    n = int(input())  # 노드 개수
    m = int(input())  # 에지 개수
    cost = [math.inf]*n  #아무것도 없는 상태에서 시작
    E = [ None for _ in range(n)] #첫 엣지에 연결된 값이 없기 때문에
    F = [ False for _ in range(n)]
    edges = [[] for _ in range(n)]  # n개의 노드의 인접성을 알기위한 연결리스트
    edges_weight={} #에지들의 가중치를 저장할 딕셔너리 
    for i in range(m):
        u, v, w = map(int,input().split()) # u정점과 v정점과 w가중치를 입력받음
        edges_weight[u,v] = w #양방향으로 연결 
        edges_weight[v,u] = w
        edges[u].append(v)
        edges[v].append(u)
    min_cost = 0 #최소 가중치 
    T=[] #선택한 간선들의 정보가 담길 리스트 
    Q = AdaptedHeap(cost[:]) #적응형 min_heap
    Q.make_heap()
    while len(Q):
        v = Q.delete_min() #cost값을 기준으로 가중치가 가장 작은 노드를 pop
        F[v] = True #방문처리 
        if E[v]!=None: #처음 노드가 F로 이동하려고 할 때는 cut을 할 수 없기 때문에 처음에는 실행이 되지 않는다. 
            T.append((E[v],v))
            min_cost += edges_weight[E[v],v]
        for w in edges[v]: #v와 인접한 노드들에 대해서 
            if (F[w] == False) and (v,w) in edges_weight: #w노드를 방문하지 않았고, 갈 수 있다면
                if (edges_weight[v,w] < cost[w]): #v를 통해 w로 가는 값이 기존에 w로 바로 갈 수 있는 값보다 더 작으면 update
                       cost[w] = edges_weight[v,w] #새로운 cost로 update
                       Q.decrease_key(w,cost[w]) #새로운 key값으로 heap을 재구성 
                       E[w] = v #w노드의 부모를 v로 연결
    return min_cost



Prim_cost = Prim()
print(Prim_cost)

'''
Prim 알고리즘의 수행시간 분석
1. while 루프는 정확히 n번(노드의 수만큼) 반복되므로 delete_min()이 n번 호출이 된다. delete_min()은 O(logn)의 시간복잡도를 갖기 때문에 O(nlogn)의 수행시간을 갖는다.

2. 각 에지는 정확히 한번씩 for 루프에서 고려되므로 최악의 경우에는 모든 에지에 대해서 decrease_key연산이 실행이 된다. decrease_key연산은 O(logn)의 수행시간을 갖는데, 총 m번(에지 개수)만큼 호출이 되기 때문에 O(mlogn)이 된다.

이 둘을 더하면 O((n+m)logn)이 된다.

'''
