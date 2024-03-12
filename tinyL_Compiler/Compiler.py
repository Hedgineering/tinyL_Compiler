import sys
from Instruction import Instruction, OpCode, print_instruction


def current_func_name(n: int = 0):
    """
    Gets the name of a function from the call stack

    Keyword Arguments:

    n -- 0 for current func name, 1 for caller of this func, 2 for caller of caller, etc.
    """
    sys._getframe(n + 1).f_code.co_name


# ========
# Globals
# ========

# Note: I know global variables are bad practice in
# general, but I'm doing this to mirror the scaffolding
# given for the project in the C implementation
regnum = 0
content = None
token, token_idx = None, None
outfile = None

# =========
# Utilities
# =========


def error(msg: str):
    raise Exception(msg)


def next_register():
    # this declares that regnum should reference global
    # regnum identifier
    global regnum
    regnum += 1
    return regnum


def is_digit(c: str):
    return c in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def to_digit(c: str) -> int:
    if not is_digit(c):
        error(f"Non-digit passed to {current_func_name()}")
    return int(c)


def is_identifier(c: str):
    return c in ["a", "b", "c", "d", "e", "f"]


def read_input(filepath):
    global token, token_idx, content
    file = open(filepath, "r")
    content = file.read()
    token = content[0]
    token_idx = 0
    file.close()
    return content.strip()


def next_token():
    global token, token_idx, content
    if content is None or token is None or token_idx is None:
        error("No content to parse, content is None")
    token_idx += 1
    token = content[token_idx]


def code_gen(opcode: OpCode, field1, field2=None, field3=None):
    instr = Instruction(opcode, field1, field2, field3)

    if outfile is None:
        error("File Error: Outfile is None")
        sys.exit(1)

    print_instruction(outfile, instr)


# ======================================================
# Mutually Recursive Helpers for LL(1) Recursive Descent
# ======================================================
def digit():
    global token
    reg = next_register()
    code_gen(OpCode.LOADI, reg, token)
    next_token()
    return reg


def variable():
    global token
    reg = next_register()
    code_gen(OpCode.LOAD, reg, token)
    next_token()
    return reg


def expr():
    global token
    reg, left_reg, right_reg = None, None, None

    if token == '+':
        next_token()
        left_reg = expr()
        right_reg = expr()
        reg = next_register()
        code_gen(OpCode.ADD, reg, left_reg, right_reg)
        return reg
    elif token == '-':
        next_token()
        left_reg = expr()
        right_reg = expr()
        reg = next_register()
        code_gen(OpCode.SUB, reg, left_reg, right_reg)
        return reg
    elif token == '*':
        next_token()
        left_reg = expr()
        right_reg = expr()
        reg = next_register()
        code_gen(OpCode.MUL, reg, left_reg, right_reg)
        return reg
    elif token == '&':
        next_token()
        left_reg = expr()
        right_reg = expr()
        reg = next_register()
        code_gen(OpCode.AND, reg, left_reg, right_reg)
        return reg
    elif token == '|':
        next_token()
        left_reg = expr()
        right_reg = expr()
        reg = next_register()
        code_gen(OpCode.OR, reg, left_reg, right_reg)
        return reg
    elif is_digit(token):
        return digit()
    elif is_identifier(token):
        return variable()
    else:
        error(f"Symbol {token} unknown")
        sys.exit(1)


def assign():
    global token
    identifier = token

    next_token() # skip identifier

    if token != '=':
        error(f"Symbol {token} unknown")
        sys.exit(1)
    
    next_token() # skip =

    expr_result_reg = expr()
    code_gen(OpCode.STORE, identifier, expr_result_reg)


def read():
    global token
    next_token() # skip ?
    identifier = token
    code_gen(OpCode.READ, identifier)
    next_token() # skip identifier


def tinyL_print():
    global token
    next_token() # skip %
    identifier = token
    code_gen(OpCode.WRITE, identifier)
    next_token() # skip identifier


def stmt():
    global token
    if is_identifier(token):
        assign()
    elif token == '?':
        read()
    elif token == '%':
        tinyL_print()


def morestmts():
    global token
    if token == ';':
        next_token()
        stmtlist()
    elif token == '!':
        next_token()
    else:
        error(f"Program error.  Current input symbol is {token}")
        sys.exit(1)


def stmtlist():
    global token
    if is_identifier(token) or token in ['?', '%']:
        stmt()
        morestmts()
    else:
        error(f"Program error.  Current input symbol is {token}")
        sys.exit(1)


def program():
    global token
    if is_identifier(token) or token in ['?', '%']:
        stmtlist()
    else:
        error(f"Program error.  Current input symbol is {token}")
        sys.exit(1)

    # if token != "!":
    #     error(f"Program error.  Current input symbol is {token}")
    #     sys.exit(1)


# =============
# Main function
# =============
def main() -> int:
    # Populate global outfile path
    global outfile
    outfile = "tinyL.out"

    print("------------------------------------------------")
    print("CS314 compiler for tinyL")
    print("------------------------------------------------")

    if len(sys.argv) != 3:
        sys.stderr.write("Use of command:\n  compile <tinyL file>\n")
        sys.exit(1)

    # Populate globals content and token
    infile = sys.argv[2]
    read_input(infile)

    program()

    print(f'\nCode written to file "{outfile}".\n')

    return 0


if __name__ == "__main__":
    sys.exit(main())
