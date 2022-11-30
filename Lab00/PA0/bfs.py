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
#


from route import Node
from route import Frontier


def BFS(problem, repeat_check=False):
    """Perform breadth-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE
    # store frontier in a queue

    root = Node(problem.start)

    if problem.is_goal(root.loc):
        return root

    # initializing the frontier to contain node, false for stack
    frontier = Frontier(root, queue=True)

    # initializing the reached set
    reached = set()

    if repeat_check == True:
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
                child_loc = child.loc
                if child_loc not in reached:
                    reached.add(child_loc)
                    frontier.add(child)
            else:
                frontier.add(child)

    return None
