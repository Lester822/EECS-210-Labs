"""
ASSIGNMENT_NAME: EECS 210 Assignment 4
FUNCTION: Prints various statements based on the properties of various sets and relations
INPUTS: NONE
OUTPUTS: Various sets and their properties
AUTHOR_NAME: Michael Stang
COLLABORATORS: NONE
CREATION_DATE: 10/09/2023
"""

def test_reflexive(input_set, relation):
    """Takes in a relation and a set and outputs whether or not it is reflexive, and the reflexive closure"""
    
    is_reflexive = True  # Sets the variable that controls whether the set is reflexive or not to default true
    reflexive_closure = set()  # Creates an empty set to hold the reflexive closure

    for point in relation:  # Goes through each point in the relation
        reflexive_closure.add(point)  # Adds the point to the closure

    for value in input_set:  # Goes through each value in the input set
        
        if (value, value) not in relation:  # Checks whether the point containing the current value of the input_set twice (x,x) is NOT in the relation.
            is_reflexive = False  # If it's not, it sets the is_reflexive value to false
            reflexive_closure.add((value, value))  # Adds the point (x, x) to the closure since it's not aready there and it is needed for reflexivness

    return (is_reflexive, reflexive_closure)  # Returns both the Boolean declaring the reflexiness and the closure
            
    
def test_symmetric(input_set, relation):
    """Takes in a relation and a set and outputs whether or not it is symmetric, and the symmetric closure"""
    
    is_symmetric = True  # Sets the variable that controls whether the set is symmetric or not to default true
    symmetric_closure = set()  # Creates an empty set to hold the symmetric closure

    for point in relation:  # Goes through each point in the relation
        symmetric_closure.add(point)  # Adds the point to the closure

    for point in relation:  # Goes through each value in the input set
        
        if (point[1], point[0]) not in relation:  # Checks whether the point which swaps the first and second values is NOT in the set
            is_symmetric = False  # If it's not, it sets the is_symmetric value to false
            symmetric_closure.add((point[1], point[0]))  # Adds the point (y, x) to the closure since it's not aready there and it is needed for symmetry

    return (is_symmetric, symmetric_closure)  # Returns both the Boolean declaring the reflexiness and the closure

def test_antisymmetric(input_set, relation):
    """Takes in a relation and a set and outputs whether or not it is antisymmetric, and the antisymmetric closure"""
    
    is_antisymmetric = True  # Sets the variable that controls whether the set is antisymmetric or not to default true

    for point in relation:  # Goes through each value in the input set
        if point[1] != point[0]:
            if (point[1], point[0]) in relation:  # Checks whether the point which swaps the first and second values IS in the set
                is_antisymmetric = False  # If it's not, it sets the is_antisymmetric value to false

    return (is_antisymmetric)  # Returns both the Boolean declaring the antireflexiness


def test_transitive(input_set, relation):
    """Takes in a relation and a set and outputs whether or not it is transitive, and the transitive closure"""
    matrix_version = set_to_matrix(input_set, relation)  # Makes a matrix from the sets
    closure_matrix = set_to_matrix(input_set, relation)  # Makes a copy of the matrix from the sets
    size = len(matrix_version)  # Gets the length of the matrix

    for k in range(size):  # Loops through for the length of matrix
        for i in range(size):  # Loops through for the length of matrix
            for j in range(size):  # Loops through for the length of matrix
                closure_matrix[i][j] = closure_matrix[i][j] or (closure_matrix[i][k] and closure_matrix[k][j])  # Sets matrix at position i,j to the logical expression (i,j) or (i,k and k,j)

    is_transitive = matrix_version == closure_matrix  # Checks if the closure matrix and the original are the same to figure out transitive

    return (is_transitive, closure_matrix)  # Returns the boolean answer and the closure matrix



def set_to_matrix(input_set, relation):
    """Converts a set of points into a matrix"""
    dimensions = len(input_set)  # Gets the dimensions that the square matrix will need to be
    matrix = []  # Creates a variable that will hold the matrix
    for x in range(dimensions):  # Loops for each row that is needed
        row = []  # Creates a row list that will be filled with nums
        for y in range(dimensions):  # Loops for each column that is needed
            row.append(0)  # Adds 0s to the row (equal to the num of columns needed)
        matrix.append(row)  # Adds the row to the matrix
    
    for point in relation:  # Goes through each point in the relation
        row = 0  # Variable that keeps track of what row the point should go
        column = 0  # Variable that keeps track of what column the point should go
        for value in input_set:  # Goes through each value in the set
            if value == point[0]:  # If the current value is equal to the first value of the point
                break  # Break out of the loop
            row += 1  # Keep track of the row that it was on
        for value in input_set:  # Same as above but with columns
            if value == point[1]:  # Checks if the value is equal to the second value in the point
                break  # Breaks out of the loop
            column += 1  # Otherwise adds 1 to the column count
        matrix[row][column] = 1  # Sets the value to 1 in the correct matrix position

    return matrix


def question_one():
    """The function that calls all the various functions and formats the output for question 1"""

    # Part D Numbers

    reflexive_set_one = {1,2,3,4}  # The first set given
    reflexive_relation_one = {(1,1), (4,4), (2,2), (3,3)}  # The first relation given
    reflexive_test_one = test_reflexive(reflexive_set_one, reflexive_relation_one)  # Runs the function that checks for reflexiness and returns a boolean and a closure

    print(f"\nR = {reflexive_relation_one}")  # Prints the relation
    if reflexive_test_one[0]:  # Checks if it is reflexive
        print("R is reflexive")  # If so, prints that
    else:  # If not
        print("R is not reflexive")  # Prints that it's not
        print(f"Reflexive Closure: {reflexive_test_one[1]}")  # Prints the reflexive closure

    # Part E Letters

    reflexive_set_two = {'a', 'b', 'c', 'd'}  # The first set given
    reflexive_relation_two = {('a','a'), ('c','c')}  # The first relation given
    reflexive_test_two = test_reflexive(reflexive_set_two, reflexive_relation_two)  # Runs the function that checks for reflexiness and returns a boolean and a closure

    print(f"\nR = {reflexive_relation_two}")  # Prints the relation
    if reflexive_test_two[0]:  # Checks if it is reflexive
        print("R is reflexive")  # If so, prints that
    else:  # If not
        print("R is not reflexive")  # Prints that it's not
        print(f"Reflexive Closure: {reflexive_test_two[1]}")  # Prints the reflexive closure


def question_two():
    """The function that calls all the various functions and formats the output for question 2"""

    # Part D Numbers

    set_one = {1,2,3,4}  # The first set given
    relation_one = {(1,2), (4,4), (2,1), (3,3)}  # The first relation given
    test_one = test_symmetric(set_one, relation_one)  # Runs the function that checks for symmetry and returns a boolean and a closure

    print(f"\nR = {relation_one}")  # Prints the relation
    if test_one[0]:  # Checks if it is symmetric
        print("R is symmetric")  # If so, prints that
    else:  # If not
        print("R is not symmetric")  # Prints that it's not
        print(f"Symmetric Closure: {test_one[1]}")  # Prints the symmetric closure

    # Part E Numbers

    set_two = {1,2,3,4}  # The first set given
    relation_two = {(1,2), (3,3)}  # The first relation given
    test_two = test_symmetric(set_two, relation_two)  # Runs the function that checks for symmetry and returns a boolean and a closure

    print(f"\nR = {relation_two}")  # Prints the relation
    if test_two[0]:  # Checks if it is symmetric
        print("R is symmetric")  # If so, prints that
    else:  # If not
        print("R is not symmetric")  # Prints that it's not
        print(f"Symmetric Closure: {test_two[1]}")  # Prints the symmetric closure


def question_three():
    """The function that calls all the various functions and formats the output for question 3"""

    # Part D Numbers

    set_one = {'a','b','c','d'}  # The first set given
    relation_one = {('a','b'), ('d','d'), ('b','c'), ('a','c')}  # The first relation given
    test_one = test_transitive(set_one, relation_one)  # Runs the function that checks for transitive-ness and returns a boolean and a closure

    print(f"\nR = {relation_one}")  # Prints the relation
    if test_one[0]:  # Checks if it is transitive
        print("R is transitive")  # If so, prints that
    else:  # If not
        print("R is not transitive")  # Prints that it's not
        print(f"Transitive Closure:")  # Prints the transitive closure
        for row in test_two[1]:
            print(row)
        print()

    # Part E Numbers

    set_two = {1,2,3}  # The first set given
    relation_two = {(1,1),(1,3),(2,2),(3,1),(3,2)}  # The first relation given
    test_two = test_transitive(set_two, relation_two)  # Runs the function that checks for transitive-ness and returns a boolean and a closure

    print(f"\nR = {relation_two}")  # Prints the relation
    if test_two[0]:  # Checks if it is transitive
        print("R is transitive")  # If so, prints that
    else:  # If not
        print("R is not transitive")  # Prints that it's not
        print(f"Transitive Closure:")  # Prints the transitive closure
        for row in test_two[1]:  # Goes through each row of the matrix
            print(row)  # Prints the row
        print()  # Adds a blank line


def question_four():
    """The function that calls all the various functions and formats the output for question 4"""

    # Part D Numbers

    set_one = {1,2,3}  # The first set given
    relation_one = {(1,1),(2,2),(2,3)}  # The first relation given

    reflexive = test_reflexive(set_one, relation_one)  # Checks whether the set is reflexive
    symmetric = test_symmetric(set_one, relation_one)  # Checks whether the set is symmetric
    transitive = test_transitive(set_one, relation_one)  # Checks whether the set is transitive

    equivilance =  reflexive[0] and symmetric[0] and transitive[0]  # Checks whether the set is all three of the above

    print(f"\nR = {relation_one}")  # Prints the relation
    
    if equivilance:  # Checks if it is transitive
        print("R is an equivilance relation")  # If so, prints that
    else:  # If not
        print("R is not an equivilance relation.\nReason: ")  # Prints that it's not
        if not reflexive[0]:  # Checks if it was reflexive
            print('NOT Reflexive')  # if not, tells the user
        if not symmetric[0]:  # Checks if it was symmetric
            print('NOT Symmetric')  # if not, tells the user
        if not transitive[0]:  # Checks if it was transitive
            print('NOT Transitive')  # if not, tells the user


    # Part E Numbers

    set_two = {'a', 'b', 'c'}  # The second set given
    relation_two = {('a','a'),('b','b'),('c','c'),('b','c'),('c','b')}  # The second relation given

    second_reflexive = test_reflexive(set_two, relation_two)  # Checks whether the set is reflexive
    second_symmetric = test_symmetric(set_two, relation_two)  # Checks whether the set is symmetric
    second_transitive = test_transitive(set_two, relation_two)  # Checks whether the set is transitive

    second_equivilance =  second_reflexive[0] and second_symmetric[0] and second_transitive[0]  # Checks whether the set is all three of the above

    print(f"\nR = {relation_two}")  # Prints the relation
    
    if second_equivilance:  # Checks if it is transitive
        print("R is an equivilance relation")  # If so, prints that
    else:  # If not
        print("R is not an equivilance relation.\nReason: ")  # Prints that it's not
        if not second_reflexive[0]:  # Checks if it was reflexive
            print('NOT Reflexive')  # if not, tells the user
        if not second_symmetric[0]:  # Checks if it was symmetric
            print('NOT Symmetric')  # if not, tells the user
        if not second_transitive[0]:  # Checks if it was transitive
            print('NOT Transitive')  # if not, tells the user

    print() # prints a blank line to make it look nice

def question_five():
    """The function that calls all the various functions and formats the output for question 5"""

    # Part D Numbers

    set_one = {1, 2, 3, 4}  # The first set given
    relation_one = {(1,1), (1,2), (2,2), (3,3), (4,1),(4,2), (4,4)}  # The first relation given

    reflexive = test_reflexive(set_one, relation_one)  # Checks whether the set is reflexive
    antisymmetric = test_antisymmetric(set_one, relation_one)  # Checks whether the set is antisymmetric
    transitive = test_transitive(set_one, relation_one)  # Checks whether the set is transitive

    equivilance =  reflexive[0] and antisymmetric and transitive[0]  # Checks whether the set is all three of the above

    print(f"\nR = {relation_one}")  # Prints the relation
    
    if equivilance:  # Checks if it is transitive
        print("R is a poset")  # If so, prints that
    else:  # If not
        print("R is not a poset.\nReason: ")  # Prints that it's not
        if not reflexive[0]:  # Checks if it was reflexive
            print('NOT Reflexive')  # if not, tells the user
        if not antisymmetric:  # Checks if it was symmetric
            print('NOT Antisymmetric')  # if not, tells the user
        if not transitive[0]:  # Checks if it was transitive
            print('NOT Transitive')  # if not, tells the user


    # Part E Numbers

    set_two = {0, 1, 2, 3}  # The second set given
    relation_two = {(0, 0), (0,1), (0, 2), (0, 3), (1,0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 2), (3, 3)}  # The second relation given

    second_reflexive = test_reflexive(set_two, relation_two)  # Checks whether the set is reflexive
    second_antisymmetric = test_antisymmetric(set_two, relation_two)  # Checks whether the set is antisymmetric
    second_transitive = test_transitive(set_two, relation_two)  # Checks whether the set is transitive

    second_equivilance =  second_reflexive[0] and second_antisymmetric and second_transitive[0]  # Checks whether the set is all three of the above

    print(f"\nR = {relation_two}")  # Prints the relation
    
    if second_equivilance:  # Checks if it is transitive
        print("R is an equivilance relation")  # If so, prints that
    else:  # If not
        print("R is not an equivilance relation.\nReason: ")  # Prints that it's not
        if not second_reflexive[0]:  # Checks if it was reflexive
            print('NOT Reflexive')  # if not, tells the user
        if not second_antisymmetric:  # Checks if it was symmetric
            print('NOT Antisymmetric')  # if not, tells the user
        if not second_transitive[0]:  # Checks if it was transitive
            print('NOT Transitive')  # if not, tells the user

    print() # prints a blank line to make it look nice

def main():
    """The main function of the program that triggers the funciton that results in the answer for each question"""
    print('\nQUESTION 1\n')  # Question header
    question_one()  # Calls the first question
    print('\nQUESTION 2\n')  # Question header
    question_two()  # Calls the second question
    print('\nQUESTION 3\n')  # Question header
    question_three()  # Calls the third question
    print('\nQUESTION 4\n')  # Question header
    question_four()  # Calls the fourth question   
    print('\nQUESTION 5\n')  # Question header
    question_five()  # Calls the fourth question   


main()