import random
loo = "Y"
def easy(direction):
  global loo
  if direction == "easy":
      direction = "done"
      for i in range(0,10):
          chance = 10 - i
          print(f"You have {chance} chances left.")
          result = int(input("Guess: "))
          if result == ans:
            print("You win")
            a = input("Do you want to play again: 'Y' or 'N'.")
            loo = a
            break
          elif i == 9 and result != ans:
            print("You lose.")
            b = input("Do you want to play again: 'Y' or 'N'.")
            loo = b
            break
          elif result > ans:
              print("Too high")
          elif result < ans:
              print("Too low")

def hard(direction):
  global loo
  if direction == "hard":
      direction = "done"
      for i in range(0,5):
          chance = 5 - i
          print(f"You have {chance} chances left.")
          result = int(input("Guess: "))   
          if result == ans:
              print("You win")
              a = input("Do you want to play again: 'Y' or 'N'.")
              loo = a
              break
          elif i == 4 and result != ans:
            print("You lose.")
            a = input("Do you want to play again: 'Y' or 'N'.")
            loo = a
          elif result > ans:
              print("Too high")
          elif result < ans:
              print("Too low")


while loo == "Y":
  print("Welcome to number guessing game")
  ans = random.randrange(1,101)
  direction = input("Do you want the game to be in 'easy' mode or the 'hard' mode: ")
  if direction == "easy":
    easy(direction)
  elif direction == "hard":
    hard(direction)

if loo == "N":
  print("Thank you for playing.")