print("Welcome to 2048!")
print("This is an implementation of an AI playing 2048 by group 8.")

#running the game
import logic
import math

# Macros
depth_limit = 2

def AI_move(mat):
    current_board = mat  # the current board
    scores = [] # scores for each node
    moves = [1,2,3,4,5,6,7,8,9,0,1,1,1,1,1,1] # moves for each node

    # write the game playing AI here:
    # 1. Evaluate score for each node
    (scores, moves) = evaluate(mat)

    # 2. choose the best move using mixmax algorithm
    index = int(minmax(0,1,True,scores,depth_limit) or 0)
    best_move = moves[index]

    # best_move = ['W', "A", "S", "D"]        # choose the best move to make

    return best_move




# minmax algorithm
def minmax(curDepth, nodeIndex, IsMax, scores, depth_limit):
    # base : terminal node is reached
    if(curDepth == depth_limit):
        return int(nodeIndex or 0)
    
    # Max turn
    if(IsMax):
        max = minmax(curDepth+1, nodeIndex*4-2, False, scores, depth_limit)
        for i in range(3):
            value = minmax(curDepth+1, nodeIndex*4-i-1, False, scores, depth_limit)
            #if(max < value):
             #   max = value
            
    # Min turn
    else:
        min = minmax(curDepth+1, nodeIndex*4-2, True, scores, depth_limit)
        for i in range(3):
            value = minmax(curDepth+1, nodeIndex*4-i-1, True, scores, depth_limit)
            if(min > value):
                min = value

def evaluate(mat):
    scores = []
    moves = []
    # write the evaluation code here:

    return (scores, moves)