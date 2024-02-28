"""
ASSIGNMENT_NAME: EECS 210 Assignment 8
FUNCTION: Prints various relations and functions along with GCDs and coefficients
INPUTS: NONE
OUTPUTS: Various relation's functionality, and GCDs and coefficients
AUTHOR_NAME: Michael Stang
COLLABORATORS: ChatGPT helped a bit comprehension of Problem Three
CREATION_DATE: 12/07/2023
"""


import nim

def print_circuit(circuit):
    """Prints a circuit with nice formatting"""

    for i in range(len(circuit)):  # Goes through each index of the list
        if i == 0:  # If it's the first index
            print(circuit[i], end='')  # Prints without the arrow
        else:  # Otherwise, if it's not the first index
            print(" -> " + circuit[i], end='')  # Prints with the arrow


def is_euler_circuit(graph):
    """Return whether or not a given graph has a euler circuit and if not, what verticies disqualify it"""

    is_circuit = True  # Variable to hold whether or not the graph is a circuit
    odd_verticies = []  # Variable to hold the verticies that disqualify the graph

    for vertex in graph:  # Loops through each vertex
        if len(graph[vertex]) % 2 == 1:  # If the length (edges) connetected to the vertex are odd
            is_circuit = False  # Mark the whole thing as false
            odd_verticies.append(vertex)  # Add it to the list of verticies that disqualify it
    
    return is_circuit, odd_verticies  # Return the boolean of circuit-ness and what verticies disqualify

def find_euler_circuit(graph):
    """Find an Euler circuit of a given graph"""

    def remove_edge(H, v1, v2):
        """Remove an edge from the graph"""
        H[v1].remove(v2)  # Removes the 2nd vertex from the first
        H[v2].remove(v1)  # Removes the 1st vertext from the second

    # Start with the first vertex in the graph's keys
    start_vertex = list(graph.keys())[0]  # Gets the first vertex in the graph
    graph_copy = graph.copy()  # Make a copy of G
    circuit = [start_vertex]  # List that holds the final order of the verticies

    while True:  # Loops until done removing eges
        # Find the first vertex in the circuit with remaining adjacent vertices
        v = None  # Sets the initial value for v
        for vertex in circuit:  # Goes through each vertex already in the circuit
            if graph_copy[vertex]:  # Checks if the edges are not empty at the given vertex
                v = vertex  # Sets the current vertex to 'v' (a more permanent variable)
                break
        if v is None:  # If v did not get reset from the loop above we must be done and can break out of the while
            # No vertices with remaining adjacent vertices, break the loop
            break  # Breaks out of the while

        # Find a new circuit starting from v
        subcircuit = [v]  # A list to hold a temporary subcircuit
        while True:  # Loops until break
            w = graph_copy[v][0]  # Gets the first vertex connected to the current one we are looking at
            remove_edge(graph_copy, v, w)  # Removes the edge between the current vertex and its first connection
            v = w  # Marks the vertex we just went to as our current vertex
            subcircuit.append(v)  # Adds the vertex we were at to our "path"
            if v == subcircuit[0]:  # Checks if we are back at the beginning (if the loop has completed)
                break  # If so, breaks

        # Find the index of v in the circuit and insert the new circuit
        index = circuit.index(subcircuit[0])  # Figures out where our mini circuit is
        circuit = circuit[:index] + subcircuit + circuit[index + 1:]  # Adds the temporary subcircuit to the final answer

    return circuit  # Returns the final circuit

def dirac_theorem(graph):
    """Take in a graph and return TRUE or FALSE depending on whether or not it is a hamilton circuit"""
    is_hamilton = True  # Variable that will keep track if any conditions have NOT been met, default is True
    verticies = list(graph.keys())  # Gets a list of verticies from the graph
    vertex_number = len(verticies)  # Counts the number of verticies
    
    if vertex_number < 3:  # If the graph does not meet the requirement of n>=3
        is_hamilton = False  # Then it is false and we end there
    else:  # Otherwise
        for vertex in verticies: # We loop through each vertex
            if len(graph[vertex]) < (vertex_number/2):  # And see if the number of edges is greater than n/2
                is_hamilton = False  # If not, we say its false
                break  # And break to save compute power
    
    return is_hamilton  # returns the final value


def question_one():
    """Do everything for question 1"""

    print("-" * 10 + "\nQUESTION 1\n" + "-" * 10)  # Print header
    # Part A
    print('\nPART A')  # Label for this part of the question

    g1_graph = {'a': ['b', 'e'], 'b': ['a', 'e'], 'c': ['d', 'e'], 'd': ['c', 'e'], 'e': ['a', 'b', 'c', 'd']}  # Declaration for g1 as a dictonary of verticies
    g2_graph = {'a': ['b', 'd', 'e'], 'b': ['a', 'c', 'e'], 'c': ['b', 'd', 'e'], 'd': ['c', 'd', 'e'], 'e': ['a', 'b', 'c', 'd']} # Declaration for g2 as a dictonary of verticies
    g3_graph = {'a': ['b', 'c', 'd'], 'b': ['a', 'd', 'e'], 'c': ['a', 'd'], 'd': ['a', 'b', 'c', 'e'], 'e': ['b', 'd']} # Declaration for g3 as a dictonary of verticies
    
    # G1
    print("\nG1 Euler: ")  # Prints header
    euler_test, euler_invalid = is_euler_circuit(g1_graph)  # Gets whether or not it is a euler circuit (and if not, what verticies disqualify it)
    if euler_test:  # If it is a circuit
        print_circuit(find_euler_circuit(g1_graph))  # Prints the circuit
    else:  # If it's NOT a circuit
        print("NOT A EULER CIRCUIT\nInvalid Verticies: ", end='')  # Print that
        for item in euler_invalid:  # Go through each vertex that disqualifys it
            print(item + " ", end='')  # Prints it

    # G2
    print("\n\nG2 Euler: ")  # Prints header
    euler_test, euler_invalid = is_euler_circuit(g2_graph)  # Gets whether or not it is a euler circuit (and if not, what verticies disqualify it)
    if euler_test:  # If it is a circuit
        print_circuit(find_euler_circuit(g2_graph))  # Prints the circuit
    else:  # If it's NOT a circuit
        print("NOT A EULER CIRCUIT\nInvalid Verticies: ", end='')  # Print that
        for item in euler_invalid:  # Go through each vertex that disqualifys it
            print(item + " ", end='')  # Prints it
    
    # G3
    print("\n\nG3 Euler: ")  # Prints header
    euler_test, euler_invalid = is_euler_circuit(g3_graph)  # Gets whether or not it is a euler circuit (and if not, what verticies disqualify it)
    if euler_test:  # If it is a circuit
        print_circuit(find_euler_circuit(g3_graph))  # Prints the circuit
    else:  # If it's NOT a circuit
        print("NOT A EULER CIRCUIT\nInvalid Verticies: ", end='')  # Print that
        for item in euler_invalid:  # Go through each vertex that disqualifys it
            print(item + " ", end='')  # Prints it

    # Part B
    print('\n\n\nPART B')  # Label for the part of the question

    given_graph = {  # This is the graph given, broken up onto multiple lines to make it easier to read. Each line represents a vertex
    'a': ['b', 'd'],  # 'a' vertex
    'b': ['a', 'c', 'e', 'd'],  # 'b' vertex
    'c': ['b', 'f'],  # 'c' vertex
    'd': ['a', 'b', 'e', 'g'],  # 'd' vertex
    'e': ['b', 'd', 'h', 'f'],  # 'e' vertex
    'f': ['c', 'e', 'h', 'i'],  # 'f' vertex
    'g': ['d', 'h'],  # 'g' vertex
    'h': ['f', 'e', 'g', 'i'],  # 'h' vertex
    'i': ['f', 'h']  # 'i' vertex
    }

    print("\nGiven Graph: ")  # Prints header
    euler_test, euler_invalid = is_euler_circuit(given_graph)  # Gets whether or not it is a euler circuit (and if not, what verticies disqualify it)
    if euler_test:  # If it is a circuit
        print_circuit(find_euler_circuit(given_graph))  # Prints the circuit
    else:  # If it's NOT a circuit
        print("NOT A EULER CIRCUIT\nInvalid Verticies: ", end='')  # Print that
        for item in euler_invalid:  # Go through each vertex that disqualifys it
            print(item + " ", end='')  # Prints it


def per_graph_question_two(graph):
    """Takes in a graph for question 2 and handles calculations and output"""
    valid = dirac_theorem(graph)  # Gets calculations from is_hamilton()
    if valid:  # If it is a hamilton
        print("GRAPH IS A HAMILTON CIRCUIT")  # Print that to the user
    else:  # Otherwise,
        print("GRAPH IS NOT NECESSARILY A HAMILTON CIRCUIT")  # Print that hamilton's theorem doesn't guarentee there is not, just says there might not


def question_two():
    """Do everything for question 2"""
    print("\n\n" + "-" * 10 + "\nQUESTION 2\n" + "-" * 10)  # Print header
    # Part A
    print('\nPART A')  # Label for this part of the question


    g1_graph = {  # This is the graph given, broken up onto multiple lines to make it easier to read. Each line represents a vertex
    'a': ['b', 'e', 'c'],  # 'a' vertex
    'b': ['a', 'e', 'c'],  # 'b' vertex
    'c': ['e', 'a', 'b', 'd'],  # 'c' vertex
    'd': ['e', 'c'],  # 'd' vertex
    'e': ['a', 'b', 'c', 'd']  # 'e' vertex
    }

    g2_graph = {  # This is the graph given, broken up onto multiple lines to make it easier to read. Each line represents a vertex
    'a': ['b'],  # 'a' vertex
    'b': ['a', 'd', 'c'],  # 'b' vertex
    'c': ['d', 'b'],  # 'c' vertex
    'd': ['b', 'c']  # 'd' vertex
    }

    g3_graph = {  # This is the graph given, broken up onto multiple lines to make it easier to read. Each line represents a vertex
    'a': ['b'],  # 'a' vertex
    'b': ['a', 'c', 'g'],  # 'b' vertex
    'c': ['d', 'b', 'e'],  # 'c' vertex
    'd': ['c'],  # 'd' vertex
    'e': ['c', 'g', 'f'],  # 'e' vertex
    'f': ['e'],  # 'f' vertex
    'g': ['b', 'e']  # 'g' vertex
    }

    print("\nG1 DIRAC: ")  # Prints header
    per_graph_question_two(g1_graph)  # Handles output and calculations for G1
    print('')  # Prints line for formatting

    print("\nG2 DIRAC: ")  # Prints header
    per_graph_question_two(g2_graph)  # Handles output and calculations for G2
    print('')  # Prints line for formatting

    print("\nG3 DIRAC: ")  # Prints header
    per_graph_question_two(g3_graph)  # Handles output and calculations for G3
    print('')  # Prints line for formatting

    # Part A
    print('\nPART B\n')  # Label for this part of the question

    example_graph = {  # This is the graph given, broken up onto multiple lines to make it easier to read. Each line represents a vertex
    'a': ['b', 'c'],  # 'a' vertex
    'b': ['a', 'c'],  # 'b' vertex
    'c': ['a', 'b', 'f'],  # 'c' vertex
    'd': ['f', 'e'],  # 'd' vertex
    'e': ['f', 'd'],  # 'e' vertex
    'f': ['c', 'd', 'e'],  # 'f' vertex
    }

    print("PROVIDED GRAPH DIRAC: ")  # Prints header
    per_graph_question_two(example_graph)  # Handles output and calculations for the provided graph 
    print('')  # Prints line for formatting


def ores_theorem(graph):
    """Take in a graph and return TRUE or FALSE depending on whether or not it is a hamilton circuit based on Ores Theorem"""
    is_hamilton = True  # Variable that will keep track if any conditions have NOT been met, default is True
    verticies = list(graph.keys())  # Gets a list of verticies from the graph
    vertex_number = len(verticies)  # Counts the number of verticies

    if vertex_number < 3:  # If the graph does not meet the requirement of n>=3
        is_hamilton = False  # Then it is false and we end there
    else:  # Otherwise
        for vertex_a in verticies:  # Goes through each vertex
            for vertex_b in verticies:  # For each vertex, goes through each vertex
                if (vertex_b != vertex_a) and (vertex_b not in graph[vertex_a]):  # If the current vertex in the inner iteration is not the main vertex or connected to the main vertex
                    deg_sum = len(graph[vertex_a]) + len(graph[vertex_b])  # Calculates deg(u) + deg(v)
                    if deg_sum < vertex_number:  # If deg(u) + deg(v) < n
                        is_hamilton = False  # then it is false, otherwise, we go to the next vertex
                        #print(vertex_a, vertex_b)
    
    return is_hamilton  # Returns a boolean


def per_graph_question_three(graph):
    """Takes in a graph for question 2 and handles calculations and output"""
    valid = ores_theorem(graph)  # Gets calculations from is_hamilton()
    if valid:  # If it is a hamilton
        print("GRAPH IS A HAMILTON CIRCUIT")  # Print that to the user
    else:  # Otherwise,
        print("GRAPH IS NOT NECESSARILY A HAMILTON CIRCUIT")  # Print that hamilton's theorem doesn't guarentee there is not, just says there might not


def question_three():
    """Do everything for question 3"""
    print("\n\n" + "-" * 10 + "\nQUESTION 3\n" + "-" * 10)  # Print header
    # Part A
    print('\nPART A')  # Label for this part of the question

    g1_graph = {  # This is the graph given, broken up onto multiple lines to make it easier to read. Each line represents a vertex
    'a': ['b', 'e', 'c'],  # 'a' vertex
    'b': ['a', 'e', 'c'],  # 'b' vertex
    'c': ['e', 'a', 'b', 'd'],  # 'c' vertex
    'd': ['e', 'c'],  # 'd' vertex
    'e': ['a', 'b', 'c', 'd']  # 'e' vertex
    }

    g2_graph = {  # This is the graph given, broken up onto multiple lines to make it easier to read. Each line represents a vertex
    'a': ['b'],  # 'a' vertex
    'b': ['a', 'd', 'c'],  # 'b' vertex
    'c': ['d', 'b'],  # 'c' vertex
    'd': ['b', 'c']  # 'd' vertex
    }

    g3_graph = {  # This is the graph given, broken up onto multiple lines to make it easier to read. Each line represents a vertex
    'a': ['b'],  # 'a' vertex
    'b': ['a', 'c', 'g'],  # 'b' vertex
    'c': ['d', 'b', 'e'],  # 'c' vertex
    'd': ['c'],  # 'd' vertex
    'e': ['c', 'g', 'f'],  # 'e' vertex
    'f': ['e'],  # 'f' vertex
    'g': ['b', 'e']  # 'g' vertex
    }

    print("\nG1 ORES: ")  # Prints header
    per_graph_question_three(g1_graph)  # Handles output and calculations for G1
    print('')  # Prints line for formatting

    print("\nG2 ORES: ")  # Prints header
    per_graph_question_three(g2_graph)  # Handles output and calculations for G2
    print('')  # Prints line for formatting

    print("\nG3 ORES: ")  # Prints header
    per_graph_question_three(g3_graph)  # Handles output and calculations for G3
    print('')  # Prints line for formatting

        # Part A
    print('\nPART B\n')  # Label for this part of the question

    example_graph = {  # This is the graph given, broken up onto multiple lines to make it easier to read. Each line represents a vertex
    'a': ['b', 'c'],  # 'a' vertex
    'b': ['a', 'c'],  # 'b' vertex
    'c': ['a', 'b', 'f'],  # 'c' vertex
    'd': ['f', 'e'],  # 'd' vertex
    'e': ['f', 'd'],  # 'e' vertex
    'f': ['c', 'd', 'e'],  # 'f' vertex
    }

    print("PROVIDED GRAPH ORES: ")  # Prints header
    per_graph_question_three(example_graph)  # Handles output and calculations for the provided graph 
    print('')  # Prints line for formatting




def question_four():
    """Do everything for question 4"""
    simulation_1_score = 0  # Variable that will hold onto player 1 (minmax's) score
    simulation_2_score = 0  # Variable that will hold onto player 2 (random's) score
    for i in range(100):  # Loops 100 times
        winner = nim.start_game(nim.generate_board(), "minmax", "random")
        if winner == 1:  # If player one wins
            simulation_1_score += 1  # Increase player 1s score
        else:  # Otherwise,
            simulation_2_score += 1  # Increase player 2s score

    print(f"PLAYER 1 WON {simulation_1_score} TIMES AND PLAYER 2 WON {simulation_2_score} TIMES")


def main():
    """Run the program"""
    question_one()  # Runs the code for question 1
    question_two()  # Runs the code for question 2
    question_three()  # Runs the code for question 3
    question_four()  # Runs the code for question 4

main()