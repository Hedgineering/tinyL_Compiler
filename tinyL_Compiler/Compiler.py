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
regnum = 1
content = None
token, token_idx = None, None


def error(msg: str):
    raise Exception(msg)


def next_register():
    # this declares that regnum should reference global
    # regnum identifier
    global regnum
    regnum += 1


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
    if content == None or token == None or token_idx == None:
        error("No content to parse, content is None")
    token_idx += 1
    token = content[token_idx]
