import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.computer_score = 0
        self.player_score = 0

    def display_rules(self):
        """Display game rules."""
        print("Game Rules:")
        print("- Rock beats Scissors")
        print("- Scissors beats Paper")
        print("- Paper beats Rock")

    def get_computer_choice(self):
        """Get the computer's random choice."""
        return random.choice(self.choices)

    def determine_winner(self, player_choice, computer_choice):
        """Determine the winner based on game rules."""
        if player_choice == computer_choice:
            return "Tie"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "scissors" and computer_choice == "paper") or \
             (player_choice == "paper" and computer_choice == "rock"):
            return "Player"
        else:
            return "Computer"

    def play_round(self):
        """Play a single round of the game."""
        player_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        while player_choice not in self.choices:
            player_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()

        computer_choice = self.get_computer_choice()
        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = self.determine_winner(player_choice, computer_choice)
        if winner == "Tie":
            print("It's a tie!")
        elif winner == "Player":
            print("You win this round!")
            self.player_score += 1
        else:
            print("Computer wins this round!")
            self.computer_score += 1

    def play_game(self):
        """Play the Rock-Paper-Scissors game."""
        self.display_rules()

        while True:
            self.play_round()
            print(f"\nScore - You: {self.player_score}, Computer: {self.computer_score}")

            play_again = input("\nDo you want to play another round? (yes/no): ").lower()
            while play_again not in ["yes", "no"]:
                play_again = input("Invalid input. Please enter yes or no: ").lower()

            if play_again == "no":
                print("\nExiting the game.")
                break

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()
