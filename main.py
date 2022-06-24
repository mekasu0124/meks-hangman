import random 
with open('./words.txt', 'r') as file:
    words = file.read().split("\n")
    answer = random.choice(words)
    tries = len(answer)
    guesses = ""
    while tries >= 0:
        guess = input("Enter Guess\n")
        if guess in answer:
            guesses += guess
            print("Correct!\nCorrect Letters: {}\nNext Guess\n".format(guesses))
        elif guess == answer:
            print("You Won! {}".format(guess))
            break
        else:
            print("Wrong! Next Guess\n")
            tries-= 1
    else:
        print("You Lost. Play Again")