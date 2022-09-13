from collections import Counter 
from string import digits
import random


#####計算python code猜的跟user設定的數字間的distance(?A?B)
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
    
#####user設定心中數字
def user_int():
    while True:
        a = input()
        if a.isdigit():
            if len(set(a)) == 4:
                return a
            else:
                print("數字輸入錯誤請重新輸入")
        else:
            print("輸入錯誤從新輸入")

#####python code猜數字
def python_guess():
    rdm = ''
    while True:
        tmp = str(random.randint(0,9))
        if tmp not in rdm:       
            rdm += tmp
        if len(rdm) == 4:
            return rdm
   
if __name__ == '__main__':
    
    count = 0
    repeat = set() 
    
    gi = Guess_integer()
    
    u_int = user_int()
    
    #####猜到中為止
    while True:
        A = 0
        B = 0
        
        #1結束while迴圈
        print("輸入exit離開，其餘則繼續")
        exit = input()
        if exit == 'exit':
            break
        
        #####python code不能重複猜
        p_guess = python_guess()        
        if p_guess not in repeat:
            repeat.add(p_guess)
        else:
            p_guess = python_guess()
            
        count += 1
        print("python code猜了第幾次:",count)
        print("python code猜的數字為:",p_guess)
        
        #####計算A,B 
        matrix = Counter([A+1 if i == j else B+2 if i != j else None for i in range(4) for j in range(4) if gi.distance(u_int[j],p_guess[i])])   
        
        #####結果
        result = f'{str(matrix[1])}A{str(matrix[2])}B'
        if result == '4A0B':
            print("python code猜到了")
            break
        else:
            print("python code猜錯了 distance為:", result)
            
        
    