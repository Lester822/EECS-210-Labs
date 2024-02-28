"""
ASSIGNMENT_NAME: EECS 210 Assignment 1
FUNCTION: Outputs various truth tables proving various logical propositions
INPUTS: NONE
OUTPUTS: 6 truth tables and labels for them representing various logical propositions
AUTHOR_NAME: Michael Stang
COLLABORATORS: NONE
CREATION_DATE: 08/27/2023
"""

import logic_functions as logic_f


def all_options_output(logic_functions, vars=['p', 'q']):
    '''
    FUNCTION: Output a list of a truth table for given inputs and logical functions
    INPUTS: List of list of functions and names of outputs (formatted [[FUNCTION, FUNCTION_NAME], [FUNCTION_2, FUNCTION_NAME]])
    OUTPUTS: List of strings, each being a line of the truth table
    '''
    
    possible_rows = 2 ** len(vars)  # Calculates the number of input rows that will be in the final table

    index = possible_rows - 1  # Gets the highest number (binary wise) of the possible rows (we care about 0 through 7, not 1 through 8 for example)

    output_lines = []  # This will be what is finally returned at the end of the function with each line being a seperate line to be printed.

    header_line = ''  # This variable represents the header line of the table. Various aspects are added to this stirng.

    for var in vars:  # Goes through each variable from the input VARS list, and adds them to the top each column (they are seperated by a " ")
        header_line += var + ' '  # Actually adds the variable to the header line
    
    header_line += '| '  # Adds the seperator between the input variables and the output variables

    for logic_function in logic_functions:  # Goes through each output and takes the name included in the list of lists in the various indexes at index 1.
        header_line += logic_function[1] + ' | '  # Adds the name and section divder to the header line

    output_lines.append(header_line)  # Adds the header as the first line of the output list

    output_lines.append('-' * len(header_line))  # Adds a divider line with a number of "-"s equal to the length of the line above to make equal spacing

    for i in range(possible_rows):  # Goes through the number of input rows that will be in the final table

        left_side = str(bin(index))[2:].replace('1', 'T').replace('0', 'F')  # Takes the current index (which starts at the highest value) and converts it to binary, then takes that binary and turns them into a string, then gets rid of the sign header off of the binary. It then converst 0s to Fs and 1s to Ts)

        while len(left_side) < len(vars):  # Back fills the left side of the rows that have less numbers in them. This ensures each line has the same number of characters.
            left_side = "F" + left_side

        left_side_output = ''  # This variable will be the input side of the table

        for char in left_side:  # Goes through each character in the left side (currently formatted like "TFF" as an example) and adds spaces for nicer output
            left_side_output += char + ' '  # Adds the space

        right_side_outputs = []  # This list will hold the output of each logical expression represented on the "Output"/Right side of the table.

        for logic_function in logic_functions:  # Goes through each logic function passed into this function
            right_side_output = logic_function[0](text_to_boolean(left_side))   # Uses "text_to_boolean" to convert the letters representing input into a list of Boolean values. Then it passes it into the next logical function in the loop, and gets back an output (either True or False).

            if right_side_output:  # If the returned value is True, 
                right_side_output = ' ' * (len(logic_function[1])//2) + 'T' + ' ' * ((len(logic_function[1])+1)//2) + '|' # it adds a True and does some math to figure out centering the output in the table by adding spaces equal to half the length of the name passed in with the output function.

            else: # If the output is False, 
                right_side_output = ' ' * (len(logic_function[1])//2) + 'F' + ' ' * ((len(logic_function[1])+1)//2) + '|' # it does the same as True, but with an "F"

            right_side_outputs.append(right_side_output)  # Adds the output to the list of ouputs that will be added together later
        
        final_right = ''  # The string that will hold the final output string of the right side of the current row on the current table

        for right_output in right_side_outputs:  # Goes through each output from the list of outputs
            final_right += right_output + ' '  # Adds the outputs to the final line with a space between them

        output_lines.append(left_side_output + "| " + final_right)  # Adds the entire line adding the left side, divider, and right side to the list of rows in the table

        index -= 1  # Counts down to get proper order of left side of the table

    output_lines.append('-' * len(output_lines[2]))  # Adds line at the bottom of the truth table for clarity
    output_lines.insert(0, '-' * len(output_lines[-1]))  # Adds line at the top of the truth table for clarity

    return output_lines  # Returns the list of lines, with each line being an entire row


def text_to_boolean(text):
    '''
    FUNCTION: Convert text representations (T or F) into true Boolean values in a list
    INPUTS: String of 'T's and 'F's representing Boolean values
    OUTPUTS: List of Boolean values
    '''

    logic_order = []  # The final list that will be returned

    for char in text:  # Goes through each "F" or "T" in the text

        if char == 'T':  # If the character is a "T",
            logic_order.append(True) # Adds True to the list

        elif char == 'F': # If the character is a "F",
            logic_order.append(False) # Adds False to the list

        else:  # Otherwise, someone put something bad as an input. 
            raise Exception("Invalid boolean value provided")  # Raises an exception to help fix future issues.
    
    return logic_order  # Returns the list of Boolean values

def main():
    # 1) DE MORGANS FIRST LAW
    print('1. De Morgan’s First Law\n')  # Header for the first table
    table_1 = all_options_output([[logic_f.de_morgan_first_o1, "!p + !q"], [logic_f.de_morgan_first_o2, "!(p * q)"]], ['p', 'q'])  # Creates a truth table using "all_options_output" function and two output functions from logic_functions.py. Logic is controlled by those functions.
    for line in table_1:  # Goes line by line of table
        print(line)  # Prints the line
    print('\n' + '*' * len(table_1[2]) + '\n')  # Creates a dividing line between tables using length of the third line of the table

    # 2) DE MORGANS SECOND LAW
    print('2. De Morgan’s Second Law\n')  # Header for the second table
    table_2 = all_options_output([[logic_f.de_morgan_second_o1, "!p * !q"], [logic_f.de_morgan_second_o2, "!(p + q)"]], ['p', 'q'])  # Creates a truth table using "all_options_output" function and two output functions from logic_functions.py. Logic is controlled by those functions.
    for line in table_2:  # Goes line by line of the table
        print(line)  #  Prints the line
    print('\n' + '*' * len(table_2[2]) + '\n')  # Creates a dividing line between tables using length of the third line of the table for clarity

    # 3) ASSOCIATIVE FIRST LAW
    print('3. First Associative Law\n')  # Header for the third table
    table_2 = all_options_output([[logic_f.associative_first_o1, "(p * q) * r"], [logic_f.associative_first_o2, "p * (q * r)"]], ['p', 'q', 'r'])  # Creates a truth table using "all_options_output" function and two output functions from logic_functions.py. Logic is controlled by those functions.
    for line in table_2:  # Goes line by line of the table
        print(line)  #  Prints the line
    print('\n' + '*' * len(table_2[2]) + '\n')  # Creates a dividing line between tables using length of the third line of the table for clarity

    # 4) ASSOCIATIVE SECOND LAW
    print('4. Second Associative Law\n')  # Header for the fourth table
    table_2 = all_options_output([[logic_f.associative_second_o1, "(p + q) + r"], [logic_f.associative_second_o2, "p + (q + r)"]], ['p', 'q', 'r'])  # Creates a truth table using "all_options_output" function and two output functions from logic_functions.py. Logic is controlled by those functions.
    for line in table_2:  # Goes line by line of the table
        print(line)  #  Prints the line
    print('\n' + '*' * len(table_2[2]) + '\n')  # Creates a dividing line between tables using length of the third line of the table for clarity

    # 5) [(p ∨ q) ∧ (p → r) ∧ (q → r)] → r ≡ T
    print('5. [(p ∨ q) ∧ (p → r) ∧ (q → r)] → r ≡ T\n')  # Header for the fourth table
    table_2 = all_options_output([[logic_f.fifth_o1, "[(p + q) * (p -> r) * (q -> r)] -> r "], [logic_f.fifth_o2, "True"]], ['p', 'q', 'r'])  # Creates a truth table using "all_options_output" function and two output functions from logic_functions.py. Logic is controlled by those functions.
    for line in table_2:  # Goes line by line of the table
        print(line)  #  Prints the line
    print('\n' + '*' * len(table_2[2]) + '\n')  # Creates a dividing line between tables using length of the third line of the table for clarity

    # 6) p ↔ q ≡ (p → q) ∧ (q → p)
    print('6. p ↔ q ≡ (p → q) ∧ (q → p)\n')  # Header for the fourth table
    table_2 = all_options_output([[logic_f.sixth_o1, "p <-> q"], [logic_f.sixth_o2, "(p -> q) * (q -> p)"]], ['p', 'q'])  # Creates a truth table using "all_options_output" function and two output functions from logic_functions.py. Logic is controlled by those functions.
    for line in table_2:  # Goes line by line of the table
        print(line)  #  Prints the line
    print('\n' + '*' * len(table_2[2]) + '\n')  # Creates a dividing line between tables using length of the third line of the table for clarity

main() # starts the program