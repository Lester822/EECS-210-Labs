"""
ASSIGNMENT_NAME: EECS 210 Assignment 6
FUNCTION: Solves sudokus
INPUTS: Text files as marked in main()
OUTPUTS: Various puzzles and their solutions
AUTHOR_NAME: Michael Stang
COLLABORATORS: None
CREATION_DATE: 11/06/2023
"""

def print_matrix(matrix):
    """Take in a matrix and print it nicely"""
    for row in matrix:  # Goes through each row
        for column in row:  # Goes through each column in each row
            print(column, end=" ")  # Prints the element followed by a space
        print()  # Adds a new line between rows

def read_in_matrix(filename):
    """Take in a filename and return a list of list matrix"""
    matrix_file = open(filename, 'r')  # Opens the given filename
    matrix = []  # A variable to hold the matrix
    for row in matrix_file:  # Goes through each line of the file
        matrix.append(row.split())  # Splits the line at each whitespace and appends it to the matrix
    
    return matrix  # Returns the matrix created

def recursive_solve(matrix, y_pos=0, x_pos=0):
    """Recursively solve a sudoku puzzle"""
    if x_pos >= 9:  # Checks if we've called the function with an improper x position, if so, moves on
        x_pos = 0  # Resets the x back to the beginning
        y_pos += 1  # Ups the y_pos
        if y_pos >= 9:  # If we are above 8, that means we've filled our board and everything SHOULD be valid
            return matrix

    if matrix[y_pos][x_pos] != "_":  # If we already have a number here, we don't need to do anything
        return recursive_solve(matrix, y_pos, x_pos + 1)  # Simply return the next position

    for num in range(1, 10):  # If we are not at the end, AND the current position is not blank, loop through each number 1 to 9
        matrix[y_pos][x_pos] = str(num)  # Set the position to be the string of the number of the current loop
        if check_valid(matrix):  # Check if that is a valid placemnt
            result = recursive_solve(matrix, y_pos, x_pos + 1)  # Branches with this placement if it was a valid placement
            if result is not None:  # If once everything has come back, we have returned a matrix instead of a None, we have found a full solution
                return result  # If so, return the matrix
        matrix[y_pos][x_pos] = "_"  # Reset the position back to blank after we're done so that backtracking shouldn't fail

    return None  # If we have no valid options, simply return None, which will trigger the if statements of previous calls in order to stop the branch

def check_valid(matrix):
    for row in matrix:  # Goes through each row of the matrix
        used = []  # Creates a list to hold values that have already been found
        for item in row:  # Goes through element in the row
            if item in used:  # If that element has already been marked in used, we have found a duplicate
                if item != "_":  # If the duplicate element is a blank space, that is OK.
                    return False  # If we have a duplicate that isn't blank, we have a problem
            else:  # If the item is not a duplicate,
                used.append(item)  # Add the item to the used list
    
    for index in range(9):  # Loops through numbers 0 to 8 (one for each column)
        used = []  # Creates a list to keep track of used values
        for inner_index in range(9):  # Loops through each item in each column
            if matrix[inner_index][index] in used:  # Checks if that item is already in used
                if matrix[inner_index][index] != "_":  # Duplicates of blanks is OK
                    return False  # If there is a duplicate of a non-blank, then it returns False to show that it is not valid
            else:  # If it's not a duplicate
                used.append(matrix[inner_index][index])  # Add it to the list of used numbers already
    
    starting_index = [(0,0), (0, 3), (0, 6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]  # A list of starting elements for the nine main 3x3 sub matricies
    for three_by_three in range(9):  # Loops 9 times (one for each 3x3 sub-matrix)
        used = []  # A list to keep track of elements already used
        y_sub_index = starting_index[three_by_three][0]  # Figures out the starting y pos
        x_sub_index = starting_index[three_by_three][1]  # Figures out the starting x pos
        for x_count in range(3):  # Loops 3 times (for each column of the sub-matrix)
            for y_count in range(3):  # Loops for each row of the sub-matrix
                if matrix[y_sub_index+y_count][x_sub_index+x_count] in used:  # If the element in the position has been marked as used
                    if matrix[y_sub_index+y_count][x_sub_index+x_count] != "_":  # And that element isn't blank (since Blanks are OK)
                        return False  # Returns False to show that it isn't valid
                else:  # If it is not a duplicate of something
                    used.append(matrix[y_sub_index+y_count][x_sub_index+x_count])  # Mark it as used
    return True  # Otherwise, if all three checks pass, the whole matrix is currently valid.


def per_puzzle(filename):
    """Take in a filename and do all needed actions for each example requested"""
    matrix = read_in_matrix(filename)  # Takes filename and passes it into read_in_matrix to return a list of list of the elemtents (each num is a string)
    solution = (recursive_solve(matrix))  # Passes the matrix into the recurrsive solver
    print(f"{filename}\n\nMatrix:\n")  # Prints the file name and does some formatting
    print_matrix(matrix)  # Prints the matrix using the print_matrix function
    print(f"\nSolution:\n")  # Prints header for formatting
    if solution is not None:  # Checks if there is a valid solution
        print_matrix(solution)  # Prints the matrix if there is one
    else:  # Otherwise,
        print("NO VALID SOLUTIONS")  # Print that there is not valid solutions
    print()  # Adds a blank line for formatting

def main():
    """Run the program"""
    per_puzzle("puzzle1.txt")  # Runs the code for puzzle 1
    per_puzzle("puzzle2.txt")  # Runs the code for puzzle 2
    per_puzzle("puzzle3.txt")  # Runs the code for puzzle 3
    per_puzzle("puzzle4.txt")  # Runs the code for puzzle 4
    per_puzzle("puzzle5.txt")  # Runs the code for puzzle 5

main()  # Starts the program