print("Enter the number between 1 and 10")
number=int(input())

if number<5:
    print("guess a larger number: ")
    number=int(input())
    if number==5:
        print("You guessed it correct")
    else:
        print("yOu guessed it wrong")
elif number>5:
    print("guess a smaller number")
    number = int(input())
    if number==5:
        print("You guessed it correct")
    else:
        print("yOu guessed it wrong")
else:
    print("You guessed it right at the first guess")
