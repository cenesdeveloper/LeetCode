class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create adjacency list
        adj = defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))

        # Min-heap (priority queue) storing pairs of (distance, node)
        minHeap = [(0, k)]
        dist = [float("inf")] * (n + 1)
        dist[k] = 0
        # Process the queue until all reachable vertices are finalized
        while minHeap:
            time, node = heapq.heappop(minHeap)
            # If this distance not the latest shortest one, skip it
            if time > dist[node]:
                continue

            # Explore all neighbors of the current vertex
            for v, w in adj[node]:
                if dist[node] + w < dist[v]:
                # If we found a shorter path to v through u, update it
                    dist[v] = dist[node] + w
                    heapq.heappush(minHeap, (dist[v], v))


        # Return the final shortest distances from the source
        res = max(dist[1:])
        return res if res != float("inf") else -1