
import tkinter as tk


def TicTacToeGui():
    Button1=tk.Button( text="-",height=5, width=10)
    Button2=tk.Button( text="-",height=5, width=10)
    Button3=tk.Button( text="-",height=5, width=10)
    Button4=tk.Button( text="-",height=5, width=10)
    Button5=tk.Button( text="-",height=5, width=10)
    Button6=tk.Button( text="-",height=5, width=10)
    Button7=tk.Button( text="-",height=5, width=10)
    Button8=tk.Button( text="-",height=5, width=10)
    Button9=tk.Button( text="-",height=5, width=10)

    Button1.grid(column=0,row=0)
    Button2.grid(column=1,row=0)
    Button3.grid(column=2,row=0)
    Button4.grid(column=0,row=1)
    Button5.grid(column=1,row=1)
    Button6.grid(column=2,row=1)
    Button7.grid(column=0,row=2)
    Button8.grid(column=1,row=2)
    Button9.grid(column=2,row=2)

def playing_game():






if __name__ == '__main__':
    window = tk.Tk()
    window.title("Tic Tac Toe")

    TicTacToeGui()



    window.mainloop()



