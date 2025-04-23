import logging
from models.game import Game
from models.player import Player

def main():
    logging.info("Initializing the King Hunt Game")
    
    
    print("Welcome to King Hunt Game!\n")
    p1_name = input("Enter Player 1 name: ")
    p2_name = input("Enter Player 2 name: ")
    
    player1 = Player(p1_name)
    player2 = Player(p2_name)

    game = Game(player1, player2)
    
    game.start()
    logging.info("Game session ended")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Starting the King Hunt Game id %u", id(main))
    main()