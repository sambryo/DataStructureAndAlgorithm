class Graph: 
    vertices = {}

    def add_vertext(self, vertext): 
        if isinstance(vertex, Vertext) and vertex.name not in self.vertices: 
            self.vertices[vertex.name] = vertex
            return True
        else: 
            return False

        def add_edge(self, u, v): 
            if u in self.vertices and v in self.vertices: 
                for key, value in self.vertices.items(): 
                    if key == u:
                        value.add_neighbor(v)
                    if key == v: 
                        value.add_neighbor(u)
                return True
            else: 
                return False

        def print_graph(self): 
            for key in sorted(list(self.vertices.keys())): 
                print(key + str(self.vertices[key].neighbors) + " " +str(self.vertices[key].distance))

        def bfs(self, vert): 
            q = list()
            vert.distance = 0
            vert.color = 'red' 
            for v in vert.neighbors:
                self.vertices[v].distance = vert.distance + 1 
                q.append(v)

            while len(q) > 0: 
                u = q.pop(0)
                node_u = self.vertices[u]
                node_u.color = 'red' 

                for v in node_u.neighbors: 
                    node_v = self.vertices[v]
                    if node_v.color = 'black': 
                        q.append(v)
                        if node_v.distance > node_u.distance + 1: 
                            node_v.distance = node_u.distance + 1




            


g = Graph()        
a = Vertext('A')
g.add_vertext(a)
g.add_vertext(Vertext('B'))
for i in range((ord('A'), ord('k'))): 
    g.add_vertext(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges: 
    g.add_edge(edge[:1], edge[1:])
