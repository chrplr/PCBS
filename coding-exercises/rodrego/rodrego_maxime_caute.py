"""
Author: Maxime Cauté
This scripts aims at implementing a RodRego parser,
based on http://proto.atech.tufts.edu/RodRego/ .
This file is the main file.
"""

REGISTERS_AMOUNT = 10
registers = [0]*REGISTERS_AMOUNT

def increment(register_index):
    """
    This function increments (by 1) a given register.
    It is similar to Inc command of RodRego save for the step movement.
    ---
    Input:
        - register_index: int. The index of the register to increment.
    Output:
        - none
    """
    check_register_index(register_index)
    registers[register_index]+=1

def decrement_or_branch(register_index):
    """
    This function decrements (by 1) a given register, if possible,
    and returns if branching is to be done.
    It is similar to Deb command of RodRego save for the step movement.
    ---
    Input:
        - register_index: int. The index of the register to increment.
    Output:
        - branch: bool. Whether branching should occur next.
    """
    check_register_index(register_index)
    if registers[register_index] == 0:
        return True
    registers[register_index]-=1
    return False

def end():
    """
    It is similar to End command of RodRego.
    Also prints registers.
    """
    print("Program ended successfully! Printing registers...")
    print(registers)
    exit()

def get_arguments():
    """
    This function parses command line arguments.
    --
    Output:
        - args: list. The list of the arguments.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("code", type=str,
                        help="The RodRego source code.")
    for i in range(10):
        parser.add_argument("register"+str(i), type=int,
                            help="The content of the register #"+str(i)+".")

    ### optional arguments
    parser.add_argument("-me", "--max_executions", type=int, default=1000,
                        help="The maximum amount of execution before forced stop.")

    args = parser.parse_args()
    return args

def parse_steps(source_code):
    """
    This function parses the input RodRego source code into steps.
    ---
    Input:
        - source_code: string. The RodRego source code, as a string.
    Output:
        - steps: int -> ? list. The dictionnary of the steps, each step associated to its index.
    """
    steps = {}

    source_code_lines = source_code.split("\\n")
    for line in source_code_lines:
        line = line.strip()
        if line == "":
            continue
        tokens = line.split()

        step_index = get_token(0, tokens, is_integer=True)
        step_command = get_token(1, tokens)
        step_register = get_token(2, tokens, is_integer=True, optional = True)
        step_next = get_token(3, tokens, is_integer=True, optional = True)
        step_branch = get_token(4, tokens, is_integer=True, optional = True)


        if step_index in steps:
            raise_parsing_error("Steps "+step_index+" already assigned!")
        steps[step_index] = (step_command, step_register, step_next, step_branch)

    return steps

def get_token(index, tokens, is_integer=False, optional=False):
    """
    Retrieves a token from a token list and checks if fits with what was expected.
    Raises a parsing error if not.
    ---
    Input:
        - index: int. The index of the token to retrieve in the list.
        - tokens: list. The tokens list.
    Parameters:
        - is_integer: bool. Specifies if the token has to be integer-like (positive).
            Defaults to False.
        - optional: bool. Specifies if the token can be absent.
            Defaults to False, i.e. requires its presence.
    Output:
        - token: str or int. The token that was retrieved.
    """
    if len(tokens) <= index:
        if not optional:
            raise_parsing_error("Absent parameter!")
        return -1

    token = tokens[index]
    if is_integer:
        if not token.isdigit():
            raise_parsing_error("Wrong parameter!")
        token = int(token)
    return token



def run(steps, max_executions):
    """
    This function runs a group of steps, starting from step 1 and following the flow.
    --
    Input:
        - steps: step dict. The dictionnary of the steps.
    """
    n_executions = 1
    step_index = 1
    while (n_executions <= max_executions):
        step_index = run_step(steps[step_index])
        n_executions+=1
    raise_runtime_error("Too many executions! "+"Limit is "+max_executions+". "
                        "Stopping to prevent infinite loops. "+
                        "Consider increasing limit with option -me.")


def run_step(step):
    """
    This function runs a single step and returns the next step index.
    ---
    Input:
        - step: string*int*int*int. The command line,
            with the command, the affected register, the next step and the branch.
            Note that the latters may be -1 if there is no such elements required.
    Output:
        - next_step: string*int*int*int. The step to run afterwards. -1 if none.
    """
    command = step[0]
    register = step[1]
    next_step = step[2]
    branch = step[3]

    if command == "INC":
        increment(register)
        return next_step
    if command == "DEB":
        branching = decrement_or_branch(register)
        return branch if branching else next_step
    if command == "END":
        end()
        return -1
    return -1

def raise_parsing_error(message = "", line = 0):
    """
    Raises a parsing error. Also displays a message clarifying it.
    --
    Parameters:
        - message: string. A precision message to display.
            Defaults to none.
        - line: int. The line of the error.
            Defaults to 0.
    """
    print("Parsing error! "+message)
    raise Exception


def raise_runtime_error(message = "", line = 0):
    """
    Raises a runtime error. Also displays a message clarifying it.
    --
    Parameters:
        - message: string. A precision message to display.
            Defaults to none.
        - line: int. The line of the error.
            Defaults to 0.
    """
    print("Runtime error! "+message)
    raise Exception

def check_register_index(register_index):
    """
    Checks the validity of the register index.
    Raises a runtime error if invalide.
    --
    Input:
        - index: int. The register index to check.
    """
    if register_index < 0:
        raise_runtime_error(message="Register index below 0.")
    if register_index >= REGISTERS_AMOUNT:
        raise_runtime_error(message="Register index above "+REGISTERS_AMOUNT+"."+
                                    "There are not as much registers.")

if __name__ == "__main__":
    """
    Upon being executed, interprets a RodRego source code
    Steps are to be separated by a "\n" and named by an integer.
    If several steps have the same name, it raises a parsing error.
    The first step to be run is #1.

    Instructions are as follow:
        - INC i j: increments register i and steps to step j.
        - DEB i j k: decreases register i if possible.
            if it was possible, steps to step j.
            else, branch to step k.
        - END: ends the run.

    Missing arguments will raise a runtime error.
    This could be replaced by a parsing error with a post-parsing check
    (but was not implemented for the sake of simplicity).
    Wrong arguments (e.g. strings instead of integers) will raise a parsing error.

    The program only runs a given number of steps (1000 by default)
    ---
    Call examples:
        python3 rodrego.py "1 INC 0 2 \n 2 END" 1 0 0 0 0 0 0 0 0 0
    """
    import argparse
    import re
    args = get_arguments()

    source_code = args.code
    #No loop due to variable names (might be optimized)
    registers[0]=args.register0
    registers[1]=args.register1
    registers[2]=args.register2
    registers[3]=args.register3
    registers[4]=args.register4
    registers[5]=args.register5
    registers[6]=args.register6
    registers[7]=args.register7
    registers[8]=args.register8
    registers[9]=args.register9
    max_executions = args.max_executions



    # Technically, parse_steps only raises parsing errors,
    # and run only raises runtime errors
    # different exceptions not implemented yet.
    try:
        steps = parse_steps(source_code)
        run(steps, max_executions)
    except Exception as e:
        print("Program ended with an error!")
    print("Finished running python.")
