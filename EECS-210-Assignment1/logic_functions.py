"""
ASSIGNMENT_NAME: EECS 210 Assignment 1 - Subfile for main.py
FUNCTION: Do the logic behind the varuious truth tables created in main.py
INPUTS: Lit of boolean expressions
OUTPUTS: A single boolean expression
AUTHOR_NAME: Michael Stang
COLLABORATORS: NONE
CREATION_DATE: 08/29/2023
"""

# LOGIC OUTPUTS FOR NUM 1 (aka DE MORGANS FIRST LAW)

def de_morgan_first_o1(log_inputs):  # Takes in a list of Booleans (should be 2 in this case)
    """The first part (output) of proving de morgan's first law using"""
    return (not log_inputs[0]) or (not log_inputs[1])  # returns the logical expression representing !p or !q

def de_morgan_first_o2(log_inputs):
    """The second part (output) of proving de morgan's first law using"""
    return not(log_inputs[0] and log_inputs[1]) # returns the logical expression representing !(p and q)


# LOGIC OUTPUTS FOR NUM 2 (aka DE MORGANS SECOND LAW)

def de_morgan_second_o1(log_inputs):  # Takes in a list of Booleans (should be 2 in this case)
    """The first part (output) of proving de morgan's second law using"""
    return (not log_inputs[0]) and (not log_inputs[1])  # returns the logical expression representing !p and !q


def de_morgan_second_o2(log_inputs):
    """The second part (output) of proving de morgan's second law using"""
    return not(log_inputs[0] or log_inputs[1])  # returns the logical expression representing !(p or q)

# LOGIC OUTPUTS FOR NUM 3 (aka FIRST ASSOCIATIVE LAW)

def associative_first_o1(log_inputs):  # Takes in a list of Booleans (should be 3 in this case)
    """The first part (output) of proving the first associative law using 3 inputs"""
    return (log_inputs[0] and log_inputs[1]) and log_inputs[2]  # returns the logical expression representing (p * q) * r


def associative_first_o2(log_inputs): # Takes in a list of Booleans (should be 3 in this case)
    """The second part (output) of proving the first associative law using 3 inputs"""
    return log_inputs[0] and (log_inputs[1] and log_inputs[2])  # returns the logical expression representing p * (q * r)


# LOGIC OUTPUTS FOR NUM 4 (aka SECOND ASSOCIATIVE LAW)

def associative_second_o1(log_inputs):  # Takes in a list of Booleans (should be 3 in this case)
    """The first part (output) of proving the second associative law using 3 inputs"""
    return (log_inputs[0] or log_inputs[1]) or log_inputs[2]  # returns the logical expression representing (p + q) + r


def associative_second_o2(log_inputs): # Takes in a list of Booleans (should be 3 in this case)
    """The second part (output) of proving the second associative law using 3 inputs"""
    return log_inputs[0] or (log_inputs[1] or log_inputs[2])  # returns the logical expression representing p + (q + r)

# LOGIC OUTPUTS FOR NUM 5

def fifth_o1(log_inputs):
    """The first part (output) of proving [(p ∨ q) ∧ (p → r) ∧ (q → r)] → r ≡ T"""
    # note: -> is also equal to ((not p) or q)
    return (not((log_inputs[0] or log_inputs[1]) and (not(log_inputs[0]) or log_inputs[2]) and (not(log_inputs[1]) or log_inputs[2])) or log_inputs[2])  # returns the logical expression representing [(p ∨ q) ∧ (p → r) ∧ (q → r)] → r

def fifth_o2(log_inputs):
    """The second part (output) of proving [(p ∨ q) ∧ (p → r) ∧ (q → r)] → r ≡ T. This will always be true"""
    return True  # Always returns True

# LOGIC OUTPUTS FOR NUM 6

def sixth_o1(log_inputs):
    """The first part (output) of proving p ↔ q ≡ (p → q) ∧ (q → p)"""
    # note: <-> in two vars is equal to ((p and q) or (not p and not q))
    return ((log_inputs[0] and log_inputs[1]) or (not(log_inputs[0]) and not(log_inputs[1])))  # returns the logical expression representing p ↔ q

def sixth_o2(log_inputs):
    """The second part (output) of proving p ↔ q ≡ (p → q) ∧ (q → p)"""
    return (not(log_inputs[0]) or log_inputs[1]) and (not(log_inputs[1]) or log_inputs[0])  # returns the logical expression representing (p → q) ∧ (q → p)