import random

WIN_CASES = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
TILES = {
  "a1": 0,
  "a2": 1,
  "a3": 2,
  "b1": 3,
  "b2": 4,
  "b3": 5,
  "c1": 6,
  "c2": 7,
  "c3": 8
}

def get_player_type():
  while True:
    player_type_reply = input("Would you like to be Player One (1) or Player Two (2)?\n").strip()

    if player_type_reply == "1":
      print("You are now Player One.")
      return 1
    if player_type_reply == "2":
      print("You are now Player Two.")
      return 0

    print("Please input a valid option.")

def ask_for_rematch():
  while True:
    rematch_reply = input("Would you like to rematch? (y/n)\n").strip().lower()
   
    if rematch_reply == "y":
      return True
    if rematch_reply == "n":
      return False

    print("Please input a valid option.")

def display_board(board):
  for i in range(0, 9, 3):
    if i != 0:
      print("—————————")
    
    print(board[i], board[i + 1], board[i + 2], sep=" | ")

def players_turn(board):
  while True:
    move = input("Pick a tile to claim! (e.g. a3)\n").strip().lower()

    if move not in TILES.keys():
      print("That is not a valid tile!")
      continue
      
    if board[TILES[move]] != " ":
      print("That tile is already claimed!")
      continue
      
    board[TILES[move]] = "X"
    break

def ais_turn(board):
  ai_move = get_ai_move(board)
        
  print(f"The AI chose {ai_move}!")
  
  board[TILES[ai_move]] = "O"

def check_if_win(board, mark):
  claimed_tiles = []
  for index, tile in enumerate(board):
    if tile == mark:
      claimed_tiles.append(index)

  for case in WIN_CASES:
    if not set(case) - set(claimed_tiles):
      return True

  return False

def get_ai_move(board):
  while True:
    ai_move = random.choice(list(TILES.keys()))

    if board[TILES[ai_move]] == " ":
      return ai_move

def main():
  player_score = 0
  ai_score = 0
  
  print("——————————————————")
  print("TIC TAC TOE VS. AI")
  print("——————————————————")
  
  while True:
    board = [" "] * 9
    player_type = get_player_type()

    turns = 0
    while True:
      turns += 1
      
      if turns % 2 == player_type:
        players_turn(board)
      else:
        ais_turn(board)

      display_board(board)

      if check_if_win(board, "X"):
        print("You won the match! (impossible)")
        player_score += 1
        break
        
      if check_if_win(board, "O"):
        print("The AI won the match!")
        ai_score += 1
        break
      
      if " " not in board:
        print("It's a tie, nobody wins!")
        player_score += 0.5
        ai_score += 0.5
        break
      
    print("———————")
    print("RESULTS")
    print("———————")
    print(f"Player: {player_score:g}")
    print(f"AI: {ai_score:g}")
    
    if not ask_for_rematch():
      break
    
    print("———————")
    print("REMATCH")
    print("———————")
      
if __name__ == "__main__":
  main()
