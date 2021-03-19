#HangMan Game

def hangman(word):
    wrong = 0
    stages = ["",
        "----------         ",
        "|         ",
        "|    |    ",
        "|    O    ",
        "|   /|\   ",
        "|   / \   ",
        "|         ",
        ]
    rletters = list(word)
    board = ["--"] * len(word)
    win = False
    print('Welcome to HangMan')

    while wrong < len(stages) - 1:
        print("\n")
        char = input("Guess a letter")
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong +=1
        
        print(("".join(board)))
        e = wrong+1
        print("\n".join(stages[0:e]))
        if "--" not in board:
            print("You Win!")
            print("".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! It was {}.".format(word))   

hangman("cat")