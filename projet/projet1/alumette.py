from random import randint
import random
class Joueur():
    def __init__(self, is_human):
        self.is_human = is_human
        
    def play(self, state):
        if self.is_human == False:
            action = randint(1, 3)
        else:
            action = int(input("$>"))
        return action

class StickGame():

    def __init__(self):
        self.nb = 12

    def display(self):
        print ("| " * self.nb)

    def tour(self, action):
        self.nb -= action



    def gameOver(self):
        if self.nb <= 0:
            return True
        return False

    def reset(self):
        self.nb = 12
        return self.nb

def partie(game, p1, p2):
    state = game.reset()
    players = [p1, p2]
    random.shuffle(players)

    p = 0

    while game.gameOver() == False:

        if players[p%2].is_human:
            game.display()

        action = players[p%2].play(state)
        game.tour(action)

        if game.gameOver() == True :
            if players[p%2].is_human:
                print("vous avez perdu ")
            else : 
                print("vous avez gagner")

        state = game.nb
        p += 1

game = StickGame()

human = Joueur(is_human=True)
random_player = Joueur(is_human=False)

ocontinuer = 1
while ocontinuer:
    partie(game, random_player, human)
    ocontinuer = int(input("1 : continuer , 0 : stop  --> "))