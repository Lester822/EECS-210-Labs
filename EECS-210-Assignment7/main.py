"""
ASSIGNMENT_NAME: EECS 210 Assignment 7
FUNCTION: Prints the number of combinations of various objects in various boxes
INPUTS: NONE
OUTPUTS: Various number of possibilities of objects in boxes
AUTHOR_NAME: Michael Stang
COLLABORATORS: In-class slides
CREATION_DATE: 12/25/2023
"""

from math import factorial
from math import pow

def combination(n, r):
    """Calculates the combination of n and r"""
    return factorial(n)/(factorial(n-r) * factorial(r))  # Does the math as provided in the slides and returns it

def sterling(n, j):
    """Calculates the sterling number of n and j"""
    summation = 0  # A variable to hold the value of the summation
    for i in range(j):  # Loops to calculate the sum from i to j-1
        summation += (pow((-1), i) * combination(j, i) * pow((j - i), n))  # Uses the formula as given
    return ((1/factorial(j)) * summation)  # Returns the value of the summation times 1/j!

def dist_obj_dist_box(object_count, box_count, objects_per_box):
    """Calculates the number of ways to put [objects] distinguishable objects into [boxes] distinguishable boxes."""
    objects_left = object_count  # A variable that will store how many objects are left
    final_value = 1  # The variable that will hold the final value, similar to a sum variable
    for num in range(box_count):  # Loops for each box
        value = factorial(objects_left)/(factorial(objects_left-objects_per_box) * factorial(objects_per_box))  # Cacluates the number of ways for each "box"
        final_value = final_value * value  # Multiplies it by the previous boxes to get the number of ways total
        objects_left -= objects_per_box  # Reduces the objects_left by the objects "used"
    return int(final_value)  # Returns the value

def indist_obj_dist_box(object_count, box_count):
    """Calculates the number of ways indist objects can be fit into distinguishable boxes """
    return int(combination(object_count+box_count-1, object_count))  # Uses the formula provided on the slides

def dist_obj_indist_box(object_count, box_count):
    """Calculates the number of ways distinguishable objects can be fit into indistinguishable boxes """
    summation = 0  # A variable that will hold our sum
    for j in range(1, box_count+1):  # Loops from j to k
        summation += sterling(object_count, j)  # Adds up the sterling numbers as calculated by sterling()
    return int(summation)  # Returns the final summation


def indist_obj_indist_box(object_count, box_count):
    """Calculates the number of ways indistinguishable objects can be fit into indistinguishable boxes"""

    def add_one(box_list):
        """Sub function that adds one to the list of boxes correctly as to not duplicate"""
        added = False  # Keeps track of if something was added
        for i in range(len(box_list)):  # Loops through each index in the list
            if i != 0:  # Checks if we're looking at the first number to avoid index errors
                if i == len(box_list) - 1:  # Checks if it's add the end of the list
                    if box_list[i-1] > box_list[i]:  # Checks if the ending element is smaller than the previous one
                        box_list[i] += 1  # Adds one to the last element
                        added = True  # Marks that we added something
                        break  # Breaks out of the loop to only increment once
                else:  # If it's not the last
                    if box_list[i-1] > box_list[i] and box_list[i] == min(box_list):  # Checks if the element is the smaller than the previous and is the smallest element
                        box_list[i] += 1  # If so, add one to it
                        for k in range(i+1, len(box_list)):  # Loops through every element after it
                            box_list[k] = 0  #  Sets it equal to 0 to get all possible combination
                        added = True  # Marks that we added something
                        break  # breaks out to only increment once
        if added == False:  # If it did not add anything, we have to increase the first element
            box_list[0] = box_list[0] + 1  # So we do that
            for j in range(len(box_list)):  # Loop though all other elements
                if j != 0:  # Doesn't reset the first one
                    box_list[j] = 0  # Resets the rest

    solutions = []  # A list to hold solutions that work
    boxes = []  # A list to store possible solutions

    for item in range(box_count):  # Loops a number of times equal to the number of boxes
        if item == 0:  # Checks if we are at the first element, 
            boxes.append(1)  # if so we set it to 1
        else:  # Otherwise
            boxes.append(0)  # Fills the rest with 0s

            # The end result is a list with a number of elements equal to the number of boxes [1,0,0,0,...]

    

    while sum(boxes) < (object_count * box_count):  # While the sum of all the elements isn't bigger than the maximum possible
        add_one(boxes)  # Increments boxes by 1
        if sum(boxes) == object_count:  # If the sum of the combination is equal to the targeted object count
            solutions.append(boxes.copy())  # Adds the solution to the list of solutions
        
    return len(solutions)  # Returns the number of solutions





def question_one():
    """Runs the code needed for question 1"""
    print("-" * 12)  # Prints a line for formatting
    print("QUESTION 1")  # Prints the header
    print("-" * 12 + "\n")  # Prints a line for formatting
    
    # EXAMPLE 8 (question a)
    print("QUESTION 1A:\nThe number of ways to distribute 52 cards to 4 players giving each player 5 cards")  # Prints the problem
    print(f"Number of Ways: {dist_obj_dist_box(52,4,5)}")  # The number of ways to distribute 52 cards to 4 players giving each player 5 cards

    # QUESTION B
    print("\nQUESTION 2A:\nThe number of ways to distribute 40 books into 4 boxes putting 10 books in each box")  # Prints what the problem is
    print(f"Number of Ways: {dist_obj_dist_box(40,4,10)}")  # Prints the solution using the function dist_obj_dist_box()


def question_two():
    """Runs the code needed for question 2"""
    print("\n" + "-" * 12)  # Prints a line for formatting
    print("QUESTION 2")  # Prints the header
    print("-" * 12 + "\n")  # Prints a line for formatting

    print("QUESTION 2A:\nHow many ways are there to place 10 indistinguishable balls into 8 distinguishable bins?")  # Prints the problem
    print(f"Number of Ways: {indist_obj_dist_box(10, 8)}")  # The number of ways to distribute 10 balls into 8 boxes

    print("\nQUESTION 2B:\nHow many ways are there to distribute 12 indistinguishable balls into six distinguishable bins?")  # Prints the problem
    print(f"Number of Ways: {indist_obj_dist_box(12, 6)}")  # The number of ways to distribute 12 balls into 6 boxes


def question_three():
    """Runs the code needed for question 3"""
    print("\n" + "-" * 12)  # Prints a line for formatting
    print("QUESTION 3")  # Prints the header
    print("-" * 12 + "\n")  # Prints a line for formatting

    print("QUESTION 3A:\nHow many ways can Anna, Billy, Caitlin, and Danny be placed into three indistinguishable homerooms?")  # Prints the problem
    print(f"Number of Ways: {dist_obj_indist_box(4, 3)}")  # The number of ways to distribute 4 people into 3 classrooms

    print("\nQUESTION 3B:\nHow many ways are there to put five temporary employees into four identical offices?")  # Prints the problem
    print(f"Number of Ways: {indist_obj_dist_box(5, 4)}")  # The number of ways to distribute 5 employees into 4 officies


def question_four():
    """Runs the code needed for question 4"""
    print("\n" + "-" * 12)  # Prints a line for formatting
    print("QUESTION 4")  # Prints the header
    print("-" * 12 + "\n")  # Prints a line for formatting

    print("QUESTION 4A:\nHow many ways can you pack six copies of the same book into four identical boxes?")  # Prints the problem
    print(f"Number of Ways: {indist_obj_indist_box(6, 4)}")  # The number of ways to pack 6 books into 4 boxes

    print("\nQUESTION 4B:\nHow many ways are there to distribute five indistinguishable objects into three indistinguishable boxes?")  # Prints the problem
    print(f"Number of Ways: {indist_obj_indist_box(5, 3)}")  # The number of ways to distribute 5 objects into three boxes


def main():
    """Runs the questions in order"""
    question_one()  # Runs the function that does question 1
    question_two()  # Runs the function that does question 2
    question_three()  # Runs the function that does question 3
    question_four()  # Runs the function that does question 4
    

main()  # Starts the program