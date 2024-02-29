import copy

def printState(state):
    print('-------------')
    for row in state:
        for col in row:
            print('|', col, end=' ')
        print('|\n-------------\n')

def nextStates(state, choice):
    states = []
    newState = copy.deepcopy(state)
    for row in range(3):
        for col in range(3):
            if newState[row][col] != 'x' and newState[row][col] != 'o':
                newState[row][col] = choice
                states.append(newState)
                newState = copy.deepcopy(state)
    return states

def max_val(currState, playerChoice, aiChoice):
    if terminated(currState, playerChoice, aiChoice) is not None:
        return terminated(currState, playerChoice, aiChoice)
    v = -1e9
    for state in nextStates(currState, playerChoice):
        v = max(v, min_val(state, playerChoice, aiChoice))
    return v
    
def min_val(currState, playerChoice, aiChoice):
    if terminated(currState, playerChoice, aiChoice) is not None:
        return terminated(currState, playerChoice, aiChoice)
    v = 1e9
    for state in nextStates(currState, aiChoice):
        v = min(v, max_val(state, playerChoice, aiChoice))
    return v
    
def terminated(state, playerChoice, aiChoice):
    # Check rows
    for row in state:
        if row[0] == row[1] == row[2]:
            if row[0] == playerChoice:
                return 1
            elif row[0] == aiChoice:
                return -1
    
    # Check columns
    for col in range(3):
        if state[0][col] == state[1][col] == state[2][col]:
            if state[0][col] == playerChoice:
                return 1
            elif state[0][col] == aiChoice:
                return -1
    
    # Check diagonals
    if state[0][0] == state[1][1] == state[2][2]:
        if state[0][0] == playerChoice:
            return 1
        elif state[0][0] == aiChoice:
            return -1
    if state[0][2] == state[1][1] == state[2][0]:
        if state[0][2] == playerChoice:
            return 1
        elif state[0][2] == aiChoice:
            return -1
    
    # Check if the game is a draw
    checker = 1
    for row in state:
        if checker == 0:
            break
        for col in row:
            if col != playerChoice and col != aiChoice:
                checker = 0
                break
    if checker == 1:
        return 0
    
    return None

def aiMove(currState, playerChoice, aiChoice):
    bestMove = None
    bestValue = 10
    for newState in nextStates(currState, aiChoice):
        v = max_val(newState, playerChoice, aiChoice)
        if v < bestValue:
            bestValue = v 
            bestMove = newState
    return bestMove

def chooseRole():
    while 1:
        playerChoice = input('Choose your role (x or o): ')
        if playerChoice == 'x' or playerChoice == 'o':
            break
        print('Invalid choice. Please try again.')
    if playerChoice == 'x':
        aiChoice = 'o'
    else:
        aiChoice = 'x'
    return playerChoice, aiChoice

def play():
    print('Welcome to Tic Tac Toe!\n')
    state = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]
    turn = 'player'
    playerChoice, aiChoice = chooseRole()
    
    while 1:
        if terminated(state, playerChoice, aiChoice) is not None:
            printState(state)
            if terminated(state, playerChoice, aiChoice) == 1:
                print('You win!')
            elif terminated(state, playerChoice, aiChoice) == -1:
                print('You lose!')
            else:
                print('It\'s a draw!')
            break
        if turn == 'player':
            print('Your turn.\n')
            printState(state)
            while 1:
                move = input('Enter your move (1-9): ')
                if not (move.isdigit()) or  not (1 <= int(move) <= 9):
                    print('Invalid move. Please try again.')
                    continue
                move = int(move) - 1
                row = move // 3
                col = move % 3
                if state[row][col] != playerChoice and state[row][col] != aiChoice:
                    state[row][col] = playerChoice
                    printState(state)
                    break
                print('Invalid move. Please try again.')
            turn = 'ai'
        else:
            print('AI\'s turn.\n')
            state = aiMove(state, playerChoice, aiChoice)
            print('AI moved.\n')
            turn = 'player'


# play()