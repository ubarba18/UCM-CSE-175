#
# heuristic.py
#
# This Python script file provides two functions in support of minimax search
# using the expected value of game states. First, the file provides the
# function "expected_value_over_delays". This function takes as an argument
# a state of game play in which the current player has just selected an
# action. The function calculates the expected value of the state over all
# possible random results determining the amount of time before the
# Guardian changes gaze direction. This function calculates this value
# regardless of whose turn it is. The value of game states that result from
# different random outcomes is determined by calling "value". Second, the
# file provides a heuristic evaluation function for non-terminal game states.
# The heuristic value returned is between "max_payoff" (best for the
# computer player) and negative one times that value (best for the opponent).
# The heuristic function may be applied to any state of play. It uses
# features of the game state to predict the game payoff without performing
# any look-ahead search.
#
# This content is protected and may not be shared, uploaded, or distributed.
#
# PLACE ANY COMMENTS, INCLUDING ACKNOWLEDGMENTS, HERE
#
# PLACE YOUR NAME AND THE DATE HERE
# Uriel Barba - 11/29/2022


from parameters import *
from minimax import probability_of_time
from minimax import value


def expected_value_over_delays(state, ply):
    """Calculate the expected utility over all possible randomly selected
    Guardian delay times. Return this expected utility value."""
    val = 0.0


    # PLACE YOUR CODE HERE
    # Note that the value of "ply" must be passed along, without
    # modification, to any function calls that calculate the value 
    # of a state.

    for x in range(min_time_steps, max_time_steps+1):
        state.time_remaining = x
        val += (probability_of_time(x)) * value(state, ply)
    return val


def heuristic_value(state):
    """Return an estimate of the expected payoff for the given state of
    game play without performing any look-ahead search. This value must
    be between the maximum payoff value and the additive inverse of the
    maximum payoff."""
    val = 0.0

    # PLACE YOUR CODE HERE
    # if computer location is ahead
    # w_loc = smaller, e_loc = bigger
    # 100 = large gap safe, 50 = decent gap, 1 = tiny gap
    # as gap increases, 
    if abs(state.w_loc) < abs(state.e_loc):
        difference = (abs(state.e_loc) - abs(state.w_loc))
        val = (max_payoff - max_payoff/abs(difference) + 10)

    # if loc are tied
    if abs(state.w_loc) - abs(state.e_loc) == 0:
        val = 0.0

    # if computer location is behind opponent
    # w_loc = bigger, e_loc = smaller
    # -100 = riskier, -1 safer
    # as gap increases, risk increases
    if abs(state.w_loc) > abs(state.e_loc):
        difference = abs(state.w_loc) - abs(state.e_loc)
        val = -(max_payoff - max_payoff/abs(difference) + 10)

    return val
