"""
Edward Milman - emilma01@dcs.bbk.ac.uk

A dice rolling game based on numbers generated from the random module. Play against the computer rolling a dice and
adding the results to a total. If a 1 is rolled the total is zero and the turn is lost. Turns can be ended early by
choice. First player to 100 wins.
"""
import random
import os
import time


def main():
    # start variables
    target = 100
    start_score = 0
    playing = True
    turn = 0
    # game loop
    while playing:
        # assigns start variables to 'this game' variables
        player_score = start_score
        computer_score = start_score
        play_turn = turn
        instructions()
        # adjusts variables - test is done after player go so if computer reaches 100 first, player get another turn
        while not is_game_over(computer_score, player_score, target):
            computer_score += computer_move(player_score, computer_score, target)
            player_score += human_move(player_score, computer_score, target)
            play_turn += 1
        # end game summary
        show_results(computer_score, player_score, play_turn)
        # asks to play again
        playing = ask_yes_or_no("Would you like to play again? (Y/N) ")


# welcome screen - prints rules to screen
def instructions():
    print("Welcome to Hundred!\n"
          "In this game you will take turns against the computer to roll a dice.\n"
          "On your turn, you can roll as many times as you wish, however if you roll a one,\n"
          "you score will be zero and you lose your turn!\n"
          "You can end your turn at any point, and your score will be added to your total.\n"
          "The first player to total 100 or more will win.\n"
          "If the player who takes the first turn reaches 100 first,\n"
          "the second player gets another go to try and win.\n"
          "Good luck!")
    os.system("pause")
    os.system("cls")


# param int player_score: current score (player)
# param int computer_score: current score (computer)
# param int target: end score
# calls update_score(). then automatically rolls once for
# player then prompts to roll again, will end turn if 1 rolled. result of roll added to total score.
# returns int total score (0 if a 1 is rolled)
def human_move(player_score, computer_score, target):
    update_score(player_score, computer_score, target)
    print("\nIt's your turn:\n")
    time.sleep(1)
    total = roll()
    print("A {} was rolled.".format(total))
    if total == 1:
        total = 0
    while total != 0 and ask_yes_or_no("Will you roll again? (Y/N) "):
        score = roll()
        print("A {} was rolled.".format(score))
        time.sleep(1)
        total += score
        if score == 1:
            total = 0
    print("You scored {} points.\n".format(total))
    time.sleep(1)
    os.system("cls")
    return total


# param int player_score: current score (player)
# param int computer_score: current score (computer)
# param int target: end score
# automatically rolls once for computer - will end turn as soon as 1 is rolled. calls assess_play() and
# randomise_play() to generate random chance of rolling. adds score of rolls to total score.
# returns int total score (0 if a 1 is rolled)
def computer_move(player_score, computer_score, target):
    update_score(player_score, computer_score, target)
    print("\nIts the computer's turn:")
    total = roll()
    print("A {} was rolled.".format(total))
    time.sleep(1)
    if total == 1:
        total = 0
    while randomise_play(assess_play(player_score, computer_score, total)) and total != 0:
        score = roll()
        print("A {} was rolled.".format(score))
        time.sleep(1)
        total += score
        if score == 1:
            total = 0
    print("The computer scored {} points.\n".format(total))
    time.sleep(2)
    os.system("cls")
    return total


# param int player_score: current score (player)
# param int computer_score: current score (computer)
# param int target: end score
# checks if game has reached end game status (score > 100 and no players tied).
# returns boolean
def is_game_over(computer_score, player_score, target):
    return (computer_score >= target or player_score >= target) and computer_score != player_score


# uses random number generation to return a number 1-6
# returns a random int 1-6
def roll():
    # random.seed(2) # uncomment for testing
    return random.randint(1, 6)


# param str question: string in closed question format
# uses question to ask a yes/no question to user. will only accept upper/lowercase y or n as first char of input
# returns boolean
def ask_yes_or_no(question):
    while True:
        try:
            response = input("{}".format(question))
            if response[0] not in {"y", "Y", "n", "N"}:
                raise ValueError("Expecting char input Y or N")
        except ValueError:
            print("Please input Y for yes or N for no.")
        else:
            return response[0] in {"y", "Y"}


# param int computer_score: current score (computer)
# param int player_score: current score (player)
# param int play_turn: number of turns taken
# returns computer_wins() if computer score is higher or player_wins() if player score is higher
def show_results(computer_score, player_score, play_turn):
    if computer_score > player_score:
        computer_wins(computer_score, player_score, play_turn)
    else:
        player_wins(computer_score, player_score, play_turn)


# param int computer_score: current score (computer)
# param int player_score: current score (player)
# param int play_turn: number of turns taken
# prints winning statement for player
def player_wins(computer_score, player_score, play_turn):
    print("Congratulations - you beat the computer!\n"
          "you won by {} points in {} turns\n"
          "Clearly you are way more cunning than any box of electronics.\n"
          "Hold you head up high as you walk down the street - the glory is yours!\n".format(
        player_score - computer_score, play_turn))


# param int computer_score: current score (computer)
# param int player_score: current score (player)
# param int play_turn: number of turns taken
# prints losing statement for player
def computer_wins(computer_score, player_score, play_turn):
    print("Oh no - the computer won!!\n"
          "You lost by {} points in {} turns.\n"
          "Somehow you were outsmarted by an inanimate object.\n"
          "It's probably best not to mention this to family and friends...\n".format(computer_score - player_score,
                                                                                     play_turn))


# param int player_score: current score (player)
# param int computer_score: current score (computer)
# param int target: end score
# prints status of game variables to screen
def update_score(player_score, computer_score, target):
    print("The scores so far are:")
    print("You have {} points and the computer has {} points.".format(player_score, computer_score))
    difference = abs(computer_score - player_score)
    if player_score > computer_score:
        position = "leading by {} points".format(difference)
    elif player_score == computer_score:
        position = "level on scores"
    else:
        position = "trailing by {} points".format(difference)
    print("You are {}, and need {} more points to win.\n".format(position, target - player_score))


# param int player_score: current score (player)
# param int computer_score: current score (computer)
# param int target: end score
# assess 'risk' for computer based on player score and current turn,
# returns an integer to be used in randomise_play()
def assess_play(player_score, computer_score, total):
    # if player close to winning, computer will play more aggressively
    if player_score >= 80:
        if computer_score + total < player_score - 15:
            risk = 9
        elif computer_score + total < player_score - 10:
            risk = 8
        else:
            risk = 6
    # if computer trails by 10+ points will play more aggressively
    elif player_score - (computer_score + total) > 10:
        risk = 6
    # for 'normal' play has 50% chance of rolling again
    else:
        risk = 5
    return risk


# param int risk: int <=10 returned by assess_play()
# randomly creates a boolean based on int risk
# returns (risk * 10) percent chance of True, False otherwise
def randomise_play(risk):
    return random.randint(1, 10) < risk


if __name__ == "__main__":
    main()
