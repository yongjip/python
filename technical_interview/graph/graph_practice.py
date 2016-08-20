class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

    def set_node_names(self, names):
        self.node_names = list(names)

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        self._node_map[new_node_val] = new_node
        return new_node

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        "insert a new edge, creating new nodes if necessary"
        nodes = {node_from_val: None, node_to_val: None}
        for node in self.nodes:
            if node.value in nodes:
                nodes[node.value] = node
                if all(nodes.values()):
                    break
        for node_val in nodes:
            nodes[node_val] = nodes[node_val] or self.insert_node(node_val)
        node_from = nodes[node_from_val]
        node_to = nodes[node_to_val]
        new_edge = Edge(new_edge_val, node_from, node_to)
        node_from.edges.append(new_edge)
        node_to.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        out = [(e.value, e.node_from.value, e.node_to.value)
                for e in self.edges]
        return out

    def get_edge_list_names(self):
        '''
        out: (Edge value, from_node_value, to_node_value) all edges
        '''
        out = [(edge.value,
            self.node_names[edge.node_from.value],
            self.node_names[edge.node_to.value])
            for edge in self.edges]
        return out

    def get_adjacency_list(self):
        max_index = self.find_max_index()
        adjacency_list = [[] for _ in range(max_index)]
        for edg in self.edges:
            from_value, to_value = edg.node_from.value, edg.node_to.value
            adjacency_list[from_value].append((to_value, edg.value))
        return [a or None for a in adjacency_list]

    def get_adjacency_list(self):
        max_index = self.find_max_index()
        adjacency_list = [[] for _ in range(max_index)]
        for edg in self.edges:
            from_value, to_value = edg.node_from.value, edg.node_to.value


    def get_adjacency_list_names(self):
        adjacency_list = self.get_adjacency_list()
        def convers_to_names(pair, graph=self):
            node_number, value = pair
            return (graph.node_names[node_number], value)
        def map_conversion(adjacency_list_for_node):
            if adjacency_list_for_node is None:
                return None
            return map(convert_to_names, adjacency_list_for_node)
        return [map_conversion(adjacency_list_for_node)
                for adjacency_list_for_node in adjacency_list]

    def find_max_index(self):
        if len(self.node_names) > 0:
            return len(self.node_names)
        max_index = -1
        if len(self.nodes):
            for node in self.nodes:
                if node.value > max_index:
                    max_index = node.value
        return max_index

    def get_adjacency_matrix(self):
        max_index = max([node.value for node in self.nodes])
        adjacency_matrix = [[0]*max_index for _ in range(max_index)]
        for edge in self.edges:
            edge_value = edge.value
            to_node = edge.node_to
            from_node = edge.node_from
            adjacency_matrix[from_node][to_node] = edge_value
        return adjacency_list

    def find_node(self, node_number):
        return self._node_map.get(node_number)

    def dfs_helper(self, start_node, visited=None):
        ret_list = [start_node.value]
        visited.add(start_node.value)
        edge_out = [e for e in start_node.edges
                    if e.node_to.value != start_node.value]
        for edge in edge_out:
            to_node = edge.node_to
            if to_node.value not in visited:
                ret_list.extend(dfs_helper(to_node, visited))
        return ret_list

    def dfs(self, start_node_num):
        start_node = self.find_node(start_node_num)
        return self.dfs_helper(start_node)

    def bfs(self, start_node_num):
        node = self.find_node(start_node_num)
        ret_list = [node.value]
        queue = [node]
        nodes_out = [e.node_to for e in node.edges
                    if e.node_to.value != node.value]
        queue.extend(nodes_out)
        for node in queue:
            if node.value not in ret_list:
                continue
            ret_list.append(node.value)
            nodes_out = [e.node_to for e in node.edges
                        if e.node_to.value != node.value]
            queue.extentd(nodes_out)
        return ret_list

    def bfs_names(self, start_node_num):
        return [self.node_names[num] for num in self.bfs(start_node_num)]
