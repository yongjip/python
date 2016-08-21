class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes or []
        self.edges = edges or []
        self.node_names = []
        self._node_map = {}

    def set_node_names(self, names):
        self.node_names = list(names)

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        self._node_map[new_node_val] = new_node
        return new_node

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        nodes = {node_from_val: None, node_to_val: None}
        for node in self.nodes:
            if node.value in nodes:
                nodes[node.value] = node
                if all(nodes.values()):
                    break
        for node_val in nodes:
            nodes[node_val] = nodes[node_val] or self.insert_node(node_val)
        from_node = nodes[node_from_val]
        to_node = nodes[node_to_val]
        new_edge = Edge(new_edge_val, from_node, to_node)
        self.edges.append(new_edge)
        from_node.edges.append(new_edge)
        to_node)edges.append(new_edge)

    def get_edge_list(self):
        '''list of (Edge Value, From Node Value, To Node Value)'''
        return [(edge.value, edge.node_from.value, edge.node_to.value)
                for edge in self.edges]

    def get_edge_list_names(self):
        '''edge value, from node name, to node name'''
        return [(edge.value,
            self.node_names[edge.node_from.value],
            self.node_names[edge.node_to.value])
            for edge in self.edges]

    def get_adjacency_list(self):
        '''indixe of outerlist: from_node value
        tuples like (to node value, edge value)'''
        max_index = self.find_max_index()
        adjacency_list = [[] for _ in range(max_index + 1)]
        for edge in self.edges:
            from_node_val, to_node_val = edge.node_from.value, edge.node_to.value
            adjacency_list[from_node_val].append((to_node_val, edge.value))
        return [a or None for a in adjacency_list]

    def get_adjacency_list_name(self):
        '''to node name, edge value'''
        adjacency_list = self.get_adjacency_list()
        def convert_to_name(pair, graph=self):
            node_number, edge_val = pair
            return (graph.node_names[node_number], edge_val)
        def map_conversion(adjacency_list_for_node):
            adjacency_list_for_node is None:
                return None
            return map(conver_to_names, adjacency_list_for_node)
        return [map_conversion(adjacency_list_for_node)
            for adjacency_list_for_node in adjecency_list]

    def get_adjacency_matrix(self):
        max_index = self.find_max_index()
        adjacency_list = [[0] * max_index for _ in range(max_index)]
        for edge in self.edges:
            from_node_val, to_node_val = edge.node_from.value, edge.node_to.value
            adjacency_list[from_node_val][to_node_val] = edge.value
        return adjacency_list
    
    def find_max_index(self):
        return max([node.value for node in self.nodes])

    def find_node(self, node_number):
        return self._node_map.get(node_number)

    def _clear_visited(self):
        for node in self.nodes:
            node.visited = False

    def dfs_helper(self, start_node):
        ret_list = [start_node.value]
        start_node.visited = True
        edges_out = [e for e in start_node.edges
                if e.node_to.value != start_node.value]
        for edge in start_node.edges:
            if not edge.to_node.visited:
                ret_list.extend(self.dfs_helper(edge.to_node))
        return ret_list


    def dfs(self, start_node_num):
        self._clear_visited()
        start_node = self.find_node(start_node_num)
        return self.dfs_helper(start_node)

    def dfs_names(self, start_node_num):
        return [self.node_names[num] for num in self.dfs(start_node_num)]

    def bfs(self, start_node_num):
        node = Node(start_node_num)
        self._clear_visited()
        ret_list = [start_node_num]
        queue = [node]
        def enqueue(node, q=queue):
            node.visited = True
            q.append(node)
        def unvisited_outgoing_edge(node, edge):
            return ((node.value != edge.node_to.value)
                    and (not edge.node_to.visited))
        while queue:
            node = queue.pop(0)
            ret_list.append(node.value)
            for e in node.edges:
                if unvisited_outgoing_edge(node, e):
                    enqueue(e.node_to)
        return ret_list

        
    def bfs_names(self, start_node_num):
            return [self.node_names[num] for num in self.bfs(start_node_num)]

