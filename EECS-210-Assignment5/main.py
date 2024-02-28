"""
ASSIGNMENT_NAME: EECS 210 Assignment 5
FUNCTION: Prints various relations and functions along with GCDs and coefficients
INPUTS: NONE
OUTPUTS: Various relation's functionality, and GCDs and coefficients
AUTHOR_NAME: Michael Stang
COLLABORATORS: ChatGPT helped a bit comprehension of Problem Three
CREATION_DATE: 10/23/2023
"""


def is_function(set_a, set_b, set_relation):
    """Take in 'A', 'B', and the relation set and return a boolean on whether or not it's a function"""
    used_points = set()  # A set that will hold the input values that are used in the set relation
    function_truth = True  # A bool variable that will keep track of whether or no the function is or isn't a function
    for point in set_relation:  # Loops through each point in the relation
        if point[0] in used_points:  # If the input value matches a value already looked at (as marked in used_points)
            function_truth = False  # Then say the relation isn't a function
            break  # And break to save computation time
        else:  # Otherwise,
            used_points.add(point[0])  # Mark the current input as a used one
    
    if len(set_a.intersection(used_points)) != len(set_a):  # Checks if the intersection of the used points and the input set are equally sized to ensure every input is used
        function_truth = False  # Sets the tracking var to false
    
    return function_truth  # Returns the value

def is_injective(set_a, set_b, set_relation):
    """
    Take in 'A', 'B', and the relation set and return a boolean on whether or not it's injective (meaning it each output has only one input)
    All functions that are fed into this are assumed to be functions already
    """
    used_outputs = set()  # An empty set to hold all the outputs already used
    injective_truth = True  # A variable to hold the truth value of the injectivness

    for point in set_relation:  # loops through each point in the relation
        if point[1] in used_outputs:  # If the output has already been marked as used
            injective_truth = False  # Say it's not injective
            break  # Break to save computation
        else:  # Otherwise,
            used_outputs.add(point[1])  # Add the output to used_inputs to mark its use
    
    return injective_truth  # Returns the boolean value of the injectivness

def is_surjective(set_a, set_b, set_relation):
    """Take in 'A', 'B', and the relation set and return a boolean on whether or not it's surjective"""
    used_outputs = set()  # An empty set to hold the used Bs so far

    for point in set_relation:  # Goes through each output
        used_outputs.add(point[1])  # Marks each output as used

    return (set_b == used_outputs)  # Returns True if the intersection of B and the used Bs is the same the list (meaning all were used)

def relation_inverse(set_relation):
    """Takes in a relation and outputs the inverse of it"""
    inverse_relation = set()  # A variable that will hold out inverted relation
    for point in set_relation:  # Goes through each point of the relation
        inverse_relation.add((point[1], point[0]))  # Adds the inverse point to the inverse relation
    return inverse_relation  # returns the inverse relation

def part_one_calcs(set_a, set_b, set_relation):
    """Take in 'A', 'B', and the relation set and return all the need values to answer part one for one given example"""
    relation_is_function = is_function(set_a, set_b, set_relation)  # Variable that will hold whether or not the relation is a function
    
    # All of the vars below will remain "N/A" if the relation is not a function
    relation_is_injective = "N/A"  # Variable that will hold whether or not the relation is injective
    relation_is_surjective = "N/A"  # Variable that will hold whether or not the relation is surjective
    relation_is_bijective = "N/A"  # Variable that will hold whether or not the relation is bijective
    inverse_relation = "N/A"  # Variable that will hold the inverse relation

    if relation_is_function:  # If the relation IS a function
        relation_is_injective = is_injective(set_a, set_b, set_relation)  # Gets the injectivness of the relation
        relation_is_surjective = is_surjective(set_a, set_b, set_relation)  # Gets the surjectivness of the relation
        relation_is_bijective = relation_is_injective and relation_is_surjective  # Gets the bijectivness of the relation

    if relation_is_bijective:  # If the relation is bijective
        inverse_relation = relation_inverse(set_relation)  # Finds the inverse

    return relation_is_function, relation_is_injective, relation_is_surjective, relation_is_bijective, inverse_relation  # Returns all of the needed values

def print_part_one(set_a, set_b, set_relation, letter):  # Handles the printing and data-gathering for give inputs for part one
    """Handle all the printing for part one"""
    values = part_one_calcs(set_a, set_b, set_relation)  # Gets the data needed
    print(f"\n{letter})\nA = {set_a}\nB = {set_b}\nf = {set_relation}\nIs Function?: {values[0]}\nIs Injective?: {values[1]}\nIs Surjective?: {values[2]}\nIs Bijective?: {values[3]}\nInverse?: {values[4]}\n")  # Actual output

def part_one():
    """Handle everything for part one"""
    print(f"{'-' * 7}\nPART 1\n{'-' * 7}\n")  # Header print
    print_part_one({'a', 'b', 'c', 'd'}, {'v', 'w', 'x', 'y', 'z'}, {('a', 'z'), ('b', 'y'), ('c', 'x'), ('d', 'w')}, 'a')  # Prints the given output
    print_part_one({'a', 'b', 'c', 'd'}, {'x', 'y', 'z'}, {('a', 'z'), ('b', 'y'), ('c', 'x'), ('d', 'z')}, 'b')  # Prints the given output
    print_part_one({'a', 'b', 'c', 'd'}, {'w', 'x', 'y', 'z'}, {('a', 'z'), ('b', 'y'), ('c', 'x'), ('d', 'w')}, 'c')  # Prints the given output
    print_part_one({'a', 'b', 'c', 'd'}, {1, 2, 3, 4, 5}, {('a', 4), ('b', 5), ('c', 1), ('d', 3)}, 'd')  # Prints the given output
    print_part_one({'a', 'b', 'c'}, {1, 2, 3, 4}, {('a', 3), ('b', 4), ('c', 1)}, 'e')  # Prints the given output
    print_part_one({'a', 'b', 'c', 'd'}, {1, 2, 3}, {('a', 2), ('b', 1), ('c', 3), ('d', 2)}, 'f')  # Prints the given output
    print_part_one({'a', 'b', 'c', 'd'}, {1, 2, 3, 4}, {('a', 4), ('b', 1), ('c', 3), ('d', 2)}, 'g')  # Prints the given output
    print_part_one({'a', 'b', 'c', 'd'}, {1, 2, 3, 4}, {('a', 2), ('b', 1), ('c', 2), ('d', 3)}, 'h')  # Prints the given output
    print_part_one({'a', 'b', 'c'}, {1, 2, 3, 4}, {('a', 2), ('b', 1), ('a', 4), ('c', 3)}, 'i')  # Prints the given output

def gcd_wp(num1, num2):
    """Takes in two numbers and outputs their GCD"""
    x = max(num1, num2)  # Finds the first initial value
    y = min(num1, num2)  # Finds the second initial value
    while y != 0:  # While we haven't found an R of 0
        r = x % y  # Calculate the remainder
        print(f"{x}/{y} = {x//y} R {r}")  # Outputs to console for user readability
        x = y  # Sets the next x to the previous y
        y = r  # Sets the next y to the previous remainder
    
    return x  # Returns the last x once y is equal to 0

def gcd(num1, num2):
    """Takes in two numbers and outputs their GCD and the steps w/out printing each step"""
    x = max(num1, num2)  # Finds the first initial value
    y = min(num1, num2)  # Finds the second initial value
    rows = []
    while y != 0:  # While we haven't found an R of 0
        r = x % y  # Calculate the remainder
        rows.append([x, y, x//y, r])  # [x = y * x//y + r]
        x = y  # Sets the next x to the previous y
        y = r  # Sets the next y to the previous remainder
    
    return x, rows   # Returns the last x once y is equal to 0


def part_two():
    """Handle everything for part two"""
    print(f"{'-' * 7}\nPART 2\n{'-' * 7}\n")  # Header print
    print(f"gcd(662, 414) = {gcd_wp(662, 414)}\n")  #  Outputs for the given GCD
    print(f"gcd(6, 14) = {gcd_wp(6, 14)}\n")  #  Outputs for the given GCD
    print(f"gcd(24, 36) = {gcd_wp(24, 36)}\n")  #  Outputs for the given GCD
    print(f"gcd(12, 42) = {gcd_wp(12, 42)}\n")  #  Outputs for the given GCD
    print(f"gcd(252, 198) = {gcd_wp(252, 198)}\n")  #  Outputs for the given GCD


def bezout_coefficients(a, b):
    """Compute the coefficients of a and b."""
    
    remainders = [a, b]  # Lists to store the remainders
    quotients = []  #  Lists to store the quotients

    # Euclidean Algorithm to compute gcd and quotients
    while remainders[-1] != 0:  # Goes until it hits a remainder of 0
        quotient = remainders[-2] // remainders[-1]  # calculate the quotient
        remainder = remainders[-2] % remainders[-1]  # calculate the reaminder
        
        quotients.append(quotient)  # Keeps track of the quotients
        remainders.append(remainder)  # Keeps track of the remainder

    s = [1, 0]  # Keeps track of s
    t = [0, 1]  # Keeps track of t
    for q in quotients:  # Goes through each quotient
        s.append(s[-2] - q * s[-1])  # Adds the new s
        t.append(t[-2] - q * t[-1])  # Adds the new t

        # these can be streamlined from question 4, since we don't need to display each of these steps, it can just do math

    return remainders, quotients, s[-2], t[-2]  # Returns the remainders, quoetients, and the second to last s and t

def per_example_problem_three(a, b):
    """Takes in two numbers and outputs their GCD and the Bez... coefficients printing each step"""
   
    remainders, quotients, s, t = bezout_coefficients(a, b)   # Fetch the remainders, quotients, and Bézout coefficients using the helper function

    # Display the initial steps of the Euclidean Algorithm
    for i in range(len(quotients)):  # Iterate over each quotient
        print(f"{remainders[i]} = {remainders[i+1]} * {quotients[i]} + {remainders[i+2]}")   # Display each division step
    
    
    if remainders[-2] != 0:  # Only display the last remainder if it's not zero (avoid displaying "0 = 0")
        print(f"{remainders[-2]} = {remainders[-2]}")  # Actually does the printing
    
    
    value = remainders[-2]  # Initialize the starting expression
    expr = str(value)  # Initialize the starting value
    
    # Iterate over the quotients in reverse to compute the backward steps
    for i in range(len(quotients)-1, -1, -1):
        old_expr = expr  # Backup the current expression
        
        value = remainders[i] - quotients[i] * remainders[i+1]   # Compute the next value using the current remainder and quotient
        
        expr = f"{remainders[i]} - {quotients[i]} * ({old_expr})"   # Put together the new expression
        
        
        print(f"{value} = {expr}") # Print the current step

    print(f"\ngcd({a}, {b}) = {s} * {a} + {t} * {b}\n")  # Display the final output


def part_three():
    """Handle everything for part three"""
    print(f"{'-' * 7}\nPART 3\n{'-' * 7}\n")  # Header print
    per_example_problem_three(252, 198)  # Runs the code for each given example set of numbers
    per_example_problem_three(6, 14)  # Runs the code for each given example set of numbers
    per_example_problem_three(24, 36)  # Runs the code for each given example set of numbers
    per_example_problem_three(12, 42)  # Runs the code for each given example set of numbers
    per_example_problem_three(252, 198)  # Runs the code for each given example set of numbers
    

def per_example_part_four(a,b):
    print('')  # prints a newline for formatting
    the_gcd, steps = gcd(a,b)  # Gets the GCD and each step of getting the GCD
    quotients = []  # A list that will hold all of the quotients
    index = 1  # This index keeps track of what q we are working on at a given point
    for step in steps:  # Goes through each step done
        quotients.append(step[2])  # Takes the quotient and stores it in the quotient list
        print(f"q{index} = {step[2]}, ", end='')  # Prints the quotients
        index += 1  # Ups the index
    print('')  # Prints a new line for formatting

    s_list = [1,0]  # The start to every s, this list will keep track of each s
    t_list = [0,1]  # The start to every t, this list will keep track of each t

    print("s0 = 1, s1 = 0", end='')  # Prints the inital 2

    index = 2  # Starts the indexing at 2 since we have two inital values
    for num in range(2,len(quotients)+1):  # Goes through every number from 2 to the end of the quotients (plus one since range is not inclusive)
        new_val_string = f"{s_list[num-2]} - {quotients[num-2]} * {s_list[num-1]}"  # Makes a string to show what it's doing for steps
        print(f", s{index} = s{index-2} - s{index-1} * q{index-1} = {new_val_string} = {s_list[num-2] - (quotients[num-2] * s_list[num-1])}", end='')  # Actually prints the value to the console
        s_list.append(s_list[num-2] - (quotients[num-2] * s_list[num-1]))  # Adds the calculated value to s_list
        index += 1  # Ups the index

    print("\nt0 = 0, t1 = 1", end='') # Prints the inital 2

    index = 2
    for num in range(2,len(quotients)+1):  # Goes through every number from 2 to the end of the quotients (plus one since range is not inclusive)
        new_val_string = f"{t_list[num-2]} - {quotients[num-2]} * {t_list[num-1]}"  # Makes a string to show what it's doing for steps
        print(f", s{index} = t{index-2} - t{index-1} * q{index-1} = {new_val_string} = {t_list[num-2] - (quotients[num-2] * t_list[num-1])}", end='')  # Actually prints the value to the console
        t_list.append(t_list[num-2] - (quotients[num-2] * t_list[num-1]))  # Adds the calculated value to t_list
        index += 1  # Ups the index
    
    print('')  # prints and empty line for formatting
    

def part_four():
    """Handle everything for part four"""
    print(f"{'-' * 7}\nPART 4\n{'-' * 7}\n")  # Header print
    per_example_part_four(414,662)  # Gets the appropriate information for the given numbers meant for examples
    per_example_part_four(6,14)  # Gets the appropriate information for the given numbers meant for examples
    per_example_part_four(24,36)  # Gets the appropriate information for the given numbers meant for examples
    per_example_part_four(12,42)  # Gets the appropriate information for the given numbers meant for examples
    per_example_part_four(252,198)  # Gets the appropriate information for the given numbers meant for examples


def main():
    """Runs the whole program"""
    part_one()  # Runs part one
    part_two()  # Runs part two
    part_three()  # Runs part three
    part_four()  # Runs part four


main()