"""This is based off of Runestone Academy's problem solving wiht
algorithms and data stuctures using python book, but I plan to make modifications
and create it without using their libraries (which are specific to their textbook)"""

def knight_graph(board_size):
    """Turns the board size into a graph, and generates the possible legal
    moves based on a helper function genLegalMoves"""
    pass

def genLegalMoves(x, y, board_size):
    """takes the position of the knight, and generates the possible moves. Needs
    to also check that the planned move is still on the board."""
    pass

def posToNodeId(row, column, board_size):
    """Gives each square a unique name"""
    return (row*board_size) + column

def legal_coordinate(x, board_size):
    """this is a helper function for genLegalMoves that checks the 
    move is actually in the board"""
    pass

def knightTour(n, path, u, limit):
    """This actually finds the path.
    n=current depth in tree
    path=list of previous verticies
    u=next vertex to explore
    limit= number of nodes in path"""
    pass