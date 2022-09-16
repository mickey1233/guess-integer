import itertools as it
import random
from collections import Counter

class number_group:
    def __init__(self,number):
        self.number = number
        
    def __sub__(self,other):
        matrix = Counter(['A' if i == j else 'B' if i != j else None for i in range(4) for j in range(4) if (int(self.number[j]) == other.number[i])])        
        return distance(f'{str(matrix["A"])}A{str(matrix["B"])}B')
        
class distance:
    def __init__(self,number):
        self.number = number
        
    def __eq__(self,other):
        if isinstance(other,distance):
            return True if self.number == other.number else False
        return 0
    
if __name__ == '__main__':
    round = 0
    lst = [i for i in range(10)]
    possible_list = list(it.permutations(lst,4))
    p_guess = number_group(possible_list[random.randint(0,len(possible_list)-1)])
    
    while True:
        u_int = number_group(input("設定4位不重複的數值"))
        if len(set(u_int.number)) == 4:
            break
        else:
            print('數字重複請重新輸入')
    
    print('user心中的數字是',u_int.number)
    
    while True:
        round+=1
        number_distance = (u_int - p_guess)
        if number_distance.number == "4A0B":
            print('猜對了')
            print('猜了幾輪:',round)
            print('user心中的數字是',u_int.number)
            print('python code猜的數字是',p_guess.number)
            break
        else:
            print('猜錯了 distance為:',number_distance.number)
            print('python code猜的數字是:',p_guess.number)
            possible_list = [i for i in possible_list if (p_guess-number_group(i)) == number_distance]
        p_guess = number_group(possible_list[random.randint(0,len(possible_list)-1)])