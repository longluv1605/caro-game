stage = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', 'o', ' ', 'o', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', 'o', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', 'x', ' ', 'o', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

def isFinished(currStage, i, j):
    target = currStage[i][j]
    if target == ' ':
        return None
    counter = 1
    firstIter, secondIter = (i, j), (i, j)
    handler = 0 # distance between f-s
    
    # Check horizontal
    while (1):
        if firstIter[1] - 1 >= 0 and currStage[firstIter[0]][firstIter[1] - 1] == target:
            counter += 1
            firstIter = (firstIter[0], firstIter[1] - 1)
        if secondIter[1] + 1 < 15 and currStage[secondIter[0]][secondIter[1] + 1] == target:
            counter += 1
            secondIter = (secondIter[0], secondIter[1] + 1)
        
        if counter == 5:
            return 1 if target == 'x' else -1
        
        if handler == firstIter[1] - secondIter[1]:
            break
        
        handler = firstIter[1] - secondIter[1]
        
    # Check vertical
    counter = 1
    firstIter, secondIter = (i, j), (i, j)
    handler = 0
    
    while (1):
        if firstIter[0] - 1 >= 0 and currStage[firstIter[0] - 1][firstIter[1]] == target:
            counter += 1
            firstIter = (firstIter[0] - 1, firstIter[1])
        if secondIter[0] + 1 < 15 and currStage[secondIter[0] + 1][secondIter[1]] == target:
            counter += 1
            secondIter = (secondIter[0] + 1, secondIter[1])
        
        if counter == 5:
            return 1 if target == 'x' else -1
        
        if handler == firstIter[0] - secondIter[0]:
            break
        
        handler = firstIter[0] - secondIter[0]
        
    # Check diagonal
    
    # 1st
    counter = 1
    firstIter, secondIter = (i, j), (i, j)
    handler = 0
    
    while (1):
        if firstIter[0] - 1 >= 0 and firstIter[1] - 1 >= 0 and currStage[firstIter[0] - 1][firstIter[1] - 1] == target:
            counter += 1
            firstIter = (firstIter[0] - 1, firstIter[1] - 1)
        if secondIter[0] + 1 < 15 and secondIter[1] + 1 < 15 and currStage[secondIter[0] + 1][secondIter[1] + 1] == target:
            counter += 1
            secondIter = (secondIter[0] + 1, secondIter[1] + 1)
        
        if counter == 5:
            return 1 if target == 'x' else -1
        
        if handler == firstIter[0] - secondIter[0]:
            break
        
        handler = firstIter[0] - secondIter[0]
        
    # 2nd
    counter = 1
    firstIter, secondIter = (i, j), (i, j)
    handler = 0
    
    while (1):
        if firstIter[0] - 1 >= 0 and firstIter[1] + 1 < 15 and currStage[firstIter[0] - 1][firstIter[1] + 1] == target:
            counter += 1
            firstIter = (firstIter[0] - 1, firstIter[1] + 1)
        if secondIter[0] + 1 < 15 and secondIter[1] - 1 >= 0 and currStage[secondIter[0] + 1][secondIter[1] - 1] == target:
            counter += 1
            secondIter = (secondIter[0] + 1, secondIter[1] - 1)
        
        if counter == 5:
            return 1 if target == 'x' else -1
        
        if handler == firstIter[0] - secondIter[0]:
            break
        
        handler = firstIter[0] - secondIter[0]
    
    # Check if not finished
    for row in currStage:
        for col in row:
            if col == ' ':
                return None

    # Draw
    return 0

print(stage[8][6])

print(isFinished(stage, 8, 6)) # 1
            
