def next_moves(state, min_bound, max_bound, last_move):
    move = []
    top, bottom = last_move, last_move
    while (1):
        for j in range(top[1], bottom[1] + 1):
            if state[top[0]][j] == ' ':
                if (top[0], j) not in move:
                    move.append((top[0], j))
        for j in range(top[0] + 1, bottom[0] + 1):
            if state[j][top[1]] == ' ':
                if (j, top[1]) not in move:
                    move.append((j, top[1]))
        for j in range(top[0] + 1, bottom[0] + 1):
            if state[j][bottom[1]] == ' ':
                if (j, bottom[1]) not in move:
                    move.append((j, bottom[1]))
        for j in range(top[1] + 1, bottom[1]):
            if state[bottom[0]][j] == ' ':
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

def is_terminated(state, i, j):
    target = state[i][j]
    if target == ' ':
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
            if col == ' ':
                return None

    # Draw
    return 0

def state_point(state, i, j):  
    target = state[i][j]
    
    firstIter, secondIter = (i, j), (i, j)
    handler = 0 # distance between f-s
    
    maxAtt, maxDef = 0, 0
    
    attack, defend= 1, 0
    # Check horizontal
    while (1):
        if firstIter[1] - 1 >= 0 and state[firstIter[0]][firstIter[1] - 1] != ' ':
            if state[firstIter[0]][firstIter[1] - 1] == target:
                attack += 1
            else:
                defend += 1
            firstIter = (firstIter[0], firstIter[1] - 1)
        if secondIter[1] + 1 < len(state) and state[secondIter[0]][secondIter[1] + 1] != ' ':
            if state[secondIter[0]][secondIter[1] + 1] == target:
                attack += 1
            else:
                defend += 1
            secondIter = (secondIter[0], secondIter[1] + 1)
        
        if attack > maxAtt:
            maxAtt = attack
        if defend > maxDef:
            maxDef = defend    
                    
        if handler == firstIter[1] - secondIter[1]:
            break
        handler = firstIter[1] - secondIter[1]
    
    # Check vertical
    attack, defend= 1, 0
    firstIter, secondIter = (i, j), (i, j)
    handler = 0
    
    while (1):
        if firstIter[0] - 1 >= 0 and state[firstIter[0] - 1][firstIter[1]] != ' ':
            if state[firstIter[0] - 1][firstIter[1]] == target:
                attack += 1
            else:
                defend += 1
            firstIter = (firstIter[0] - 1, firstIter[1])
        if secondIter[0] + 1 < len(state) and state[secondIter[0] + 1][secondIter[1]] != ' ':
            if state[secondIter[0] + 1][secondIter[1]] == target:
                attack += 1
            else:
                defend += 1
            secondIter = (secondIter[0] + 1, secondIter[1])
        
        if attack > maxAtt:
            maxAtt = attack
        if defend > maxDef:
            maxDef = defend    
        
        if handler == firstIter[0] - secondIter[0]:
            break
        handler = firstIter[0] - secondIter[0]
       
    # Check diagonal
    # 1st
    attack, defend= 1, 0
    firstIter, secondIter = (i, j), (i, j)
    handler = 0
    
    while (1):
        if firstIter[0] - 1 >= 0 and firstIter[1] - 1 >= 0 and state[firstIter[0] - 1][firstIter[1] - 1] != ' ':
            if state[firstIter[0] - 1][firstIter[1] - 1] == target:
                attack += 1
            else:
                defend += 1
            firstIter = (firstIter[0] - 1, firstIter[1])
            firstIter = (firstIter[0] - 1, firstIter[1] - 1)
        if secondIter[0] + 1 < len(state) and secondIter[1] + 1 < len(state) and state[secondIter[0] + 1][secondIter[1] + 1] != ' ':
            if state[secondIter[0] + 1][secondIter[1] + 1] == target:
                attack += 1
            else:
                defend += 1
            firstIter = (firstIter[0] - 1, firstIter[1])
            secondIter = (secondIter[0] + 1, secondIter[1] + 1)
        
        if attack > maxAtt:
            maxAtt = attack
        if defend > maxDef:
            maxDef = defend    
        
        if handler == firstIter[0] - secondIter[0]:
            break
        handler = firstIter[0] - secondIter[0]
    # 2nd
    attack, defend= 1, 0
    firstIter, secondIter = (i, j), (i, j)
    handler = 0
    
    while (1):
        if firstIter[0] - 1 >= 0 and firstIter[1] + 1 < len(state) and state[firstIter[0] - 1][firstIter[1] + 1] != ' ':
            if state[firstIter[0] - 1][firstIter[1] + 1] == target:
                attack += 1
            else:
                defend += 1
            firstIter = (firstIter[0] - 1, firstIter[1])
            firstIter = (firstIter[0] - 1, firstIter[1] + 1)
        if secondIter[0] + 1 < len(state) and secondIter[1] - 1 >= 0 and state[secondIter[0] + 1][secondIter[1] - 1] != ' ':
            if state[secondIter[0] + 1][secondIter[1] - 1] == target:
                attack += 1
            else:
                defend += 1
            firstIter = (firstIter[0] - 1, firstIter[1])
            secondIter = (secondIter[0] + 1, secondIter[1] - 1)
            
        if attack > maxAtt:
            maxAtt = attack
        if defend > maxDef:
            maxDef = defend    
            
        if handler == firstIter[0] - secondIter[0]:
            break
        handler = firstIter[0] - secondIter[0]
    
    pointDef = 1e6 if maxDef == 4 else 3500 if maxDef == 3 else 0
    pointAtt = maxAtt * 1000
    return pointAtt + pointDef

def value(state, alpha, beta, x, y, min_bound, max_bound, depth):
    if is_terminated(state, x, y) is not None:
        return is_terminated(state, x, y)
    if depth == 0:
        return state_point(state, x, y)
    target = state[x][y]
    if target == 'o':
        return max_val_ab(state, alpha, beta, x, y, min_bound, max_bound, depth)
    return min_val_ab(state, alpha, beta, x, y, min_bound, max_bound, depth)

def min_val_ab(state, alpha, beta, x, y, min_bound, max_bound, depth):
    v = 1e9
    for (i, j) in next_moves(state, min_bound, max_bound, (x, y)):
        state[i][j] = 'o'
        min_bound, max_bound = change_bound(min_bound, max_bound, i, j, len(state))
        v = min(v, value(state, alpha, beta, i, j, min_bound, max_bound, depth - 1))
        state[i][j] = ' '
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v

def max_val_ab(state, alpha, beta, x, y, min_bound, max_bound, depth):
    v = -1e9
    for (i, j) in next_moves(state, min_bound, max_bound, (x, y)):
        state[i][j] = 'x'
        min_bound, max_bound = change_bound(min_bound, max_bound, i, j, len(state))
        v = max(v, value(state, alpha, beta, i, j, min_bound, max_bound, depth - 1))
        state[i][j] = ' '
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v

def change_bound(min_bound, max_bound, i, j, size):
    if i - 1 < min_bound[0]:
        min_bound = (i - 1 if i - 1 >= 0 else i, min_bound[1])
    if i + 1 > max_bound[0]:
        max_bound = (i + 1 if i + 1 < size else i, max_bound[1])
    if j - 1 < min_bound[1]:
        min_bound = (min_bound[0], j - 1 if j - 1 >= 0 else j)
    if j + 1 > max_bound[1]:
        max_bound = (max_bound[0], j + 1 if j + 1 < size else j)
    return min_bound, max_bound

def ai_move(state, min_bound, max_bound, last_move):
    bestMove = None
    bestValue = 1e9 + 10
    for (i, j) in next_moves(state, min_bound, max_bound, last_move):
        state[i][j] = 'o'
        min_bound, max_bound = change_bound(min_bound, max_bound, i, j, len(state))
        v = value(state, -1e9, 1e9, i, j, min_bound, max_bound, depth=2)
        if v < bestValue:
            bestValue = v 
            bestMove = (i, j)
            # print('bestValue: ', bestValue, 'bestMove: ', bestMove)
        state[i][j] = ' '
    return bestMove

def inp():
    n = int(input('Input size of the board: '))
    state = [[' ' for i in range(n)] for j in range(n)]
    min_bound = (n - 1, n - 1)
    max_bound = (0, 0)
    
    m = int(input('Input number of moved cells: '))
    x, y = 0, 0
    for i in range(m):
        x, y = map(int, input('Input position of the cell: ').split())
        state[x][y] = 'x' if i % 2 == 0 else 'o'
        min_bound, max_bound = change_bound(min_bound, max_bound, x, y, n)
    return state, min_bound, max_bound, (x, y)

def main():
    state, min_bound, max_bound, last_move = inp()
    move = ai_move(state, min_bound, max_bound, last_move)
    print(move)

if __name__ == '__main__':
    main()
