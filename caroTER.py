import time


def next_moves(state, min_bound, max_bound, last_move):
    move = []
    top, bottom = last_move, last_move
    while 1:
        for j in range(top[1], bottom[1] + 1):
            if state[top[0]][j] == " ":
                if (top[0], j) not in move:
                    move.append((top[0], j))
        for j in range(top[0] + 1, bottom[0] + 1):
            if state[j][top[1]] == " ":
                if (j, top[1]) not in move:
                    move.append((j, top[1]))
        for j in range(top[0] + 1, bottom[0] + 1):
            if state[j][bottom[1]] == " ":
                if (j, bottom[1]) not in move:
                    move.append((j, bottom[1]))
        for j in range(top[1] + 1, bottom[1]):
            if state[bottom[0]][j] == " ":
                if (bottom[0], j) not in move:
                    move.append((bottom[0], j))
        if (
            top[0] == min_bound[0]
            and top[1] == min_bound[1]
            and bottom[0] == max_bound[0]
            and bottom[1] == max_bound[1]
        ):
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
    count = counter(state, i, j, target) + 1

    if count == 5:
        return 1e9 if target == "x" else -1e9
    # Check if not finished
    for row in state:
        for col in row:
            if col == " ":
                return None

    # Draw
    return 0


def counter(state, i, j, target):
    firstIter, secondIter = (i, j), (i, j)
    handler = 0  # distance between f-s

    counter = 0
    max = 0
    # Check horizontal
    while 1:
        if firstIter[1] - 1 >= 0 and state[firstIter[0]][firstIter[1] - 1] == target:
            counter += 1
            firstIter = (firstIter[0], firstIter[1] - 1)
        if (
            secondIter[1] + 1 < len(state)
            and state[secondIter[0]][secondIter[1] + 1] == target
        ):
            counter += 1
            secondIter = (secondIter[0], secondIter[1] + 1)

        if handler == firstIter[1] - secondIter[1]:
            break
        handler = firstIter[1] - secondIter[1]
    if counter > max:
        max = counter

    # Check vertical
    counter = 0
    firstIter, secondIter = (i, j), (i, j)
    handler = 0

    while 1:
        if firstIter[0] - 1 >= 0 and state[firstIter[0] - 1][firstIter[1]] == target:
            counter += 1
            firstIter = (firstIter[0] - 1, firstIter[1])
        if (
            secondIter[0] + 1 < len(state)
            and state[secondIter[0] + 1][secondIter[1]] == target
        ):
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

    while 1:
        if (
            firstIter[0] - 1 >= 0
            and firstIter[1] - 1 >= 0
            and state[firstIter[0] - 1][firstIter[1] - 1] == target
        ):
            counter += 1
            firstIter = (firstIter[0] - 1, firstIter[1] - 1)
        if (
            secondIter[0] + 1 < len(state)
            and secondIter[1] + 1 < len(state)
            and state[secondIter[0] + 1][secondIter[1] + 1] == target
        ):
            counter += 1
            secondIter = (secondIter[0] + 1, secondIter[1] + 1)

        if handler == firstIter[0] - secondIter[0]:
            break
        handler = firstIter[0] - secondIter[0]
    if counter > max:
        max = counter
    # 2nd
    counter = 0
    firstIter, secondIter = (i, j), (i, j)
    handler = 0

    while 1:
        if (
            firstIter[0] - 1 >= 0
            and firstIter[1] + 1 < len(state)
            and state[firstIter[0] - 1][firstIter[1] + 1] == target
        ):
            counter += 1
            firstIter = (firstIter[0] - 1, firstIter[1] + 1)
        if (
            secondIter[0] + 1 < len(state)
            and secondIter[1] - 1 >= 0
            and state[secondIter[0] + 1][secondIter[1] - 1] == target
        ):
            counter += 1
            secondIter = (secondIter[0] + 1, secondIter[1] - 1)

        if handler == firstIter[0] - secondIter[0]:
            break
        handler = firstIter[0] - secondIter[0]
    if counter > max:
        max = counter

    return max


def state_point(state, i, j):
    target = state[i][j]
    attack_point = counter(state, i, j, target) + 1

    enemy = "o" if target == "x" else "x"
    defend_point = counter(state, i, j, enemy)

    attack_point *= 1000 if attack_point > 1 else 0
    defend_point = (
        1e6
        if defend_point == 4
        else 3500 if defend_point == 3 else 2500 if defend_point == 2 else 0
    )

    point = attack_point + defend_point

    return point if target == "x" else -point


def value(state, alpha, beta, x, y, min_bound, max_bound, depth):
    if is_terminated(state, x, y) is not None:
        return is_terminated(state, x, y)
    if depth == 0:
        return state_point(state, x, y)
    target = state[x][y]
    if target == "o":
        return max_val_ab(state, alpha, beta, x, y, min_bound, max_bound, depth)
    return min_val_ab(state, alpha, beta, x, y, min_bound, max_bound, depth)


def min_val_ab(state, alpha, beta, x, y, min_bound, max_bound, depth):
    v = 1e9
    for i, j in next_moves(state, min_bound, max_bound, (x, y)):
        state[i][j] = "o"
        min_bound, max_bound = change_bound(min_bound, max_bound, i, j, len(state))
        v = min(v, value(state, alpha, beta, i, j, min_bound, max_bound, depth - 1))
        state[i][j] = " "
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v


def max_val_ab(state, alpha, beta, x, y, min_bound, max_bound, depth):
    v = -1e9
    for i, j in next_moves(state, min_bound, max_bound, (x, y)):
        state[i][j] = "x"
        min_bound, max_bound = change_bound(min_bound, max_bound, i, j, len(state))
        v = max(v, value(state, alpha, beta, i, j, min_bound, max_bound, depth - 1))
        state[i][j] = " "
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
    for i, j in next_moves(state, min_bound, max_bound, last_move):
        state[i][j] = "o"
        min_bound, max_bound = change_bound(min_bound, max_bound, i, j, len(state))
        v = value(state, -1e9, 1e9, i, j, min_bound, max_bound, depth=3)
        if v < bestValue:
            bestValue = v
            bestMove = (i, j)
            # print('bestValue: ', bestValue, 'bestMove: ', bestMove)
        state[i][j] = " "
    return bestMove


def player_move(state, n):
    while 1:
        move = input("Your move: ")
        if move.isdigit():
            move = int(move)
            if (
                move >= 0
                and move < n * n
                and state[move // n][move % n] != "x"
                and state[move // n][move % n] != "o"
            ):
                return move
        print("Invalid move! Please try again")


def show_result(state, i, j):
    if is_terminated(state, i, j) is None:
        return 0
    if is_terminated(state, i, j) == 1e9:
        print("You win!")
    elif is_terminated(state, i, j) == -1e9:
        print("AI win!")
    elif is_terminated(state, i, j) == 0:
        print("Draw!")
    return 1


def main():
    n = 10
    state = [[" " for i in range(n)] for j in range(n)]

    print_state(state, n)

    min_bound = (n - 1, n - 1)
    max_bound = (0, 0)
    last_move = None
    while 1:
        move = player_move(state, n)
        last_move = (move // n, move % n)
        state[move // n][move % n] = "x"
        min_bound, max_bound = change_bound(
            min_bound, max_bound, move // n, move % n, n
        )
        print("min_bound: ", min_bound, "max_bound: ", max_bound)
        print_state(state, n)
        if show_result(state, move // n, move % n):
            break
        print("AI move: ", end="")
        start = time.time()
        move = ai_move(state, min_bound, max_bound, last_move)
        last_move = move
        end = time.time()
        print(move[0] * n + move[1])
        print("Time: ", end - start)
        state[move[0]][move[1]] = "o"
        min_bound, max_bound = change_bound(min_bound, max_bound, move[0], move[1], n)
        print_state(state, n)
        if show_result(state, move[0], move[1]):
            break


def print_state(state, n):
    print("-------" * n + "-")
    # print('|      ' * n + '|')
    for i in range(n):
        print("|      " * n + "|")
        for j in range(n):
            print(
                "|",
                "{:^5s}".format(str(i * n + j) if state[i][j] == " " else state[i][j]),
                end="",
            )
        print("|\n" + ("-------" * n) + "-")


if __name__ == "__main__":
    main()
