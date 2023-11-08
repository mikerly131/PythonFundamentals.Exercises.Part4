from random import randrange

# Function to get a random number input from a human between 1 & 10
def get_random_number():
     rand_number = input("Give me a number between 1 and 10: ")
     return int(rand_number)

# Function to generate a random number from 1 to 10
def get_random_number2():
     rand_number2 = randrange(1, 11)
     return rand_number2

# Function to check if the numbers match and print out the correct content to the user
def do_randos_match(rnum1, rnum2):
     if (rnum1 == rnum2):
          guess = "That is correct"
     elif (rnum1 < rnum2):
          guess = "Your guess was too low"
     else:
          guess = "Your guess was too high"
     return guess

# Function to determine if the game is over due to a correct guess
def is_game_over(num1, num2):
     if (num1 == num2):
          return True
     else:
          return False     


guessStatus = False
game_number = get_random_number2()

while guessStatus == False:

     player_number = get_random_number()
     result = do_randos_match(player_number, game_number)


#    print(f"Random number generated: {game_number}")
     print(f"Your guess was: {player_number}")
     print(result)
     guessStatus = is_game_over(game_number, player_number)
#    if (player_number == game_number):
#         guessStatus = True;
   
