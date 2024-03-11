from tkinter import *
from tkinter import messagebox
import copy

root = Tk()
root.title("Tic Tac Toe")

state = [['', '', ''], ['', '', ''], ['', '', '']]

def clearGame():
    global state
    state = [['', '', ''], ['', '', ''], ['', '', '']]
    buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]
    for button in buttons:
        button.config(text='', bg='SystemButtonFace')

def clicked(button):
    if button['text'] != '':
        messagebox.showerror('Tic Tac Toe', 'Invalid move!')
    button.config(text='X', bg='red')
    coor = button.grid_info()
    state[coor['row']][coor['column']] = 'X'
    
    if not check_winner(state):
        move = aiMove()
        state[move[0]][move[1]] = 'O'
        buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]
        buttons[move[0]*3 + move[1]].config(text='O', bg='blue')
        check_winner(state)
        
def check_winner(currState):
    if terminated(currState) == None:
        return 0
    if terminated(currState) == 1:
        messagebox.showinfo('Tic Tac Toe', 'You win')
    elif terminated(currState) == -1:
        messagebox.showinfo('Tic Tac Toe', 'You lose')
    elif terminated(currState) == 0:
        messagebox.showinfo('Tic Tac Toe', 'Draw')
    clearGame()
    return 1
   
def min_val(currState):
    if terminated(currState) != None:
        return terminated(currState)
    v = 1e9
    for i in range(3):
        for j in range(3):
            if currState[i][j] == '':
                currState[i][j] = 'O'
                v = min(v, max_val(currState))
                currState[i][j] = ''
    return v

def max_val(currState):
    if terminated(currState) != None:
        return terminated(currState)
    v = -1e9
    for i in range(3):
        for j in range(3):
            if currState[i][j] == '':
                currState[i][j] = 'X'
                v = max(v, min_val(currState))
                currState[i][j] = ''
    return v
 
def aiMove():
    bestMove = None
    bestScore = 100
    nextState = copy.deepcopy(state)
    for i in range(3):
        for j in range(3):
            if state[i][j] == '':
                nextState[i][j] = 'O'
                score = max_val(nextState)
                if score < bestScore:
                    bestScore = score
                    bestMove = (i, j)
                nextState[i][j] = ''
    return bestMove

def terminated(currState):
    for i in range(3):
        if currState[i][0] == currState[i][1] == currState[i][2] != '':
            return 1 if currState[i][0] == 'X' else -1
        if currState[0][i] == currState[1][i] == currState[2][i] != '':
            return 1 if currState[0][i] == 'X' else -1
    if currState[0][0] == currState[1][1] == currState[2][2] != '':
        return 1 if currState[0][0] == 'X' else -1
    if currState[0][2] == currState[1][1] == currState[2][0] != '':
        return 1 if currState[2][0] == 'X' else -1
    for row in currState:
        for col in row:
            if col == '':
                return None
    return 0
       
# Create buttons
button1 = Button(root, text='', font=('Arial 15 bold'), command=lambda: clicked(button1), height=4, width=8)
button2 = Button(root, text='', font=('Arial 15 bold'), command=lambda: clicked(button2), height=4, width=8)
button3 = Button(root, text='', font=('Arial 15 bold'), command=lambda: clicked(button3), height=4, width=8)

button4 = Button(root, text='', font=('Arial 15 bold'), command=lambda: clicked(button4), height=4, width=8)
button5 = Button(root, text='', font=('Arial 15 bold'), command=lambda: clicked(button5), height=4, width=8)
button6 = Button(root, text='', font=('Arial 15 bold'), command=lambda: clicked(button6), height=4, width=8)

button7 = Button(root, text='', font=('Arial 15 bold'), command=lambda: clicked(button7), height=4, width=8)
button8 = Button(root, text='', font=('Arial 15 bold'), command=lambda: clicked(button8), height=4, width=8)
button9 = Button(root, text='', font=('Arial 15 bold'), command=lambda: clicked(button9), height=4, width=8)

# Grid buttons
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)

button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)

button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)




root.mainloop()