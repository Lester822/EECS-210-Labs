"""
ASSIGNMENT_NAME: EECS 210 Assignment 3
FUNCTION: Show the logic behind several set functions
INPUTS: NONE
OUTPUTS: Outputs various sets and truth values for various set operations
AUTHOR_NAME: Michael Stang
COLLABORATORS: NONE
CREATION_DATE: 09/25/23
"""

def composite(set_one, set_two):
    solution = set()  # The set that will hold the final answer

    for first_item in set_one:  # Goes through each item in the first set

        for second_item in set_two:  # Goes through each item in the second set

            if first_item[1] == second_item[0]:  # If the second element from the first set is the same as the first element from the second item 

                solution.add((first_item[0], second_item[1]))  # Adds the pair of the first item from the first set and the second item from the second set

    return solution


def problem_one():
    """Handles all of question 1"""

    # Setup for problem 1
    print("\nProblem 1: ")  # Tell the user the following are the answers to problem 1

    set_one = {(1,1), (2,2), (3,3)}  # Initializes the first set as given in the problem
    set_two = {(1,1), (1,2), (1,3), (1,4)}  # Initializes the second set as given in the problem

    print(f"R1: {set_one}")  # Shows the user the first set
    print(f"R2: {set_two}\n")  # Shows the user the second set

    # Problem 1a (R1 U R2)

    problem_1a_output = set()  # Creates a new set to hold the final answer in

    for item in set_one:  # Goes through each item of set one
        problem_1a_output.add(item)  # Adds the item to the final answer set

    for item in set_two:  # Goes through each item of set two
        problem_1a_output.add(item)  # Adds the item to the final answer set

    print(f"R1 ∪ R2: {problem_1a_output}\n")  # Displays the final set to the user

    # Problem 1b (R1 ∩ R2)

    problem_2a_output = set()  # Creates a new set to hold the final answer in

    for item in set_one:  # Goes through each item of set one
        if item in set_two:  # If the item is in the other set
            problem_2a_output.add(item)  # Add the item to the final answer set

    print(f"R1 ∩ R2: {problem_2a_output}\n")  # Displays the final set to the user
    
    # Problem 1c (R1 - R2)

    problem_3a_output = set()  # Creates a new set to hold the final answer in

    for item in set_one:  # Goes through each item of set one
        if item not in set_two:  # If the item is not in the other set
            problem_3a_output.add(item)  # Add the item to the final answer set

    print(f"R1 - R2: {problem_3a_output}\n")  # Displays the final set to the user

    # Problem 1d (R2 - R1)

    problem_4a_output = set()  # Creates a new set to hold the final answer in

    for item in set_two:  # Goes through each item of set one
        if item not in set_one:  # If the item is not in the other set
            problem_4a_output.add(item)  # Add the item to the final answer set

    print(f"R2 - R1: {problem_4a_output}\n")  # Displays the final set to the user


def problem_two():
    """Handles all of question 2"""

    # Setup for problem 1
    print("\nProblem 2: ")  # Tell the user the following are the answers to problem 1

    set_one = {(1,1), (1,4), (2,3), (3,1), (3,4)}  # Initializes the first set as given in the problem
    set_two = {(1,0), (2,0), (3,1), (3,2), (4,1)}  # Initializes the second set as given in the problem

    print(f"R1: {set_one}")  # Shows the user the first set
    print(f"R2: {set_two}\n")  # Shows the user the second set

    problem_two_set = composite(set_one, set_two)  # Calls the composite function which takes in two sets and returns a set of the composite
    
    print(f"S ◦ R: {problem_two_set}\n")  # Outputs the final answer to the user


def problem_three():
    """Handles all of question 3"""

    # Setup for problem 1
    print("\nProblem 3: ")  # Tell the user the following are the answers to problem 1

    set_one = {(1,1), (1,4), (2,3), (3,1), (3,4)}  # Initializes the first set as given in the problem

    print(f"R: {set_one}\n")  # Shows the user the set

    problem_three_set = composite(set_one, set_one)

    print(f"R^2: {problem_three_set}\n")  # Outputs the final answer to the user


def problem_four():
    """Handles all of question 4"""

    # Setup for problem 4
    print("\nProblem 4: ")  # Tell the user the following are the answers to problem 1

    set_one = set()  # Initializes the set that will be used to store the points

    for x in range(-10,11):  # Goes through each number -10 through 10 for x
        for y in range (-10, 11):  # Goes through each number -10 through 10 for y
            if (x + y) == 0:  # If x + y is equal to 0 (which is the condition)
                set_one.add((x,y))  # Add that point to the set

    number_set = range(-10,11)  # A variable holding all of the numbers that make up the pairs

    # Problem 4a (Show R)

    print(f"R: {set_one}\n")  # Shows the user the first set

    # Problem 4b (Reflexive)

    is_reflexive = True  # A variable that will keep track of whether or not the set is reflexisve
    first_to_break_reflexive = None  # A variable that will track what the first pair not found in the set that breaks reflexivity

    for number in number_set:  # Goes through each number in the initial number set
        if (number, number) not in set_one:  # If the set of the numnber is not in the set
            is_reflexive = False  # Set reflexive to false
            first_to_break_reflexive = (number, number)  # track what number did it 
            break  # Break out of loop

    print(f"R is Reflexive: {is_reflexive}", end=' ')  # Prints the final result of "is_reflexive"
    if not is_reflexive:  # Checks if it was non-reflexive
        print(f"| Example Pair Missing: {first_to_break_reflexive}")  # If so, prints an extra message with the number pair that wasn't found
    print()  # Adds a blank line for formatting


    # Problem 4c (Symmetric)

    is_symmetric = True  # A variable that holds whether or not the set is symmetric
    pair_to_break_symmetric = None

    for pair in set_one:  # Goes through each pair in the set

        if (pair[1], pair[0]) not in set_one:  # Checks if the inverted pair is NOT in the set
            is_symmetric = False  # Sets symmetric to false since a missing pair
            pair_to_break_symmetric = (pair[1], pair[0])
            break  # Breaks out of loop

    print(f"R is Symmetric: {is_symmetric}", end=' ')  # Prints the final result of "is_symmetric"
    if not is_symmetric:  # Checks if it was non-symmetric
        print(f"| Example Pair Missing: {pair_to_break_symmetric}")  # If so, prints an extra message with the number pair that wasn't found
    
    print('\n')  # Adds a blank line for formatting

    # Problem 4d (Antisymmetric)

    is_antisymmetric = True  # The variable holding whether or not it is antisummetric (starts as true)
    pair_to_break_anti = None  # The variable that will hold what point breaks anti_symmetry

    for pair in set_one:  # Goes through each pair in the set
        
        if (pair[1], pair[0]) in set_one:  # Checks if the inverse exsists
            is_antisymmetric = False  # Sets is_symmetric to False
            pair_to_break_anti = (pair[1], pair[0])  # Marks the first point in the set that is the symmetry of another
            break  # Breaks out of loop

    print(f"R is Antisymmetric: {is_antisymmetric}", end=' ')  # Prints the final result of "is_antisymmetric"
    if not is_antisymmetric:  # Checks if it was non-antisymmetric
        print(f"| Example Pair Missing: {pair_to_break_anti}")  # If so, prints an extra message with the number pair that wasn't found
    print()  # Adds a blank line for formatting

    # Problem 4e (Transitive)

    is_transitive = True  # The variable that holds whether the set is transitive
    pair_to_break_transitive = None  # The variabe that holds what the first point that is missing for it to transitive

    for first_pair in set_one:  # Goes through each pair in the set
        if not is_transitive:  # checks if it has already found an issue
            break  # If so, breaks
        for second_pair in set_one:  # For each pair, goes through every other pair
            if not(first_pair == second_pair):  # if the points aren't the same
                if (first_pair[1] == second_pair[0]) and (first_pair[0] != second_pair[1]):  # if the second element of the first point, is the same as the first element of the second and makes sure the two points are not the same as (a,b) (b, c) requires c and a be different
                    if not ((first_pair[0], second_pair[1]) in set_one):  # If the point containing the first element of the first point, and the second of the second is not in the list
                        is_transitive = False  # Means that the set is not transitive and sets this to false
                        pair_to_break_transitive = (first_pair[0], second_pair[1])  # Keeps track of what point would be needed to fix the first issue
                        break  # Breaks out of loop

    print(f"R is Transitive: {is_transitive}", end=' ')  # Prints the final result of "is_transitive"
    if not is_transitive:  # Checks if it was non-transitive
        print(f"| Example Pair Missing: {pair_to_break_transitive}")  # If so, prints an extra message with the number pair that wasn't found
    print()  # Adds a blank line for formatting
                


def main():
    """Calls the various questions' associated function"""
    problem_one()  # Calls the function to answer question 1
    problem_two()  # Calls the function to answer question 2
    problem_three()  # Calls the function to answer question 3
    problem_four()  # Calls the function to answer question 4

main()  # Starts the program