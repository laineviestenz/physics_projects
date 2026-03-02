"""This is based off of Runestone Academy's problem solving wiht
algorithms and data stuctures using python book, but I plan to make modifications
and create it without using their libraries (which are specific to their textbook)"""

from graph import Graph
def knight_graph(board_size):
    """Turns the board size into a graph, and generates the possible legal
    moves based on a helper function genLegalMoves"""
    kt_graph = Graph()
    for row in range(board_size):
        for column in range(board_size):
            node_id = posToNodeId(row, column, board_size)
            newPositions = genLegalMoves(row, column, board_size)

def genLegalMoves(x, y, board_size):
    """takes the position of the knight, and generates the possible moves. Needs
    to also check that the planned move is still on the board."""
    legal_moves = []
    possible_moves = [(-1,-2),(-1,2),(-2,-1),(-2,1),
                   ( 1,-2),( 1,2),( 2,-1),( 2,1)]
    for i in possible_moves:
        new_x = x + i[0]
        new_y = y + i[1]
        if check_legal(new_x) == True and check_legal(new_y) == True:
           legal_moves.append((new_x, new_y))
    return legal_moves

def posToNodeId(row, column, board_size):
    """Gives each square a unique name"""
    return (row*board_size) + column

def check_legal(number, board_size):
    """this is a helper function for genLegalMoves that checks the 
    move is actually in the board"""
    if number >= 0 and number <= (board_size-1): #off by 1 indexing
        return True
    else:
        return False

def knightTour(n, path, u, limit):
    """This actually finds the path.
    n=current depth in tree
    path=list of previous verticies
    u=next vertex to explore
    limit= number of nodes in path"""
    pass