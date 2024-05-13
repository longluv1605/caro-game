import tkinter as tk
from tkinter import messagebox

n = 10
state = [[' ' for i in range(n)] for j in range(n)]
board = [[None for i in range(n)] for j in range(n)]
min_bound = (n - 1, n - 1)
max_bound = (0, 0)
last_move = (n // 2, n // 2)

def next_moves():
    global last_move
    move = []
    top, bottom = last_move, last_move
    while (1):
        for j in range(top[1], bottom[1] + 1):
            if state[top[0]][j] != 'x' and state[top[0]][j] != 'o':
                if (top[0], j) not in move:
                    move.append((top[0], j))
        for j in range(top[0] + 1, bottom[0] + 1):
            if state[j][top[1]] != 'x' and state[j][top[1]] != 'o':
                if (j, top[1]) not in move:
                    move.append((j, top[1]))
        for j in range(top[0] + 1, bottom[0] + 1):
            if state[j][bottom[1]] != 'x' and state[j][bottom[1]] != 'o':
                if (j, bottom[1]) not in move:
                    move.append((j, bottom[1]))
        for j in range(top[1] + 1, bottom[1]):
            if state[bottom[0]][j] != 'x' and state[bottom[0]][j] != 'o':
                if (bottom[0], j) not in move:
                    move.append((bottom[0], j))
        if top[0] == min_bound[0] and top[1] == min_bound[1] and bottom[0] == max_bound[0] and bottom[1] == max_bound[1]:
            # print("_______________________out")
            return move
        itop = top[0] - 1 if top[0] - 1 >= min_bound[0] else top[0]
        jtop = top[1] - 1 if top[1] - 1 >= min_bound[1] else top[1]
        ibottom = bottom[0] + 1 if bottom[0] + 1 <= max_bound[0] else bottom[0]
        jbottom = bottom[1] + 1 if bottom[1] + 1 <= max_bound[1] else bottom[1]
        top = (itop, jtop)
        bottom = (ibottom, jbottom)

def is_terminated(i, j):
    target = state[i][j]
    if target != 'x' and target != 'o':
        return None
    counter = 1
    firstIter, secondIter = (i, j), (i, j)
    handler = 0 # distance between f-s
    
    # Check horizontal
    while (1):
        if firstIter[1] - 1 >= 0 and state[firstIter[0]][firstIter[1] - 1] == target:
            counter += 1
            firstIter = (firstIter[0], firstIter[1] - 1)
        if secondIter[1] + 1 < len(state) and state[secondIter[0]][secondIter[1] + 1] == target:
            counter += 1
            secondIter = (secondIter[0], secondIter[1] + 1)
        
        if counter == 5:
            return 1e9 if target == 'x' else -1e9
        
        if handler == firstIter[1] - secondIter[1]:
            break
        
        handler = firstIter[1] - secondIter[1]
        
    # Check vertical
    counter = 1
    firstIter, secondIter = (i, j), (i, j)
    handler = 0
    
    while (1):
        if firstIter[0] - 1 >= 0 and state[firstIter[0] - 1][firstIter[1]] == target:
            counter += 1
            firstIter = (firstIter[0] - 1, firstIter[1])
        if secondIter[0] + 1 < len(state) and state[secondIter[0] + 1][secondIter[1]] == target:
            counter += 1
            secondIter = (secondIter[0] + 1, secondIter[1])
        
        if counter == 5:
            return 1e9 if target == 'x' else -1e9
        
        if handler == firstIter[0] - secondIter[0]:
            break
        
        handler = firstIter[0] - secondIter[0]
        
    # Check diagonal
    
    # 1st
    counter = 1
    firstIter, secondIter = (i, j), (i, j)
    handler = 0
    
    while (1):
        if firstIter[0] - 1 >= 0 and firstIter[1] - 1 >= 0 and state[firstIter[0] - 1][firstIter[1] - 1] == target:
            counter += 1
            firstIter = (firstIter[0] - 1, firstIter[1] - 1)
        if secondIter[0] + 1 < len(state) and secondIter[1] + 1 < len(state) and state[secondIter[0] + 1][secondIter[1] + 1] == target:
            counter += 1
            secondIter = (secondIter[0] + 1, secondIter[1] + 1)
        
        if counter == 5:
            return 1e9 if target == 'x' else -1e9
        
        if handler == firstIter[0] - secondIter[0]:
            break
        
        handler = firstIter[0] - secondIter[0]
        
    # 2nd
    counter = 1
    firstIter, secondIter = (i, j), (i, j)
    handler = 0
    
    while (1):
        if firstIter[0] - 1 >= 0 and firstIter[1] + 1 < len(state) and state[firstIter[0] - 1][firstIter[1] + 1] == target:
            counter += 1
            firstIter = (firstIter[0] - 1, firstIter[1] + 1)
        if secondIter[0] + 1 < len(state) and secondIter[1] - 1 >= 0 and state[secondIter[0] + 1][secondIter[1] - 1] == target:
            counter += 1
            secondIter = (secondIter[0] + 1, secondIter[1] - 1)
        
        if counter == 5:
            return 1e9 if target == 'x' else -1e9
        
        if handler == firstIter[0] - secondIter[0]:
            break
        
        handler = firstIter[0] - secondIter[0]
    
    # Check if not finished
    for row in state:
        for col in row:
            if col != 'x' and col != 'o':
                return None

    # Draw
    return 0

def attack(i, j):  
    target = state[i][j]
    
    firstIter, secondIter = (i, j), (i, j)
    handler = 0 # distance between f-s
    
    counter = 1
    max = 0
    # Check horizontal
    while (1):
        if firstIter[1] - 1 >= 0 and state[firstIter[0]][firstIter[1] - 1] == target:
            counter += 1
            firstIter = (firstIter[0], firstIter[1] - 1)
        if secondIter[1] + 1 < len(state) and state[secondIter[0]][secondIter[1] + 1] == target:
            counter += 1
            secondIter = (secondIter[0], secondIter[1] + 1)
        
        if counter > max:
            max = counter
            
        if handler == firstIter[1] - secondIter[1]:
            break
        handler = firstIter[1] - secondIter[1]
    
    # Check vertical
    counter = 0
    firstIter, secondIter = (i, j), (i, j)
    handler = 0
    
    while (1):
        if firstIter[0] - 1 >= 0 and state[firstIter[0] - 1][firstIter[1]] == target:
            counter += 1
            firstIter = (firstIter[0] - 1, firstIter[1])
        if secondIter[0] + 1 < len(state) and state[secondIter[0] + 1][secondIter[1]] == target:
            counter += 1
            secondIter = (secondIter[0] + 1, secondIter[1])
        
        if counter > max:
            max = counter
        
        if handler == firstIter[0] - secondIter[0]:
            break
        handler = firstIter[0] - secondIter[0]
       
    # Check diagonal
    # 1st
    counter = 0
    firstIter, secondIter = (i, j), (i, j)
    handler = 0
    
    while (1):
        if firstIter[0] - 1 >= 0 and firstIter[1] - 1 >= 0 and state[firstIter[0] - 1][firstIter[1] - 1] == target:
            counter += 1
            firstIter = (firstIter[0] - 1, firstIter[1] - 1)
        if secondIter[0] + 1 < len(state) and secondIter[1] + 1 < len(state) and state[secondIter[0] + 1][secondIter[1] + 1] == target:
            counter += 1
            secondIter = (secondIter[0] + 1, secondIter[1] + 1)
        
        if counter > max:
            max = counter
        
        if handler == firstIter[0] - secondIter[0]:
            break
        handler = firstIter[0] - secondIter[0]
    # 2nd
    counter = 0
    firstIter, secondIter = (i, j), (i, j)
    handler = 0
    
    while (1):
        if firstIter[0] - 1 >= 0 and firstIter[1] + 1 < len(state) and state[firstIter[0] - 1][firstIter[1] + 1] == target:
            counter += 1
            firstIter = (firstIter[0] - 1, firstIter[1] + 1)
        if secondIter[0] + 1 < len(state) and secondIter[1] - 1 >= 0 and state[secondIter[0] + 1][secondIter[1] - 1] == target:
            counter += 1
            secondIter = (secondIter[0] + 1, secondIter[1] - 1)
            
        if counter > max:
            max = counter    
            
        if handler == firstIter[0] - secondIter[0]:
            break
        handler = firstIter[0] - secondIter[0]
    
    return max * 1000

def defend(i, j):  
    target = state[i][j]
    enemy = 'o' if target == 'x' else 'x'
    
    firstIter, secondIter = (i, j), (i, j)
    handler = 0 # distance between f-s
    
    counter = 0
    max = 0
    # Check horizontal
    while (1):
        if firstIter[1] - 1 >= 0 and state[firstIter[0]][firstIter[1] - 1] == enemy:
            counter += 1
            firstIter = (firstIter[0], firstIter[1] - 1)
        if secondIter[1] + 1 < len(state) and state[secondIter[0]][secondIter[1] + 1] == enemy:
            counter += 1
            secondIter = (secondIter[0], secondIter[1] + 1)
        
        if counter > max:
            max = counter
            
        if handler == firstIter[1] - secondIter[1]:
            break
        handler = firstIter[1] - secondIter[1]
    
    # Check vertical
    counter = 0
    firstIter, secondIter = (i, j), (i, j)
    handler = 0
    
    while (1):
        if firstIter[0] - 1 >= 0 and state[firstIter[0] - 1][firstIter[1]] == enemy:
            counter += 1
            firstIter = (firstIter[0] - 1, firstIter[1])
        if secondIter[0] + 1 < len(state) and state[secondIter[0] + 1][secondIter[1]] == enemy:
            counter += 1
            secondIter = (secondIter[0] + 1, secondIter[1])
        
        if counter > max:
            max = counter
        
        if handler == firstIter[0] - secondIter[0]:
            break
        handler = firstIter[0] - secondIter[0]
       
    # Check diagonal
    # 1st
    counter = 0
    firstIter, secondIter = (i, j), (i, j)
    handler = 0
    
    while (1):
        if firstIter[0] - 1 >= 0 and firstIter[1] - 1 >= 0 and state[firstIter[0] - 1][firstIter[1] - 1] == enemy:
            counter += 1
            firstIter = (firstIter[0] - 1, firstIter[1] - 1)
        if secondIter[0] + 1 < len(state) and secondIter[1] + 1 < len(state) and state[secondIter[0] + 1][secondIter[1] + 1] == enemy:
            counter += 1
            secondIter = (secondIter[0] + 1, secondIter[1] + 1)
        
        if counter > max:
            max = counter
        
        if handler == firstIter[0] - secondIter[0]:
            break
        handler = firstIter[0] - secondIter[0]
    # 2nd
    counter = 0
    firstIter, secondIter = (i, j), (i, j)
    handler = 0
    
    while (1):
        if firstIter[0] - 1 >= 0 and firstIter[1] + 1 < len(state) and state[firstIter[0] - 1][firstIter[1] + 1] == enemy:
            counter += 1
            firstIter = (firstIter[0] - 1, firstIter[1] + 1)
        if secondIter[0] + 1 < len(state) and secondIter[1] - 1 >= 0 and state[secondIter[0] + 1][secondIter[1] - 1] == enemy:
            counter += 1
            secondIter = (secondIter[0] + 1, secondIter[1] - 1)
            
        if counter > max:
            max = counter    
            
        if handler == firstIter[0] - secondIter[0]:
            break
        handler = firstIter[0] - secondIter[0]
    
    if max == 4: 
        return 1e6
    if max == 3:
        return 3500
    return 0

def state_point(i, j):
    target = state[i][j]
    
    point = attack(i, j) + defend(i, j)
    return point if target == 'x' else -point

def min_val_ab(alpha, beta, i, j, depth):
    global last_move
    if is_terminated(i, j) is not None:
        return is_terminated(i, j)
    if depth == 0:
        return state_point(i, j)
    v = 1e9
    for (i, j) in next_moves():
        state[i][j] = 'o'
        last_move = (i, j)
        change_bound(i, j, len(state))
        v = min(v, max_val_ab(alpha, beta, i, j, depth - 1))
        state[i][j] = ' '
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v

def max_val_ab(alpha, beta, i, j, depth):
    global last_move
    if is_terminated(i, j) is not None:
        return is_terminated(i, j)
    if depth == 0:
        return state_point(i, j)
    v = -1e9
    for (i, j) in next_moves():
        state[i][j] = 'x'
        last_move = (i, j)
        change_bound(i, j, len(state))
        v = max(v, min_val_ab(alpha, beta, i, j, depth - 1))
        state[i][j] = ' '
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v

def show_result(i, j):
    if is_terminated(state, i, j) is None:
        return 0
    if is_terminated(state, i, j) == 1e9:
        print('You win!')
    elif is_terminated(state, i, j) == -1e9:
        print('AI win!')
    elif is_terminated(state, i, j) == 0:
        print('Draw!')
    return 1

def change_bound(i, j, size):
    global min_bound, max_bound
    if i - 1 < min_bound[0]:
        min_bound = (i - 1 if i - 1 >= 0 else i, min_bound[1])
    if i + 1 > max_bound[0]:
        max_bound = (i + 1 if i + 1 < size else i, max_bound[1])
    if j - 1 < min_bound[1]:
        min_bound = (min_bound[0], j - 1 if j - 1 >= 0 else j)
    if j + 1 > max_bound[1]:
        max_bound = (max_bound[0], j + 1 if j + 1 < size else j)

def ai_move():
    global last_move
    bestMove = None
    bestValue = 1e9 + 10
    for (i, j) in next_moves():
        state[i][j] = 'o'
        last_move = (i, j)
        change_bound(i, j, len(state))
        v = max_val_ab(-1e9, 1e9, i, j, depth=2)
        if v < bestValue:
            bestValue = v 
            bestMove = (i, j)
            # print('bestValue: ', bestValue, 'bestMove: ', bestMove)
        state[i][j] = ' '
    return bestMove


def clicked(i, j):
    global last_move
    board[i][j].config(text='X', state='disabled')
    board[i][j].config(bg='yellow')
    board[i][j].config(fg='black')
    board[i][j].config(font=('Arial 15 bold'))
    state[i][j] = 'x'
    
    if is_terminated(i, j) is not None:
        messagebox.showinfo('Result', 'You win!' if is_terminated(i, j) == 1e9 else 'AI win!' if is_terminated(i, j) == -1e9 else 'Draw!')
        return
    
    last_move = (i, j)
    change_bound(i, j, len(state))

def move(i, j):
    clicked(i, j)
    move = ai_move()
    
    state[move[0]][move[1]] = 'o'
    change_bound(move[0], move[1], len(state))
    board[move[0]][move[1]].config(text='O', state='disabled')
    board[move[0]][move[1]].config(bg='blue')
    board[move[0]][move[1]].config(fg='yellow')
    board[move[0]][move[1]].config(font=('Arial 15 bold'))
    
    if is_terminated(move[0], move[1]) is not None:
        messagebox.showinfo('Result', 'You win!' if is_terminated(i, j) == 1e9 else 'AI win!' if is_terminated(i, j) == -1e9 else 'Draw!')

########################################################################################

def play():
    root = tk.Tk()
    root.title('Caro')
    
    for i in range(n):
        for j in range(n):
            board[i][j] = tk.Button(root, text='', font=('Arial 15 bold'), command=lambda x1=i, y1=j: move(x1, y1), height=2, width=5)
            board[i][j].grid(row=i, column=j)
    
    root.mainloop()
    
play()