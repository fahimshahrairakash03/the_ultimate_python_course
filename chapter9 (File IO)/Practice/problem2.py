import random

def game():
    print("you are playing the game")
    score = random.randint(1,62)
    with open("highscore.txt","r") as f:
        hiScore = f.read()
        if(hiScore!=""):
            hiScore=int(hiScore)
        else:
            hiScore = 0 
    print(f"Your score: {score}")
    if(score>hiScore):
        with open("highscore.txt","w") as f:
            f.write(str(score))
    

    return score

game()