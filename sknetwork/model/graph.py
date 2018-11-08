import numpy as np


class Graph(object):
    """
	Generic class for graphs.

	Parameters
	----------
	graph_dict : dictionary 
		node -> list of neighbors
		each node is an integer.
	directed :  bool

	Attributes
    ----------
	_directed
	_graph_dict
	n_vertices
	degrees


	Example
	-------
	>>> graph = { 0 : [1,4,5],
          1 : [0,2,4],
          2 : [1,3],
          3 : [2,4],
          4 : [0,1,3],
          5 : [0]
        }
    >>> G = Graph(graph)

	"""

    def __init__(self, graph_dict={}, directed=False):
        self.directed = directed
        self.graph_dict = graph_dict
        self.degrees = {}
        self.n_vertices = None
        self.n_edges = None
        self.basics()

    def clear(self):
        self.directed = None
        self._graph_dict = {}
        self.n_vertices = None
        self.n_edges = None
        self.degrees = {}
        self.basics()

    @property
    def graph_dict(self):
        """
		gets the graph dic and checks consistencies if the graph is directed or undirected.

		"""
        return self._graph_dict

    @graph_dict.setter
    def graph_dict(self, graph_input):
        """

		:type graph_input: dict
		"""
        if not isinstance(graph_input, dict):
            raise ValueError("First argument should be a dictionary")

        if not self.directed:
            Pb = False
            for u in graph_input.keys():
                for v in graph_input[u]:
                    if u not in graph_input[v]:
                        print('Pb for edge', u, v)
                        Pb = True
            if Pb:
                raise ValueError("Missing edges in your undirected graph")
        self._graph_dict = graph_input

    def basics(self):
        """
		computes some basic quantities.
		For directed graphs, degrees are out-degrees.
		"""
        self.n_vertices = len(self.graph_dict.keys())
        self.degrees = {i: len(self.graph_dict[i]) for i in self.graph_dict.keys()}
        self.n_edges = int(np.sum(list(self.degrees.values())))

        if not self.directed:
            self.n_edges = int(self.n_edges / 2)

    def vertices(self):
        return list(self.graph_dict.keys())

    def add_vertex(self, v, verbose=False):
        if v not in self.vertices():
            self._graph_dict[v] = []
            self.degrees[v] = 0
            self.n_vertices += 1
            if verbose:
                print('Added vertex: %d.' % v)
        elif verbose:
            print('no vertex added, vertex %d already present.' % v)

    def add_edge(self, x, y, direct=False, verbose=False):
        """
		add an edge
		"""
        if direct:
            if self.directed:
                raise ValueError("Please add a directed edge, using direct=True")
        elif self.directed:
            raise ValueError("Please add an undirected edge, using direct=False")

        self.add_vertex(x, verbose=verbose)
        self.add_vertex(y, verbose=verbose)
        self._graph_dict[x].append(y)
        self.degrees[x] += 1
        if direct:
            self._graph_dict[y].append(x)
            self.degrees[y] += 1
        self.n_edges += 1