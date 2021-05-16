import random

def main():
    wordBase = ["nate", "shit", "god", "what", "day"]
    playAgain = True
    while playAgain == True:
      print(f"\nThe word base : {wordBase}")
      guessGame(wordBase)
      tryAgain = input("Do u want try again? (Y/N) :")
      if tryAgain == "N":
          playAgain = False
        


def guessGame(wordBase):
  guessInp = ""
  guessCount = 0
  guessLimit = 3
  randNum = random.randint(0, 4)
  guessWord = wordBase[randNum]
  while guessInp != guessWord and guessCount < guessLimit:
    guessInp = input("Enter the guess word: ")
    guessCount += 1
  if guessCount == guessLimit:
    print("Out of Guesses, YOU LOSE")
  else:
    print("You Win!!!! :)")

main()
