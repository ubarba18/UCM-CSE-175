#
# astar.py
#
# This file provides a function implementing A* search for a route finding
# problem. Various search utilities from "route.py" are used in this function,
# including the classes RouteProblem, Node, and Frontier. Also, this function
# uses heuristic function objects defined in the "heuristic.py" file.
#
# YOUR COMMENTS INCLUDING CITATIONS
# Implemented code from solutions for PA#0 given by professor David Noelle
# YOUR NAME - THE DATE
# Uriel Barba - 10/5/2022


from route import Node
from route import Frontier


def a_star_search(problem, h, repeat_check=False):
    """Perform A-Star search to solve the given route finding problem,
    returning a solution node in the search tree, corresponding to the goal
    location, if a solution is found. Only perform repeated state checking if
    the provided boolean argument is true."""

    # PLACE YOUR CODE HERE
    # store frontier in a priority queue, with f(n) cost
    root = Node(problem.start)

    if problem.is_goal(root.loc):
        return root

    frontier = Frontier(root, sort_by='f')

    reached = set()

    if repeat_check == True:
        reached.add(root.loc)

    while not frontier.is_empty():
        leaf = frontier.pop()
        if problem.is_goal(leaf.loc):
            return leaf

        expanded = leaf.expand(problem, h)

        for child in expanded:
            if repeat_check == True:
                child_loc = child.loc
                if child_loc in reached:
                    if child in frontier and frontier.__getitem__(child) > child.path_cost + h(child.loc):
                        frontier.pop()
                        frontier.add(child)
            else:
                frontier.add(child)
                reached.add(child.loc)
    return None
