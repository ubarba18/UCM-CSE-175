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


from route import Node
from route import Frontier


def DFS(problem, repeat_check=False):
    """Perform depth-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE
    # store frontier in a stack

    root = Node(problem.start)

    # base case: if start loc is goal loc, done, return node
    if problem.is_goal(root.loc):
        return root

    # initializing the frontier to contain node, false for stack
    frontier = Frontier(root, queue=False)

    # initializing the reached set
    reached = set()
    reached.add(root.loc)

    while not frontier.is_empty():
        # leaf node removed from the frontier
        leaf = frontier.pop()

        # check if leaf loc is goal
        if problem.is_goal(leaf.loc):
            return leaf

        # expand node
        expanded = leaf.expand(problem)
        # for child in node:
        for child in expanded:
            # Discussed the repeat_check with Ethan Reidel
            if repeat_check == True:
                if child not in reached:
                    reached.add(child.loc)
                    frontier.add(child)
            else:
                frontier.add(child)

    return None
