#========================== Import ==========================
import networkx as nx
import pandas as pd
import statistics
import collections
import timeit


#========================== 1) READING DATA ==========================
def read_names_list(file_path):
	"""
    Funtion to read names file. The ID is the same as the index of row 
    so we are only saving the names ordered.
    Args:
        file_path (str): Source file
    Returns: 
        names_list (list): List of names, index is node ID
    """
	names_list = []
	with open(file_path) as file:
	    for line in file:
	        cline = line.rstrip().split()
	        #row_id = cline[0]
	        row_name = cline[1:]
	        #names_list.append((row_id, " ".join(row_name)))
	        names_list.append(" ".join(row_name))
	return names_list


def read_categories_list(file_path):
	"""
    Funtion to read categories nodes.
    Args:
        file_path (str): Source file
    Returns: 
        categories (dict): Dictionary with categories and nodes in each cat
    """
	categories = {}
	with open(file_path) as file:
	    for line in file:
	        row_cat = line.rstrip().partition(':')[2].partition('; ')[0]
	        row_artic = list(map(int, line.rstrip().partition(':')[2].partition('; ')[2].split()))
	        if len(row_artic) > 3500: # Each category must have more than 3500 nodes
	            categories[row_cat] = row_artic
	return categories


def intersect_categories_reduced(categories, set_nodes):
	"""
    Funtion to intersect categories with the set of reduced nodes.
    Args:
        categories (dictionary): Dictionary with categories and nodes in each cat
        set_nodes (set): List of unique nodes in reduced file
    Returns: 
        categories_reduced (dict): Intersection of each variables and take only nodes
        with more than 3500 results
    """
	categories_reduced = {}
	for key, values in categories.items():
	    aux_list = set_nodes.intersection(values)
	    if(len(aux_list) > 3500): # Each category must have more than 3500 nodes
	        categories_reduced[key] = aux_list   
	return categories_reduced


#========================== RQ2) Block Ranking ==========================
def shortest_path_bfs_list(dic_adj_graph, source, destination_list): 
	"""
    Funtion to compute shortest path using BFS between one source node to many destination nodes.
    Args:
        dic_adj_graph (dictionary): Dictionary with categories and nodes in each cat
        source (int):  Origin node to run bfs
        destination_list (list or set): List of nodes to compute destination path
    Returns: 
        jumps_list (list): List of containing length of shortest path computed
    """
	visited = {source}
	queue = collections.deque([(source, 0)])
	jumps_list = [] # To store the number of jumps of each node in desination_list

	# Repeat until queue is empty
	while queue: 
	    vertex = queue.popleft()
	    # If vertex is destionation return level
	    if vertex[0] in destination_list:
	        jumps_list.append(vertex[1])
	    # Add to visited and append to queue
	    for neighbour in dic_adj_graph[vertex[0]]: 
	        if neighbour not in visited: 
	            visited.add(neighbour) 
	            queue.append((neighbour, vertex[1]+1)) 
	return jumps_list


def shortest_path_bfs_list_list(dic_adj_graph, source_list, destination_list): 
	"""
    Funtion to compute shortest path using BFS between many source nodes to many destination nodes.
    Args:
        dic_adj_graph (dictionary): Dictionary with categories and nodes in each cat
        source_list (list or set):  List of nodes origin
        destination_list (list or set): List of nodes to compute destination path
    Returns: 
        jumps_list (list): List of containing length of shortest path computed
    """
	visited = set()
	queue = collections.deque([])
	for node in source_list:
	    visited.add((node, node))
	    queue.append((node, 0, node))
	jumps_list = [] # To store the number of jumps of each node in desination_list

	# Repeat until queue is empty
	while queue: 
	    vertex = queue.popleft() # 0:node - 1:level - 2:initial_node
	    # If vertex is destionation return level
	    if vertex[0] in destination_list:
	        jumps_list.append(vertex[1])
	    # Add to visited and append to queue
	    for neighbour in dic_adj_graph[vertex[0]]: 
	        if (neighbour, vertex[2]) not in visited: 
	            visited.add((neighbour, vertex[2])) 
	            queue.append((neighbour, vertex[1]+1, vertex[2])) 
	return jumps_list

def distance(dic_adj, categories_reduced, C0, CI, n_nodes):
	"""
	Funtion to compute distance and shortest path using BFS between one source node 
	to many destination nodes.
	Args:
		dic_adj (dictionary): Dict of adjacency list of the dir graph
	    categories_reduced (dictionary): Dictionary with categories and nodes in each cat
	    C0 (str): Source category name
	    C1 (str): Destinantion category name
	    n_nodes (int): Number of nodes of C0 to compute
	Returns: 
	    resturn (int): Median of the shortest path computed between nodes of each category
	"""
	CxCy = []

	C0 = list(categories_reduced.get(C0)) #C0
	CI = set(categories_reduced.get(CI)) #C1

	for s_value in C0[:n_nodes]:
	    CxCy.extend(shortest_path_bfs_list(dic_adj, s_value, CI))

	return statistics.median(CxCy)