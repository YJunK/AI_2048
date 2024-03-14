print("Welcome to 2048!")
print("This is an implementation of an AI playing 2048 by group 8.")

#running the game
import logic
import math
import random

# Macros
depth_limit = 6

def AI_move(mat):
    current_board = mat  # the current board
    scores = [] # scores for each node
    moves = [] # moves for each node
    inval = []

    # write the game playing AI here:
    # 1. Evaluate score for each node
    scores, moves, inval = Eval(mat)

    # dummy element for node indexing
    scores.insert(0,0)
    moves.insert(0,0)

    # 2. choose the best move using mixmax algorithm
    index = minmax(0,0,True,scores,min(depth_limit,len(scores)),inval,moves)
    best_move = moves[index]

    # for invalid input
    key = ['D','W','A','S']
    for i in range(4):
        if(inval[best_move] == 0):
            return best_move
        best_move = key[i]
    return best_move


# minmax algorithm
def minmax(curDepth, nodeIndex, IsMax, scores, depth_limit, inval,moves):
    # base : terminal node is reached
    if(curDepth == depth_limit):
        return nodeIndex
    
    # Max turn
    if(IsMax):
        max_index = minmax(curDepth+1, nodeIndex*4+4, False, scores, depth_limit,inval,moves)
        max = scores[max_index]
        for i in range(3):
            index = minmax(curDepth+1, nodeIndex*4+i+1, False, scores, depth_limit,inval,moves)
            value = scores[index]
            if(max < value and (inval[moves[index]]==0)):
                max = value
                max_index = index
        return max_index
            
    # Min turn
    else:
        min_index = minmax(curDepth+1, nodeIndex*4+4, True, scores, depth_limit,inval,moves)
        min = scores[min_index]
        for i in range(3):
            index = minmax(curDepth+1, nodeIndex*4+i+1, True, scores, depth_limit,inval,moves)
            value = scores[index]
            if(min > value and (inval[moves[index]]==0)):
                min = value
                min_index = index
        return min_index

def Eval(mat):
    scores = []
    moves = []
    queue = []
    inval = {'W':0, 'S':0, 'A':0, 'D':0}

    up_mat, up_score = logic.move_up(mat)
    down_mat, down_score = logic.move_down(mat)
    left_mat, left_score = logic.move_left(mat)
    right_mat, right_score = logic.move_right(mat)

    if up_mat == mat:
        inval['W'] = 1
    if down_mat == mat:
        inval['S'] = 1
    if left_mat == mat:
        inval['A'] = 1
    if right_mat == mat:
        inval['D'] = 1
    
    queue.append((up_mat,'W', 1))
    queue.append((down_mat, 'S', 1))
    queue.append((left_mat, 'A', 1))
    queue.append((right_mat, 'D', 1))

    while queue:
        cur_mat, dir, cur_dep = queue.pop(0)
        if(cur_dep == depth_limit + 1):
            break
        # if cur_mat not in visited:
        # visited.append(cur_mat)
        scores.append(sum(row.count(0) for row in cur_mat)+ max_tile(cur_mat))
        moves.append(dir)
            
        up_mat, up_score = logic.move_up(cur_mat)
        down_mat, down_score = logic.move_down(cur_mat)
        left_mat, left_score = logic.move_left(cur_mat)
        right_mat, right_score = logic.move_right(cur_mat)

        if up_mat == cur_mat:
            queue.append((up_mat, dir, cur_dep+1))
        else:
            queue.append((up_mat, dir, cur_dep+1))
        
        if down_mat == cur_mat:
            queue.append((down_mat, dir, cur_dep+1))
        else:
            queue.append((down_mat, dir, cur_dep+1))
        
        if left_mat == cur_mat:
            queue.append((left_mat, dir, cur_dep+1))
        else:
            queue.append((left_mat, dir, cur_dep+1))
        
        if right_mat == cur_mat:
            queue.append((right_mat, dir, cur_dep+1))
        else:
            queue.append((right_mat, dir, cur_dep+1))

    return scores, moves, inval
                
def max_tile(mat):
    max_tile = 0 
    for row in mat:
        for element in row:
            if element > max_tile:
                max_tile = element
    return max_tile

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

def maxtileeval(mat):
    scores = []
    moves = []

    max_tile = 0 
    for row in mat:
        for element in row:
            if element > max_tile:
                max_tile = element
    
    scores.append(max_tile)
    moves.append('MAX')
    current_mat = mat.copy()

    return (scores, moves)
