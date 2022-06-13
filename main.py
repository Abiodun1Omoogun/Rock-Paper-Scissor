# Rock, Paper, Scissors Game
import random
from xml.dom import InvalidAccessErr

# moves for player  vs computer
moves_options = ["R for rock","P for paper","S for scissor"]
# random item from moves 


while True:
   computer = random.choice(moves_options)
   player = input("What moves_option did you choose: " " (or quit the game)").upper( )
       
   if player == "quit the game":
      print("The game has ended.")
      break


   elif player == "R":
       if computer == "P":
          print("You lose!", computer, "beats", player)
       else:
          print("You win!", player, "beats", computer)

   elif player == "P":
       if computer == "S":
          print("You lose!", computer, "beats", player)
       else:
          print("You win!", player, "beats", computer)

   elif player == "S":
       if computer == "R":
          print("You lose!", computer, "beats", player)
       else:
          print("You win!", player, "beats", computer) 
   
   elif player == computer:
      print(" It a tie!")

   else:
      # Invalid moves_options
      print("Invalid input, retry")


# print(random.choice(moves))




