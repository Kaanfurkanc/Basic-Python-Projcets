print("Welcome to hangman game ! \n\n")

name = input("Please enter your name : ")
print("Dear ",name,", right to wrong = 5")
wrong = 5
guess = ""
word = "python"

while wrong > 0 :
    guess_letter = input("Enter a letter : ")
    guess += guess_letter
    if guess_letter  not in word:
        wrong -=1
        print("Wrong guess letter ! Remaining right to wrong = ",wrong)
    mistake = 0
    for letter in word :
        if letter in guess:
            print(letter)
        else:
            print("-")
            mistake += 1
    if mistake == 0 :
        print("Congrats ! You win ")
    if wrong == 0:
        print("You lose .")
        break