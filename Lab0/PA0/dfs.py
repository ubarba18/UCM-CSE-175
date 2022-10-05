#
# dfs.py
#
# This file provides a function implementing depth-first search for a
# route-finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
# 
# YOUR COMMENTS INCLUDING CITATIONS
#
# YOUR NAME - THE DATE
# 


from sre_constants import FAILURE
from route import Node
from route import Frontier


def DFS(problem, repeat_check=False):
    """Perform depth-first search to solve the given route finding
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
            # expand the node
        for road in problem.roads:
            # add child to the frontier
            child = Node(road, leaf, leaf.road)
            frontier.add(child)

            # add child to reached set if and only if not already in the reached set
            if child not in reached:
                reached.add(child)

        return FAILURE

    return None
