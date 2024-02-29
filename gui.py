from tkinter import *

root = Tk()
root.title("Tic Tac Toe")

def clicked(button):
    button['text'] = 'X'
    
button = Button(root, text=' ', font=('Arial 15 bold'), height=4, width=8, command=lambda: clicked(button))
       
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