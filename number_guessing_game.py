number = 6 # guessing no

while True :
    user = int(input("Guess the no : "))
    if user == number :
        print("Congurats , You won the game ✅! ")
        break
    print("You guessed wrong no , try again ❌")

    
