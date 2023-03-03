#wap to creat a function that will generate random 3 dice number and if all 3 match, then display "you win" else display "you loss/try again"
import random
def streak():
    dices = ['1','2','3','4','5','6']
    selection = random.choices(dices, k=3)
    if selection[0]== selection[1]== selection[2]:
        return selection,

