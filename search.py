# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    return graphSearch(problem, dfsStrategy)
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    actions = graphSearch(problem, bfsStrategy)
    #print actions
    return actions
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    return graphSearch(problem, ucsStrategy)
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    return graphSearch(problem, aStarStrategy, heuristic)
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

# Graph Search Method
# Returns a list of actions based on strategy
def graphSearch(problem, strategy, heuristic=nullHeuristic):
    closedSet = []
    fringe = util.PriorityQueue()
    item = {'node' : problem.getStartState(), 'actions' : [], 'priority' : 0}
    fringe.push(item, 0)
    while not fringe.isEmpty():
        item = fringe.pop()
        node = item['node']
        if problem.isGoalState(node):
            return item['actions'] # return list of actions
        if node not in closedSet:
            closedSet.append(node)
            listOfSuccessors = problem.getSuccessors(node) #expanding node
            for successor in listOfSuccessors:
                newItem = strategy(item, successor, problem, heuristic)
                fringe.push(newItem, newItem['priority'])
    return []

# strategy for DFS
def dfsStrategy(item, successor, problem, heuristic):
    (nextNode, action, cost) = successor
    currentPriority = item['priority']
    newItem = {'node' : nextNode, 'actions' : item['actions'] + [action], 'priority' : currentPriority - 1}
    return newItem

# strategy for BFS
def bfsStrategy(item, successor, problem, heuristic):
    (nextNode, action, cost) = successor
    currentPriority = item['priority']
    newItem = {'node' : nextNode, 'actions' : item['actions'] + [action], 'priority' : currentPriority + 1}
    return newItem

# strategy for ucs
def ucsStrategy(item, successor, problem, heuristic):
    (nextNode, action, cost) = successor
    newActionsList = item['actions'] + [action]
    newCost = problem.getCostOfActions(newActionsList)
    newItem = {'node' : nextNode, 'actions' : newActionsList, 'priority' : newCost}
    return newItem

# strategy for A*
def aStarStrategy(item, successor, problem, heuristic):
    (nextNode, action, cost) = successor
    newActionsList = item['actions'] + [action]
    newCost = problem.getCostOfActions(newActionsList) + heuristic(nextNode, problem)
    newItem = {'node' : nextNode, 'actions' : newActionsList, 'priority' : newCost}
    return newItem




