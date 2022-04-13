from tracemalloc import start
from colorama import Fore
import random
import time
 
game=[['-' ,'-' ,'-' ],
     ['-' ,'-' ,'-' ],
     ['-' ,'-' ,'-' ]]
row_list=[0,1,2]
col_list=[0,1,2]
game_end=False

def show_game_board():
    for row in game:
        for item in row:
            if item == 'X':
                print(Fore.RED + item,end=" ")
            elif item == 'O':
                print(Fore.BLUE + item,end=" ")
            else:
                 print(Fore.WHITE + item,end=" ")
        print(Fore.WHITE)



def check_game():
    global game_end
    
    row1=game[0][0]+game[0][1]+game[0][2]
    row2=game[1][0]+game[1][1]+game[1][2]
    row3=game[2][0]+game[2][1]+game[2][2]
    col1=game[0][0]+game[1][0]+game[2][0]
    col2=game[0][1]+game[1][1]+game[2][1]
    col3=game[0][2]+game[1][2]+game[2][2]
    ghotr1=game[0][0]+game[1][1]+game[2][2]
    ghotr2=game[0][2]+game[1][1]+game[2][0]

    if "XXX" in row1 or "XXX" in row2 or "XXX" in row3 or "XXX" in col1 or "XXX" in col2 or "XXX" in col3 or "XXX" in ghotr1 or "XXX" in ghotr2:
        print("X win")        
        game_end=True               
    elif "OOO" in row1 or "OOO" in row2 or "OOO" in row3 or "OOO" in col1 or "OOO" in col2 or "OOO" in col3 or "OOO" in ghotr1 or "OOO" in ghotr2:
         print("O win")         
         game_end=True
    elif((game[0][0]=="X" or game[0][0]=="O") and(game[0][1]=="X" or game[0][1]=="O")
and (game[0][2]=="X" or game[0][2]=="O" ) and(game[1][0]=="X" or game[1][0]=="O")
and (game[1][1]=="X" or game[1][1]=="O") and (game[1][2]=="X" or game[1][2]=="O")
and (game[2][0]=="X" or game[2][0]=="O") and (game[2][1]=="X" or game[2][1]=="O")
and (game[2][2]=="X" or game[2][2]=="O")  ):
        print("Draw")
        game_end=True
         
        
         
def two_player():
    start_time = time.time()
        
    while(not game_end):
        while(True):
          print("Player1")
          row=int(input("row:"))
          col=int(input("col:"))
          if game[row][col]=="-":
             game[row][col]="X"       
             break
          else:
              print("be careful")

        show_game_board()
        check_game()           
#player2
        if not game_end:
           while(True):
              print("Player2")
              row=int(input("row:"))
              col=int(input("col:"))
              if game[row][col]=="-":
                 game[row][col]="O"
                 break
              else:
                 print("be careful")
           show_game_board()
           check_game()
    print("Time:", round(time.time() - start_time, 2),"sec")
           
    
def one_player():
    start_time = time.time()
    while(not game_end):
        while(True):
          print("Your turn")
          row=int(input("row:"))
          col=int(input("col:"))
          if game[row][col]=="-":
             game[row][col]="X"
             break
          else:
              print("be careful")
                   
        show_game_board()        
        check_game()
        if not game_end:
            
           print("Computer turn")
           while(True):
              row=random.choice(row_list)
              col=random.choice(col_list)
              if game[row][col]=="-":
                 game[row][col]="O"
                 break
              else:
                 row=random.choice(row_list)
                 col=random.choice(col_list)

        show_game_board()
        check_game()
    print("Time:", round(time.time() - start_time, 2),"sec")
        
        
                    
#menu
choice=int(input("1:Tow Player  2:One player: "))
if(choice==1):
    two_player()
elif(choice==2):
    one_player()
else:
    print("something went wrong")
