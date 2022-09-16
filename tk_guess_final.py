import itertools as it
import random
from collections import Counter
import tkinter as tk
import tkinter.messagebox

###計算兩組數字的distance
class number_group:
    def __init__(self,number):
        self.number = number
        
    def __sub__(self,other):
        matrix = Counter(['A' if i == j else 'B' if i != j else None for i in range(4) for j in range(4) if (int(self.number[j]) == other.number[i])])        
        return distance(f'{str(matrix["A"])}A{str(matrix["B"])}B')

###比較兩個distance是否相等###        
class distance:
    def __init__(self,number):
        self.number = number
        
    def __eq__(self,obj):
        if isinstance(obj,distance):
            return True if self.number == obj.number else False
        return 0

###輸出(猜錯/猜對)的結果###    
def output1(round,p_guess,number_distance):
    output.delete(1.0, 'end-1c')
    output.delete(2.0, 'end-1c')
    output.delete(3.0, 'end-1c')
    output.insert(1.0,"python code猜了第幾次:\n")
    output.insert(1.18,round)  
    output.insert(2.0,"python code猜的數字為:\n")
    output.insert(2.19,p_guess)
    output.insert(3.0,"distance為:")
    output.insert(3.12,number_distance)

###清除重新輸入###
def onclear():
    global token,round
    token = True
    round = 0
    output.delete(1.0, 'end-1c')
    output.delete(2.0, 'end-1c')
    output.delete(3.0, 'end-1c')
    tkinter.messagebox.showinfo(title = 'clear', message = "清除成功")
    
###輸入user心中的數字###
def onOK():
    global token,u_int1,p_guess,possible_list
    if token:        
        if len(set(u_int.get())) == 4 and u_int.get().isdigit() and len(u_int.get()) == 4 :
            tkinter.messagebox.showinfo(title = 'success', message = "輸入成功")
            u_int1 = number_group(str(u_int.get()))
            token = False
            ###python code猜的數字###
            lst = [i for i in range(10)]
            possible_list = list(it.permutations(lst,4))
            p_guess = number_group(possible_list[random.randint(0,len(possible_list)-1)])
        else:
            tkinter.messagebox.showinfo(title = 'error', message = "輸入錯誤從新輸入")  
    else:
        tkinter.messagebox.showinfo(title = 'error', message = "已輸入過")
        
###python code猜下一個數字###
def next():
    global p_guess,round,u_int,u_int1,possible_list   
    if token:
        tkinter.messagebox.showinfo(title = 'error', message = "請先輸入數字") 
    else:
        number_distance = (u_int1 - p_guess)
        if number_distance.number == '4A0B':         
            output1(round+1,p_guess.number,number_distance.number)
            tkinter.messagebox.showinfo(title = 'Congratulation', message = "python code 猜對了")
        else:
            round += 1
            output1(round,p_guess.number,number_distance.number)
            tkinter.messagebox.showinfo(title = 'Unfortunately', message = "python code 猜錯了", )
            possible_list = [i for i in possible_list if (p_guess-number_group(i)) == number_distance]
    p_guess = number_group(possible_list[random.randint(0,len(possible_list)-1)])

if __name__ == '__main__':
    token = True 
    round = 0
    ###tkinter 視窗設置###
    window = tk.Tk()
    window.title('Guess_integer')
    u_int = tk.Entry(window, width = 20)
    u_int.grid(column=3, row=0)
    button = tk.Button(window, text = "Ok", command = onOK)
    button.grid(column=5, row=0)
    button2 = tk.Button(window, text = "Clear", command = onclear)
    button2.grid(column=4, row=0)
    output = tk.Text(window, height = 10, width = 40)
    output.grid(column=3, row=2)
    button1 = tk.Button(window, text = "下一回", command = next)
    button1.grid(column=3, row=3)
    window.mainloop()
    

    

       