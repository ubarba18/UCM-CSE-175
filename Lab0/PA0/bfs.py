#
# bfs.py
#
# This file provides a function implementing breadth-first search for a
# route-finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# YOUR NAME - THE DATE
# Uriel Barba - 9/21/2022


from sre_constants import FAILURE
from PA0.route import RoadMap
from route import Node
from route import Frontier


def BFS(problem, repeat_check=False):
    """Perform breadth-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE

    root = Node(problem.start, None, None)

    if root is problem.goal:
        return root

    # initializing the frontier to contain node
    frontier = Frontier()
    frontier.add(root)

    # initializing the reached set
    reached = set()
    reached.add(root)

    # while frontier is not empty
    while frontier is not None:
        # a leaf node removed from frontier
        leaf = frontier.pop()
 
        # if the node contains a goal state
        if leaf is problem.goal:
            return leaf
        
        # for each child of the leaf
        

    return None
