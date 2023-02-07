import collections
import heapq
from sys import stdin as s

s = open("/Users/sunu/PycharmProjects/TIL/ps/1766_sample.txt", "rt") #절대 경로도 되고, 상대 경로도 된다.

n, m = map(int, s.readline().split()) 

indegree = [0]* (n+1)
graph = collections.defaultdict(list)

for _ in range(m):
	a, b = map(int, s.readline().split())
	graph[a].append(b)
	indegree[b] += 1

heap = []
for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)
        
result = []
while heap:
    now = heapq.heappop(heap)
    result.append(now)

    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(heap, i)

print(*result)