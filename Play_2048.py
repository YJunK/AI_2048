print("Welcome to 2048!")
print("This is an implementation of an AI playing 2048 by group 8.")

#running the game
import logic
import math

# Macros
depth_limit = 1

def AI_move(mat):
    current_board = mat  # the current board
    scores = [] # scores for each node
    moves = [] # moves for each node

    # write the game playing AI here:

    # 1. Evaluate score for each node
    (scores, moves) = evaluate(mat)

    # dummy element for node indexing
    scores.insert(0,0)
    moves.insert(0,0)


    # 2. choose the best move using mixmax algorithm
    index = minmax(0,0,True,scores,min(depth_limit,len(scores)))
    best_move = moves[index]

    return best_move


# minmax algorithm
def minmax(curDepth, nodeIndex, IsMax, scores, depth_limit):
    # base : terminal node is reached
    if(curDepth == depth_limit):
        return nodeIndex
    
    # Max turn
    if(IsMax):
        max_index = minmax(curDepth+1, nodeIndex*4+4, False, scores, depth_limit)
        max = scores[max_index]
        for i in range(3):
            index = minmax(curDepth+1, nodeIndex*4+i+1, False, scores, depth_limit)
            value = scores[index]
            if(max < value):
                max = value
                max_index = index
        return max_index
            
    # Min turn
    else:
        min_index = minmax(curDepth+1, nodeIndex*4+4, True, scores, depth_limit)
        min = scores[min_index]
        for i in range(3):
            index = minmax(curDepth+1, nodeIndex*4+i+1, True, scores, depth_limit)
            value = scores[index]
            if(min > value):
                min = value
                min_index = index
        return min_index


def evaluate(mat):
    scores = []
    moves = []

    current_mat = mat.copy()

    # simulate move_up
    up_mat, up_score = logic.move_up(mat)
    up_empty_tiles = sum(row.count(0) for row in up_mat)

    if up_mat != current_mat:
        scores.append(up_empty_tiles)
        moves.append('W')
    else:
        scores.append(0)
        moves.append('W')

    # simulate move_down
    down_mat, down_score = logic.move_down(mat)
    down_empty_tiles = sum(row.count(0) for row in down_mat)

    if down_mat != current_mat:
        scores.append(down_empty_tiles)
        moves.append('S')
    else:
        scores.append(0)
        moves.append('S')

    # simulate move_left
    left_mat, left_score = logic.move_left(mat)
    left_empty_tiles = sum(row.count(0) for row in left_mat)

    if left_mat != current_mat:
        scores.append(left_empty_tiles)
        moves.append('A')
    else:
        scores.append(0)
        moves.append('A')

    # simulate move_right
    right_mat, right_score = logic.move_right(mat)
    right_empty_tiles = sum(row.count(0) for row in right_mat)

    if right_mat != current_mat:
        scores.append(right_empty_tiles)
        moves.append('D')
    else:
        scores.append(0)
        moves.append('D')
    
    return (scores, moves)