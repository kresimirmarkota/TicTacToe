
import tkinter as tk

window = tk.Tk()
window.title("Tic Tac Toe")



btns=[]

Button1=tk.Button( text="-",height=5, width=10,command=lambda : clicker(1))
Button2=tk.Button( text="-",height=5, width=10,command=lambda : clicker(2))
Button3=tk.Button( text="-",height=5, width=10,command=lambda : clicker(3))
Button4=tk.Button( text="-",height=5, width=10,command=lambda : clicker(4))
Button5=tk.Button( text="-",height=5, width=10,command=lambda : clicker(5))
Button6=tk.Button( text="-",height=5, width=10,command=lambda : clicker(6))
Button7=tk.Button( text="-",height=5, width=10,command=lambda : clicker(7))
Button8=tk.Button( text="-",height=5, width=10,command=lambda : clicker(8))
Button9=tk.Button( text="-",height=5, width=10,command=lambda : clicker(9))

btns.append(Button1)
btns.append(Button2)
btns.append(Button3)
btns.append(Button4)
btns.append(Button5)
btns.append(Button6)
btns.append(Button7)
btns.append(Button8)
btns.append(Button9)

Button1.grid(column=0,row=0)
Button2.grid(column=1,row=0)
Button3.grid(column=2,row=0)
Button4.grid(column=0,row=1)
Button5.grid(column=1,row=1)
Button6.grid(column=2,row=1)
Button7.grid(column=0,row=2)
Button8.grid(column=1,row=2)
Button9.grid(column=2,row=2)



def clicker(number):
    turn = False

    if btns[0]['text'] == '-' and turn == False and number == 1:
        btns[0].config(text="x")
        turn= True

    elif btns[1]['text'] == '-' and turn == False and number == 2 :
        btns[1].config(text="x")
        turn= True
    # print(turn)
    elif btns[2]['text'] == '-' and turn == False and number == 3 :
        btns[2].config(text="x")
        turn= True

    elif btns[3]['text'] == '-' and turn == False and number == 4 :
        btns[3].config(text="x")
        turn= True
    elif btns[4]['text'] == '-' and turn == False and number == 5 :
        btns[4].config(text="x")
        turn= True
    elif btns[5]['text'] == '-' and turn == False and number == 6 :
        btns[5].config(text="x")
        turn= True
    elif btns[6]['text'] == '-' and turn == False and number == 7 :
        btns[6].config(text="x")
        turn= True
    elif btns[7]['text'] == '-' and turn == False and number == 8 :
        btns[7].config(text="x")
        turn= True
    elif btns[8]['text'] == '-' and turn == False and number == 9 :
        btns[8].config(text="x")
        turn= True

    elif btns[0]['text'] == '-' and turn == True and number == 1:
        btns[0].config(text="O")
        turn = False
    elif btns[1]['text'] == '-' and turn == True and number == 2:
        btns[1].config(text="O")
        turn = False
    elif btns[2]['text'] == '-' and turn == True and number == 3:
        btns[2].config(text="O")
        turn = False
    elif btns[3]['text'] == '-' and turn == True and number == 4:
        btns[3].config(text="O")
        turn = False
    elif btns[4]['text'] == '-' and turn == True and number == 5:
        btns[4].config(text="O")
        turn = False
    elif btns[5]['text'] == '-' and turn == True and number == 6:
        btns[5].config(text="O")
        turn = False
    elif btns[6]['text'] == '-' and turn == True and number == 7:
        btns[6].config(text="O")
        turn = False
    elif btns[7]['text'] == '-' and turn == True and number == 8:
        btns[7].config(text="O")
        turn = False
    # if btns[8]['text'] == '-' and turn == True and number == 9:
    elif btns[8]['text'] == '-' and turn == True and number == 9:
        btns[8].config(text="O")
        turn = False
    print(turn)









window.mainloop()



