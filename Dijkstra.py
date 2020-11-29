import math

def relax(u, v): # 특정노드 u를 거쳐서 가는 것이 이득이면 업데이트 해주는 함수 
    if dist[v] > dist[u] + cost[u, v]:
        dist[v] = dist[u] + cost[u, v]

class AdaptedHeap:
    class Locator:
        def __init__(self,key,j):
            self.key = key #key값. 즉 d[v]값 
            self.index = j #key값에 저장된 index / 노드번호
    def __init__(self,L=[]):
        self.A = L #distance를 받아옴
        for i in range(len(L)):
            self.A[i] = self.Locator(self.A[i],i) #A[i]의 원소(distance값을 받아서 계속 pop할 원소들)는 자신의 key값(d[i])와 노드 번호를 표현하는 index값을 속성으로 가진다.
    def __str__(self):
        return str(self.A)
			
    def __len__(self):
        return len(self.A)
			
    def make_heap(self):#n개의 노드에 대해서 heapify_down을 거쳐 min_heap구조로 만든다. 
        n=len(self.A) 
        for k in range(n-1,-1,-1): #n개의 노드에 대해서 heapify_down을 거쳐 min_heap구조로 만든다. 
            self.heapify_down(k,n)
						
    def heapify_up(self,k): #인덱스 i에 저장된 item을 up
        while k > 0 and self.A[(k - 1) // 2].key > self.A[k].key: #현재 노드와 부모노드의 key값을 비교 
            self.A[k], self.A[(k-1)//2] =  self.A[(k-1)//2],self.A[k] #이동 
            k = (k - 1) // 2  # 부모 노드로 이동
						
    def heapify_down(self,idx,n):
        while 2*idx+1 <n: # idx번째 값에 있는 노드의 왼쪽 자식노드의 인덱스는 2*idx+1이다. idx*2+1<n을 해줌으로써 접근하는 idx가 자식노드를 가진다면 반복문을 실행하고, 리프노드라면 실행하지 않는다.
        # 즉 idx는 왼쪽으로 자식노드를 갖거나, 왼쪽 오른쪽 자식노드를 모두 가진다.
            L,R = 2*idx+1, 2*idx+2 #왼쪽 자식노드는 자신의 idx에 2를 곱하고 1을 더함 / 오른쪽 자식노드는 자신의 idx에 2를 곱하고 2를 더함 
            if L<n and self.A[L].key < self.A[idx].key: #접근한 노드의 값이 왼쪽 자식노드의 값보다 크다면 실행 -> 내려가야함 / <인 이유 ->최소힙을 구현하기 위해서
                m=L
            else:
                m=idx #아니라면 그자리 그대로 
            if R<n and self.A[m].key >self.A[R].key: #R번 노드가 n보다 작을 때 즉, 노드가 존재할 때 이번엔 오른쪽 자식 노드와 비교 
                m=R #키값이 더 크다면 새로 업데이트 
            if m != idx: #새로 배정받은 위치가 기존의 idx와 다르다면 이동
                self.A[idx], self.A[m] =  self.A[m],self.A[idx]
                idx=m
            else: #자기 자리를 찾았으면 break 
                break
								
    def delete_min(self):
        if len(self.A) ==0: return None
        key = self.A[0]# 제일 위의 노드의 정보를 백업
        self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1],self.A[0] #제일 위의 노드와 마지막 노드를 바꿔준다.
        self.A.pop() #기존에 위에 있던 노드가 제일 마지막으로 왔기 때문에 pop
        self.heapify_down(0,len(self.A)) #새로 올라간 0번 노드에 대해서 heapify_down을 거치면서 힙구조 유지
        return key.index #맨 위에 있는 노드 몇번 인덱스에 있었는지를 반환 

    def decrease_key(self,v,distance):
        for i in range(len(self.A)): #A리스트만큼 반복 
            if self.A[i].index==v: #노드의 번호가 새로 업데이트된 v노드와 같으면 
                self.A[i].key = distance  # 새로운 distance로 업데이트
                self.heapify_up(i) #i번째 인덱스의 노드의 key값이 업데이트가 되었으므로 힙구조를 위해 heapfiy_up을 실행 
                break


n = int(input()) #노드 개수
m=int(input()) #에지 개수 
cost = {} #u에서 v로 가는 간선의 가중치가 담길 딕셔너리 
edges = [[] for _ in range(n)] #n개의 노드의 인접성을 알기위한 연결리스트 구조
for i in range(m): #간선의 개수만큼 u,v,w (시작점, 종점, 가중치)를 입력받아서 u에서 v로가는 가중치 w는 cost 딕셔너리에 저장 및 u와 v는 인접하기 때문에 u번 노드가 v에 연결됨
	u,v,w = map(int,input().split())
	cost[u,v] = w
	edges[u].append(v)
	
dist = [math.inf] * n  # 소스부터의 거리
dist[0] = 0  # 소스 0번부터 자기 자신까지의 거리


dist2=dist[:] #dist리스트를 복사해서 힙에서 사용 
h1 = AdaptedHeap(dist2) #h1이라는 적응형 힙을 만들어줌 
h1.make_heap() #h1을 min_heap구조로 만든다. 

while len(h1):
    u=h1.delete_min() #힙의 가장 위의 값 즉 d[v]가 작은 노드의 index(노드 번호)를 반환받는다. 
    for v in edges[u]: #u(노드번호)와 인접한 노드에 대해서 실행 
        if (u,v) in cost: #만약 u에서 v로 갈 수가 있다면 
            if dist[v] > dist[u] + cost[u, v]: #relax과정을 실행
                dist[v] = dist[u] + cost[u, v]
                h1.decrease_key(v,dist[v])#v노드에 대해서 d[v]가 바뀌었으므로 decrease_key연산을 진행

for i in dist: #최종 결과를 출력
	print(i,end=' ')


