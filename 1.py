from collections import Counter 
from string import digits
import random
import tkinter as tk
import tkinter.messagebox
####git版本2
class Guess_integer:
    def distance(self,u_int,p_guess):
        distance = int(u_int) - int(p_guess)
        return (0==distance) 
    def __eq__(self,obj):
        if isinstance(obj,Guess_integer):
            if self.distance == obj.distance:
                return True
            else:
                return False
        return 0

def python_guess():
    rdm = ''
    while True:
        tmp = str(random.randint(0,9))
        if tmp not in rdm:       
            rdm += tmp
        if len(rdm) == 4:
            return rdm
p_guess = ''    
       
def onOK():
    while True:
        global p_guess
        if p_guess != "":
            tkinter.messagebox.showinfo(title = 'error', message = "已輸入過")
            break
        if len(set(u_int.get())) == 4 and u_int.get().isdigit():
            
            p_guess = python_guess()
            tkinter.messagebox.showinfo(title = 'success', message = "輸入成功")
            break
        else:
            tkinter.messagebox.showinfo(title = 'error', message = "輸入錯誤從新輸入")  
            break
        
gi = Guess_integer()
count = 0
repeat = set()

def next():
    global p_guess,count,repeat,gi
    if p_guess == '':      
        tkinter.messagebox.showinfo(title = 'error', message = "請先輸入數字")  
    else:
        while True:        
            if p_guess not in repeat:
                repeat.add(p_guess)
                break
            else:
                p_guess = python_guess()
        count += 1
        matrix = Counter(['A' if i == j else 'B' if i != j else None for i in range(4) for j in range(4) if gi.distance(u_int.get()[j],p_guess[i])])
        result = f'{str(matrix["A"])}A{str(matrix["B"])}B'
        if result == '4A0B':
            tkinter.messagebox.showinfo(title = 'Congratulation', message = "python code 猜對了")
        else:
            
            output.delete(1.0, 'end-1c')
            output.delete(2.0, 'end-1c')
            output.delete(3.0, 'end-1c')
            output.insert(1.0,"python code猜了第幾次:\n")
            output.insert(1.18,count)  
            output.insert(2.0,"python code猜的數字為:\n")
            output.insert(2.19,p_guess)
            output.insert(3.0,"distance為:")
            output.insert(3.12,result)
            tkinter.messagebox.showinfo(title = 'Unfortunately', message = "python code 猜錯了", )
            
if __name__ == '__main__':       
    window = tk.Tk()
    window.title('Guess_integer')
    u_int = tk.Entry(window, width = 20)
    u_int.pack()
    button = tk.Button(window, text = "OK", command = onOK)
    button.pack()
    output = tk.Text(window, height = 10, width = 40)
    output.pack()
    button1 = tk.Button(window, text = "下一回", command = next)
    button1.pack()
    window.mainloop()
    
    

    