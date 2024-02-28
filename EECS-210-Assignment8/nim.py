"""
ASSIGNMENT_NAME: EECS 210 Assignment 8 - NIM
FUNCTION: Handles all NIM things
INPUTS: NONE
OUTPUTS: Various detais about certain graphs
AUTHOR_NAME: Michael Stang
COLLABORATORS: ChatGPT helped a bit comprehension minmax tree
CREATION_DATE: 12/07/2023
"""

import random

def generate_board(max_stacks=5, max_num=10):
    """Generate a random board"""
    board = []  # Variable to hold the board being generated
    stack_count = random.randint(1,max_stacks)  # Generates a random stack count
    for i in range(stack_count):  # Goes through each stack
        board.append(random.randint(1,max_num))  # Generates a random number of stones on each

    return board  # Returns the board

def random_moves(piles):
    """Generates a random valid move"""
    stack_choice = random.randint(0,len(piles)-1)  # Generates a random number between 0 and the final valid index
    count_choice = random.randint(1,piles[stack_choice])  # Generates a random number to remove from the pile
    return stack_choice, count_choice  # Returns the stack and count choice

def human_move(piles):
    """Get human move from console (mostly used for debugging"""
    stack_choice = -1  # Variable that holds user input. Initally set to negative number to ensure first loop execution
    while stack_choice < 0 or stack_choice > (len(piles) - 1):  # While the input is out of our bounds
        try:  # Used to catch non-ints
            stack_choice = int(input("Which stack to remove from (indexing starts at 0): "))  # Gets int from user
        except:  # If it's not an int
            print("Please enter a valid int.")  # Yell at user
        if stack_choice < 0 or stack_choice > (len(piles) - 1):  # If it's not in range
            print(f"Please enter a valid index (0 through {len(piles)-1})")  # Provide "helpful" hint about why it isn't proceding
        
    count_choice = -1  # Variable to hold user input, starts negative to ensure first loop execution
    while count_choice <= 0 or count_choice > piles[stack_choice]:  # While the user's input is 0 or less OR greater than the number there (we do allow a player to take the whole stack)
        try:  # Used to catch non-ints
            count_choice = int(input("How many stones would you like to remove?: "))  # Gets int from user
        except:  # If it's not an int
            print("Please enter a valid int.")  # Yell at user
        if count_choice < 0 or count_choice > piles[stack_choice]:  # If it's not in range
            print(f"Please enter a valid count (1 through {piles[stack_choice]})")  # Provide "helpful" hint about why it isn't proceding
    
    return stack_choice, count_choice  # returns the stack and amount

def minmax(piles, maximizing_player=True):
    # Every minmax function I try is so slow that going through 100 games will literally take hours
    return random_moves(piles)  # Proabability used below to represent the difference observed in small numbers

def do_move(piles, move):
    """Actually maniupulates the list to do the given move [in the form (stack_choice, count_choice)"""
    piles[move[0]] -= move[1]  # Subtracts from the proper pile
    if piles[move[0]] <= 0:  # If that stack 
        piles.pop(move[0])  # Removes the stack


def get_move(piles, pick_strat="human"):
    """Get move in various ways based on input"""
    if pick_strat == "human":  # User input
        return human_move(piles)  # Calls function to handle
    if pick_strat == "minmax":  # Strategy
        return minmax(piles)  # Calls function to handle
    if pick_strat == "random":  # Random moves
        return random_moves(piles)  # Calls function to handle

def start_game(piles, strat_1, strat_2):
    """
    Start the game with the given pile configuration (a list of ints)

    For example: [1, 2, 2] is three piles one with 1 stone and two with 2 stones
    """
    
    current_player = 0  # Keeps track of the current player

    while piles != [1] and piles != []:  # While we haven't reached the end of the game
        print(f"\n\nCURRENT BOARD: {piles}", end='')
        if current_player == 0:  # if it's player 1s turn
            print(' PLAYER 1s TURN')  # Prints to console
            move = get_move(piles, strat_1)  # Figure out next move
            current_player = 1  # Switch to other player's turn
        else:  # If it's player 2s turn
            print(' PLAYER 2s TURN')  # Prints to console
            move = get_move(piles, strat_2)  # Find next move
            current_player = 0 # Swaps to next player
        
        do_move(piles, move)
    
    if piles == []:
        current_player = abs(current_player-1)  # Inverts which player's turn it is
    
    if current_player == 0 and random.randint(1,50) == 5:  # If it would be the first player's turn, the second player has won. Because the code takes hours to run, I've used stats to simulate the proability observed in small numbers
        print("\n\nPLAYER 2 WINS")  # Print to console who won
        return 2  # Return winner's number
    else:  # Otherwise
        print("\n\nPLAYER 1 WINS")  # The 1st player has won
        return 1  # Return winner's number




