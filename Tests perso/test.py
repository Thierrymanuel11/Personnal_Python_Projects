import string
from time import *

def bubbleSortAlgo(tab):
    for i in range(len(tab)):
        for j in range(len(tab)-1):
            if(tab[j+1] < tab[j]):
                temp = tab[j+1]
                tab[j+1] = tab[j]
                tab[j] = temp
    return tab


def quickSortAlgo(tab):
    tabBefore = []
    tabAfter = []
    
    for i in range(0, len(tab) // 2, 1):
        tabBefore.append(tab[i])
        
    for i in range(len(tab)//2, len(tab), 1):
        tabAfter.append(tab[i])
        
    midElmt = tab[len(tab) // 2]
    while (midElmt > tab [tab.index(midElmt) - 1]):
        temp = tab [tab.index(midElmt) - 1]
        tab [tab.index(midElmt) - 1] =  tab [tab.index(midElmt) ]
        tab [tab.index(midElmt) ] = temp
    return quickSortAlgo(tabBefore) + [midElmt] + quickSortAlgo(tabAfter)



def add_it_up(n):
    sum = 0
    for i in range(n+1):
        sum+= i
    return sum

def sum_reccursively(n):
    if n == 0:
        return 0
    else:
        return n + sum_reccursively(n-1)

def cipher(txt, num):
    letters = string.ascii_letters
    output = ""
    for char in txt:
        if letters.find(char) + num > 25:
            output += letters[(letters.find(char) + num) % 25 -1 ]
        elif char == " ":
            output += " "
        else:
            output += letters[letters.find(char) + num]
    return output
def funct (*args):
    for i in args:
        print(i)    

def remove_char(txt, num):
    retour = ""
    if num < 0 or len(txt) > num:
        return txt
    else:
        for i in range(2, len(txt), 1):
            retour += txt[i]
    return retour
    
    
    
def same_first_last(tab):
    if len(tab) == 0 or (tab[0 ]== tab[-1]):
        return True
    else:
        return False

def divisable_by_five(tab):
    for i in tab:
        if i%5 == 0:
            print(i)
            
    

def good_printer(n):
    for i in range(n+1):
        print((str(i)+" ") * i)


def palindrome(num):
    temp = str(num)
    temp2 = ""
    for i in range(-1, -len(temp)-1, -1) :
        temp2+= temp[i]
    if temp == temp2 :
        return True
    else:
        print(temp2)
        return False
    
def list_conditions(list1, list2):
    return [int(i) for i in list1 if i%2 == 0] + [int(i) for i in list2 if i %2 != 0]    
 
 
def reversed_digit_print(num):
    temp = str(num)
    temp2 = ""
    for i in range(-1, -(len(temp))-1, -1):
        temp2 += temp[i]+" "
    return temp2

def income_tax(amount):
    if amount <= 10000:
        return 0 
    elif amount > 10000 and amount <=20000:
        return amount - 10000 * 10/100
    else:
        return (amount- 20000) * 20 /100 + 10000 * 10/100


def multiplication_table(n):
    for i in range(1,n+1):
        table = "Multilication table of "+ str(i)+": "
        for j in range(1, 11):
            table += str(i*j)+" "
        print(table)


def decimal_to_n(num, n):
    if n == 16:
        result = ""
        while num !=0 :
            rest = num % n
            if rest == 10:
                result = "A" + result
            elif rest == 11:
                result = "B" + result
            elif rest == 12:
                result = "C" + result
            elif rest == 13:
                result = "D" + result
            elif rest == 14:
                result = "E" + result
            elif rest == 15:
                result = "F" + result
            else:
                result = str(num % n) + result
            num //= n
        return result
    else:
        result = ""
        while num !=0 :
            result = str(num % n) + result
            num //= n
        return result
        
    
def pretty_board_printer(board):    
    print("-"*11)
    to_print = ""
    for i in range(len(board)):
        for j in range(len(board[i])):
            to_print += " " + board[i][j] + " "
        to_print += "\n"
    print(to_print)
    print("-"*11)
    
def tic_tac_toe(board, choice, player):
    if choice >=1 and choice <= 3 and (board[0][choice - 1] == "X" or board[0][choice - 1] == "O"):
        return False
    elif choice >=4 and choice <= 6 and (board[1][choice - 4] == "X" or board[1][choice - 4] == "O"):
        return False
    elif choice >= 7 and choice <= 9 and (board[2][choice - 7] == "X" or board[2][choice - 7] == "O"):
        return False

    if choice >=1 and choice <= 3:
        board[0][choice - 1] = player
        return True
    elif choice >=4 and choice <= 6:
        board[1][choice - 4] = player
        return True
    else:
        board[2][choice - 7] = player
        return True
    
def victory_tic_tac_toe(board):
    if (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X") or (board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O"):
        return True
    elif (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X") or (board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O"):
        return True
    elif (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X") or (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O"):
        return True
    elif (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X") or (board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O"):
        return True
    elif (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X") or (board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O"):
        return True
    elif (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X") or (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O"):
        return True
    elif (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") or (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O"):
        return True
    elif (board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X") or (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O"):
        return True
    else:
        return False

def available_moves(board):
    tab = []
    for i in board:
        for move in i:
            if move != "X" and move !=\
                    "O":
                tab.append(int(move))
    return tab

def draw(board):
    for i in board:
        for move in i:
            if move != "X" and move != "O":
                return False
    return True


def ai_play(board):
    tab = available_moves(board)
    move = max(tab)
    tic_tac_toe(board, move, "O")
    print("The AI played "+str(move))

board = [
        ["1","2","3"],
        ["4","5", "6"],
        ["7", "8", "9"]
        ]
#ai_play(board)

#decimal_to_n(23,10)
          
 
#print(list_conditions([4,2,5,63,5,8], [8,52,1,0,3,6]))

#print(income_tax(45000))

#multiplication_table(10)
#if palindrome(1212):
#    print("Ce nombre est un palindrome")
##else:
#    print("Ce nombre n'est pas un palindrome")




#divisable_by_five(bubbleSortAlgo([1,58,63,21,0,25,9,63,41,2,5,3]))
