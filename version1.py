import numpy as np
matrix_maze = np.array([
    ['1011'],
    ['0011'],
    ['0011'],
    ['0111']
]) #1 la tuong, 0 la blank
def invert_one_cell(x):
	y=''
	for i_x in x:
		if i_x=='0':
			y+='1'
		else:
			y+='0'
	return y

position_start = (3, 0)
position_end = (0, 0)

#1 la co loi di
#0 la ngo cut hoac di ngc lai o da di
list_path=[0,0,0,0]

current_row = position_start[0]
current_col=position_start[1]

#destination
end_row = position_end[0]
end_col = position_end[1]


def ham_solve_maze(direction, current_row, current_col):
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
    if direction == 1 and matrix_maze[current_row, current_col][0:1] == '1':
        return list_path
    if direction == 2 and matrix_maze[current_row, current_col][1:2] == '1':
        return list_path
    if direction == 3 and matrix_maze[current_row, current_col][2:3] == '1':
        return list_path
    if direction == 4 and matrix_maze[current_row, current_col][3:4] == '1':
        return list_path

    #normal case => recursion
    if direction == 1 and matrix_maze[current_row, current_col][0:1] == '0':
        current_row = current_row-1
        current_col = current_col

        invert_next_cell=invert_one_cell(matrix_maze[current_row][current_col])
        invert_next_cell[2:3] = 0 # freeze recent entrance

        list_path[0] = list_path[0]+"_" + invert_next_cell
            
    if direction == 2 and matrix_maze[current_row, current_col][1:2] == '0':
        current_row = current_row+1
        current_col = current_col
    if direction == 3 and matrix_maze[current_row, current_col][2:3] == '0':
        current_row = current_row
        current_col = current_col-1
    if direction == 4 and matrix_maze[current_row, current_col][3:4] == '0':
        current_row = current_row
        current_col = current_col+1

    ham_solve_maze(1, current_row, current_col)
    ham_solve_maze(2, current_row, current_col)
    ham_solve_maze(3, current_row, current_col)
    ham_solve_maze(4, current_row, current_col)
    deep_tree += 1


#ham_solve_maze(1, deep_tree, current_row, current_col)
#ham_solve_maze(2, deep_tree, current_row, current_col)
#ham_solve_maze(3, deep_tree, current_row, current_col)
#ham_solve_maze(4, deep_tree, current_row, current_col)
