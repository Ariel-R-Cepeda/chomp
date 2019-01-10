





class Board:
  def __init__(self,rows,cols):
    self.rows = rows
    self.cols = cols
  def __repr__(self,rows,cols):
    i = 0
    ind = 1
    stuff = ""
    alphabet = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for _ in range(self.rows):
      stuff += alphabet[i] + range(self.cols + 1)[ind] + " "
      if ind == range(self.cols + 1)[-1]:
        print(stuff)
        stuff = ""
        ind = 1
        i += 1
      if i == range(self.rows)[-1]:
        break

      




print("Welcome to...")
print(" .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  ")   
print("| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. | ")  
print("| |     ______   | || |  ____  ____  | || |     ____     | || | ____    ____ | || |   ______     | | ")
print("| |   .' ___  |  | || | |_   ||   _| | || |   .'    `.   | || ||_   \  /   _|| || |  |_   __ \   | | ") 
print("| |  / .'   \_|  | || |   | |__| |   | || |  /  .--.  \  | || |  |   \/   |  | || |    | |__) |  | | ") 
print("| |  | |         | || |   |  __  |   | || |  | |    | |  | || |  | |\  /| |  | || |    |  ___/   | | ") 
print("| |  \ `.___.'\  | || |  _| |  | |_  | || |  \  `--'  /  | || | _| |_\/_| |_ | || |   _| |_      | | ") 
print("| |   `._____.'  | || | |____||____| | || |   `.____.'   | || ||_____||_____|| || |  |_____|     | | ") 
print("| |              | || |              | || |              | || |              | || |              | | ") 
print("| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' | ") 
print(" '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  ")

while True:
  Game_mode = input("PVP[1] ||| vs. Ai[2]")
  

  if Game_mode == "2":
    print("Not implemented yet, get some friends ... loser")
    print(" Lmao")
    exit()
  
  if Game_mode == "1":
    Player1 = input("Player 1, enter your name:")
    Player2 = input("Player 2, enter your name:")
    break

  else :
    print("Woah there my special buddy, pick an actual option.")

print("Board Size:")
while True:
  board_sz_prompt = input("Small[1] ||| Normal[2] ||| Large[3] ||| THICC[4] ||| tall boi[5]")
  if board_sz_prompt == "0" :
    print("You finna die ")
    rows = 1
    cols = 1
    break
  if board_sz_prompt == "1" :
    rows = 2
    cols = 3
    break
  if board_sz_prompt == "2" :
    rows = 4
    cols = 5
    break
  if board_sz_prompt == "3" :
    rows = 6
    cols = 8
    break
  if board_sz_prompt == "4" :
    rows = 26
    cols = 30
    break
  if board_sz_prompt == "5" :
    rows = 26
    cols = 4
    break
  if board_sz_prompt != "0" or "1" or "2" or "3" or "4" or "5" :
    print(" Please choose a valid option")
      
print(Board(rows,cols))
player1_turn = input(f'{Player1}, its your turn! Pick a place to chomp.')
