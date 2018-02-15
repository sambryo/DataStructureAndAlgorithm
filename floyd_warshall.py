INF = 9999
vertext = 5


def floyd_warshall(graph):
    dist = map(lambda i: map(lambda j: j, i), graph)
    for k in range(vertext):
        for i in range(vertext):
            for j in range(vertext):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
