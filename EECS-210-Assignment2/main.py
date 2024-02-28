"""
ASSIGNMENT_NAME: EECS 210 Assignment 2
FUNCTION: Outputs various truth statements showcasing logical quantifiers
INPUTS: NONE
OUTPUTS: The logical answers to two questions, each with 6 parts (a-f)
AUTHOR_NAME: Michael Stang
COLLABORATORS: NONE
CREATION_DATE: 09/11/2023
"""

def onevar_nice_output(logic_input): 
    """Take in logic statement and print it nicely. Inpuut is a tuple in the form {BOOL, LIST/INT}"""
    if logic_input[1] == []:  # Checks if the vars that prove it are an empty list
        vars = None  # if they are replace that with None
    else:  # otherwise
        vars = logic_input[1]  # set the vars to be the value of logic_input[1]
    print(f'     {logic_input[0]} | Single Var(s) That Proves It: {vars}')

    

def onevar_un_qual(domain, statement, inverse=False):
    """Function that takes in domain, statement, and whether its inverted and returns the universal qualifier output"""
    is_true = True  # Assumes true to start, only need one false to change
    prove_var = None  # Var to keep track of what variable proves that it's fales
    for x in domain:  # goes through each number in the domain
        if not statement(x):  # Checks if it makes the statement false
            is_true = False  # If it does, that means the universal qualifier will be false
            prove_var = x  # And keeps track of the num that caused it
            break  # Breaks the loop to get the first num that caused it
    
    if inverse:  # checks if the statement is a not Universal Qualifier
        is_true = not is_true  # if it is, inverts the final answer

    return is_true, x  # passes back the final BOOL and the num that triped it to be false if it did (otherwises passees None)

def onevar_ex_qual(domain, statement, inverse=False):
    """Function that takes in domain, statement, and whether its inverted and returns the existential qualifier output"""
    is_true = False  # Starts as false, only needs one true to change it the other way
    prove_var = None  # Keeps track of what number 'trips' the change to True
    for x in domain:  # Goes through each num in the domain
        if statement(x):  # If the num makes the statement True
            is_true = True  # Flip the is_true var
            prove_var = x  # Keep track of what number did that
            break  # Break out of the loop to keep track of the first num that switches the var
    
    if inverse:  # Checks if user wants the value of not EQ
        is_true = not is_true  # if so, flips the output

    return is_true, prove_var  # passes back the final BOOL and the num that caused the swap (otherwise passes back None)

def problem_one():
    """The entire code for problem 1"""

    print('QUESTION 1: ')  # Informs the user that this is question 1

    domain = [0,1,2,3,4,5,6,7,8,9,10]  # The list of the domains of X for the asserations
    print('\n' + '-' * 15 + '\n')  # A nice line for formating

    # Part 'a'

    print('1a -> ∃x P(x), where P(x) is the statement “x<2”')  # Prints the question
    onevar_nice_output(onevar_ex_qual(domain, lambda x: x < 2))  # Passes the various values (including the logic as a lambda function) into the function to get a final answer, which is passed into the function for nice output 
    print('\n' + '-' * 15 + '\n')  # A nice line for formating

    # Part 'b'

    print('1b -> ∀x P(x), where P(x) is the statement “x<2”')  # Prints the question
    onevar_nice_output(onevar_un_qual(domain, lambda x: x < 2))  # Passes the various values (including the logic as a lambda function) into the function to get a final answer, which is passed into the function for nice output 
    print('\n' + '-' * 15 + '\n')  # A nice line for formating

    # Part 'c'

    print('1c -> ∃x (P(x) ∨ Q(x)) where P(x) is the statement “x<2” and where Q(x) is the statement “x>7”')  # Prints the question
    onevar_nice_output(onevar_ex_qual(domain, lambda x: (x < 2) or (x > 7)))  # Passes the various values (including the logic as a lambda function) into the function to get a final answer, which is passed into the function for nice output 
    print('\n' + '-' * 15 + '\n')  # A nice line for formating
    
    # Part 'd'

    print('1d -> ∀x (P(x) ∨ Q(x)) where P(x) is the statement “x<2” and where Q(x) is the statement “x>7”')  # Prints the question
    onevar_nice_output(onevar_un_qual(domain, lambda x: (x < 2) or (x > 7)))  # Passes the various values (including the logic as a lambda function) into the function to get a final answer, which is passed into the function for nice output 
    print('\n' + '-' * 15 + '\n')  # A nice line for formating
    
    # Part 'e'
    
    print('1e -> Prove De Morgan’s Law for the Existential Quantifier where P(x) is the statement “x<5”\n')  # Prints the question
    print('∃x P(x)')  # prints the part of the question
    onevar_nice_output(onevar_ex_qual(domain, lambda x: x < 5))  # Passes the various values (including the logic as a lambda function) into the function to get a final answer, which is passed into the function for nice output 

    print('\n¬∀x ¬P(x)')  # prints the part of the question
    onevar_nice_output(onevar_un_qual(domain, lambda x: x >= 5, True))  # Passes the various values (including the logic as a lambda function) into the function to get a final answer, which is passed into the function for nice output 
    print('\n' + '-' * 15 + '\n')  # A nice line for formating

    # Part 'f'
    
    print('1f -> Prove De Morgan’s Law for the Universal Quantifier where P(x) is the statement “x<5”\n')  # prints the quesiton
    print('∀x P(x)')  # prints the part of the question
    onevar_nice_output(onevar_un_qual(domain, lambda x: x < 5))  # Passes the various values (including the logic as a lambda function) into the function to get a final answer, which is passed into the function for nice output 

    print('\n¬∃x ¬P(x)')  # prints the part of the question
    onevar_nice_output(onevar_ex_qual(domain, lambda x: x >= 5, True))  # Passes the various values (including the logic as a lambda function) into the function to get a final answer, which is passed into the function for nice output 
    print('\n' + '-' * 15 + '\n')  # A nice line for formating


def twovar_ex_qual(domain, statement, in_var, next):
    is_true = False  # sets initial value of is_true to False, requiring ONE value that flips it
    prove_vars = []  # A blank list to hold what variables will prove the statement

    for x in domain:  # Goes through each item in the domain given
        if next is not None:  # If there is a more inner statement, do this

            truth_value = next(domain, statement, x, None)  # Gets the innerstatement value. truth_value = {BOOL, [FLOAT, FLOAT]}

            if truth_value[0]:  # If the boolean of the inner statement is true
                is_true = True  # We declare the value of this to be true since we only need one correct
                prove_vars = [x, truth_value[1][1]]  # Marks the proven variables to be the current var plus the returned variable from the other equation
                break  # Breaks the loop
            print(str(truth_value[0]) + ' ' + str([x, truth_value[1][1]]))
        else:  # If there is not a more inner staatemetn
            if statement(in_var, x):  # Tests the passeed in logcial expression
                is_true = True  # if it returns true we have one correct value and can mark the whole thing as true
                prove_vars = [None, x]  # sets the prove_vars to be the current value
                break  # breaks out of the loops
            
        
    return is_true, prove_vars  # returns the the bool and the variables

def twovar_un_qual(domain, statement, in_var, next):
    is_true = True  # Sets the initial value to true, with only one False needed to change it
    prove_vars = []  # Sets the initial list of nums that change is_true

    for x in domain:  # Goes through each num in the domain
        if next is not None:  # Sees if there is a quantifier within this one
            truth_value = next(domain, statement, x, None)  # if there is, get the value of the inner one first
            if not truth_value[0]:  # then check if the value is false
                is_true = False  # if so, one false value flips this one to False
                prove_vars = [x, truth_value[1][1]]  # Keeps track of the numbers that caused the trip from both this function call and the inner one
                break  # breaks out to get the first combo to break it 
            print(str(truth_value[0]) + ' ' + str([x, truth_value[1][1]]))  # Prints each num to show every combination, proving the statement

        else:  # If this is the most inner quantifier
            if not statement(in_var, x):  # Check if the statement is not true using the passed in num
                is_true = False  # if so, it sets the value to false
                prove_vars = [None, x]  # keeps track of just the inner value that tripped it
                break  # breaks out of the loop to just get the inner value

    
    return is_true, prove_vars  # passed back the bool and the important variables

def problem_two():

    print('\n\n\n\nQUESTION 2: \nIf the statement has None for the vars that prove it, you can see the various combonations that cause that to be the case above each.')  # prints for user clarity
    print('\n' + '-' * 15 + '\n')  # prints a nice line for formatting

    proposition = lambda x, y : x * y == 1  # the logical proposition, changing this has major impacts on the logic below

    domain = [1,2,4,5,10,0.5,0.25,0.2,0.1]  # the list of the domain, changing this does change the logical outputs 

    # Part 'a'

    print('2a -> ∀x∀yP(x,y)')  # prints the question
    onevar_nice_output(twovar_un_qual(domain, proposition, None, twovar_un_qual))  # Calls the nice format output, and passes in the quantifier nested within another using hte domain and prop from above
    print('\n' + '-' * 15 + '\n')  # prints a nice line for formatting

    # Part 'b'

    print('2b -> ∀x∃yP(x,y)')  # prints the question
    onevar_nice_output(twovar_un_qual(domain, proposition, None, twovar_ex_qual))  # Calls the nice format output, and passes in the quantifier nested within another using hte domain and prop from above
    print('\n' + '-' * 15 + '\n')  # prints a nice line for formatting

    # Part 'c'

    print('2c -> ∀y∃xP(x,y)')  # prints the question
    onevar_nice_output(twovar_un_qual(domain, proposition, None, twovar_ex_qual))  # Calls the nice format output, and passes in the quantifier nested within another using hte domain and prop from above
    print('\n' + '-' * 15 + '\n')  # prints a nice line for formatting

    # Part 'd'

    print('2d -> ∃x∀yP(x,y)')  # prints the question
    onevar_nice_output(twovar_ex_qual(domain, proposition, None, twovar_un_qual))  # Calls the nice format output, and passes in the quantifier nested within another using hte domain and prop from above
    print('\n' + '-' * 15 + '\n')  # prints a nice line for formatting

    # Part 'e'

    print('2e -> ∃y∀xP(x,y)')  # prints the question
    onevar_nice_output(twovar_ex_qual(domain, proposition, None, twovar_un_qual))  # Calls the nice format output, and passes in the quantifier nested within another using hte domain and prop from above
    print('\n' + '-' * 15 + '\n')  # prints a nice line for formatting

    # Part 'f'

    print('2f -> ∃x∃yP(x,y)')  # prints the question
    onevar_nice_output(twovar_ex_qual(domain, proposition, None, twovar_ex_qual))  # Calls the nice format output, and passes in the quantifier nested within another using hte domain and prop from above
    print('\n' + '-' * 15 + '\n')  # prints a nice line for formatting

def main():
    """The function that calls both problems"""
    problem_one()  # all the code for problem 1
    problem_two()  # all the code for problem 2

main()  # calls main to start the program