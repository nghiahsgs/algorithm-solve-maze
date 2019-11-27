import numpy as np
matrix_maze=np.array([
    ['1010', '0100', '1100', '1001'],
    ['0110', '1100', '1001', '0011'],
    ['1010', '1000', '0101', '0011'],
    ['0111', '1110', '1101', '0111']
])
position_start=(3,2)
position_end=(2,2)

#list nay dc de quy, list long list
#1 tuong duong dau ra
#0: tuong duong ngo cut
#list_path=[0,0,0,0]
deep_tree_evaluate = matrix_maze.shape[0]*matrix_maze.shape[1]
deep_tree_evaluate=2
list_path_last_branch_tree=[0,0,0,0]
b = [list_path_last_branch_tree for i in range(4)]
# print(b)

for i_tree in range(deep_tree_evaluate):
    b = [b for i in range(4)]
# print(b)
list_path=b



# current_row = position_start[0]
# current_col=position_start[1]


def ham_solve_maze(direction, deep_tree, current_row, current_col):
    '''
    #direction
    1: up
    2: down
    3: left
    4: right
    '''
    print('current_row', current_row)
    print('current_col', current_col)
    print('list_path', list_path)
    #base case
    if current_row == position_end[0] and current_col == position_end[1]:
        return list_path
    if direction == 1 and matrix_maze[current_row, current_col][0:1]=='1':
        a = list_path[0]
        for deep in range(deep_tree):
            a[0]=0
        return list_path
    if direction == 2 and matrix_maze[current_row, current_col][1:2] == '1':
        a = list_path[1]
        for deep in range(deep_tree):
            a[1] = 0
        return list_path
    if direction == 3 and matrix_maze[current_row, current_col][2:3] == '1':
        a = list_path[2]
        for deep in range(deep_tree):
            a[2]=0
        return list_path
    if direction == 4 and matrix_maze[current_row, current_col][3:4] == '1':
        a = list_path[3]
        for deep in range(deep_tree):
            a[3] = 0
        return list_path

    #normal case => recursion
    deep_tree += 1
    if direction == 1 and matrix_maze[current_row, current_col][0:1] == '0':
        current_row = current_row-1
        current_col = current_col
    if direction == 2 and matrix_maze[current_row, current_col][1:2] == '0':
        current_row = current_row+1
        current_col = current_col
    if direction == 3 and matrix_maze[current_row, current_col][2:3] == '0':
        current_row = current_row
        current_col = current_col-1
    if direction == 4 and matrix_maze[current_row, current_col][3:4] == '0':
        current_row = current_row
        current_col = current_col+1
    ham_solve_maze(1, deep_tree, current_row, current_col)
    ham_solve_maze(2, deep_tree, current_row, current_col)
    ham_solve_maze(3, deep_tree, current_row, current_col)
    ham_solve_maze(4, deep_tree, current_row, current_col)
    deep_tree+=1


#ham_solve_maze(1, deep_tree, current_row, current_col)
#ham_solve_maze(2, deep_tree, current_row, current_col)
#ham_solve_maze(3, deep_tree, current_row, current_col)
#ham_solve_maze(4, deep_tree, current_row, current_col)
