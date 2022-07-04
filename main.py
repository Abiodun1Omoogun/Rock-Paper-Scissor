# Rock, Paper, Scissors Game
import random

# moves for player  vs computer
moves_options = ["R for rock","P for paper","S for scissor"]
print(moves_options)


while True:
   player = input("What moves_option did you choose? (or QUIT THE GAME)").upper( )
   # print("random.choice(moves_options)")
   computer = random.choice(["R for rock","P for paper","S for scissor"])  
   
   if player == "QUIT THE GAME":
      print("THE GAME HAS ENDED.")
      break 
             
   elif player == "R":
       if computer == "S":
          print("You win!", player, "beats", computer)  
       else:
          computer == "P"
          print("You lose!", computer, "beats", player) 

   elif player == "P":
       if computer == "R":
          print("You win!", player, "beats", computer)
       else:
          computer == "S"
          print("You lose!", computer, "beats", player) 
   
   elif player == "S":
       if computer == "P":
          print("You win!", player, "beats", computer)
       else:
          computer == "R"
          print("You lose!", computer, "beats", player) 
   
   else: 
      player != moves_options
      # Invalid moves_options
      print("Invalid input, retry")
   
   if player == computer:
     print("It's a tie!", player, "Has the same moves_options with", computer)