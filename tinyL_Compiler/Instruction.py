from enum import Enum, auto


# Equivalent to the enum declaration in C
class OpCode(Enum):
    LOAD = 1
    LOADI = 2
    STORE = 3
    ADD = 4
    SUB = 5
    MUL = 6
    OR = 7
    AND = 8
    READ = 9
    WRITE = 10


# Equivalent to the struct declaration in C
class Instruction:
    def __init__(
        self,
        opcode,
        field1,
        field2=None,
        field3=None,
        prev=None,
        next=None,
        critical=False,
    ):
        self.opcode = OpCode(opcode)  # Ensure opcode is an instance of OpCode
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3
        self.prev = prev  # Previous Instruction instance
        self.next = next  # Next Instruction instance
        self.critical = critical


def print_instruction(outfile_path: str, instr: Instruction):
    """
    Prints a formatted instruction to a specified output file.

    This function takes an instruction object and an output file object, formatting the instruction
    based on its opcode and fields. It supports different formatting for various instruction types,
    ensuring that the output matches the expected syntax for each instruction. The function handles
    instructions with varying numbers of fields, specifically accommodating instructions that require
    one, two, or three fields.

    Parameters:
    - outfile_path: A path to the file to write to, where the instruction will be printed.
    - instr: An Instruction object containing the opcode and fields necessary for formatting
             the instruction. The Instruction object must have an 'opcode' attribute that corresponds
             to an OpCode enum value, and 'field1', 'field2', and 'field3' attributes for the instruction's fields.
             Instructions may also use 'prev' and 'next' attributes for linked list behavior, although these
             are not used directly by this function.

    Raises:
    - ValueError: If `outfile` is None (indicating a file error) or if an illegal instruction (an unsupported
                  opcode) is encountered.

    Note:
    This implementation assumes the Instruction class and OpCode enum are defined according to the
    provided specifications, with appropriate attributes and enum members.
    """
    with open(outfile_path, mode="a") as outfile:
        if not outfile:
            raise ValueError("File error")
        if instr:
            # Define the instruction format strings with placeholders as needed
            opcode_formats = {
                OpCode.LOAD: "LOAD r{} {}\n",
                OpCode.LOADI: "LOADI r{} #{}\n",
                OpCode.STORE: "STORE {} r{}\n",
                OpCode.ADD: "ADD r{} r{} r{}\n",
                OpCode.SUB: "SUB r{} r{} r{}\n",
                OpCode.MUL: "MUL r{} r{} r{}\n",
                OpCode.READ: "READ {}\n",
                OpCode.WRITE: "WRITE {}\n",
                OpCode.AND: "AND r{} r{} r{}\n",
                OpCode.OR: "OR r{} r{} r{}\n",
            }

            format_string = opcode_formats.get(instr.opcode)
            if not format_string:
                raise ValueError("Illegal instruction")

            # Depending on the instruction, format with the correct number of fields
            if instr.opcode in [OpCode.READ, OpCode.WRITE]:
                # For instructions with a single field
                print(format_string.format(instr.field1), file=outfile, end="")
            elif instr.opcode in [OpCode.LOAD, OpCode.LOADI, OpCode.STORE]:
                # For instructions with two fields
                print(
                    format_string.format(instr.field1, instr.field2),
                    file=outfile,
                    end="",
                )
            else:
                # For instructions with three fields
                print(
                    format_string.format(instr.field1, instr.field2, instr.field3),
                    file=outfile,
                    end="",
                )


def print_instruction_list(file_path, instr):
    """
    Prints a list of instructions to a specified file.

    This function iterates over a linked list of Instruction objects, printing each
    instruction to the file specified by file_path using the print_instruction function.

    Parameters:
    - file_path: The path to the file where the instructions will be printed.
    - instr: The first Instruction object in the linked list of instructions to be printed.

    Raises:
    - ValueError: If the file path is None or empty, or if the instr argument is None (indicating no instructions).
    """
    if not file_path:
        raise ValueError("File error")
    if not instr:
        raise ValueError("No instructions")

    while instr:
        print_instruction(
            file_path, instr
        )  # Assuming print_instruction now accepts a file object again
        instr = instr.next


def parse_instruction_string(line: str) -> Instruction:
    words = line.split()
    if not words:
        return None

    opcode_str = words[0].upper()  # Ensure opcode is uppercase to match OpCode enum
    if opcode_str in [
        "LOAD",
        "LOADI",
        "STORE",
        "ADD",
        "SUB",
        "MUL",
        "AND",
        "OR",
        "READ",
        "WRITE",
    ]:
        if opcode_str == "LOAD":
            # LOAD r%d %c
            reg = int(words[1][1:])  # Skip 'r'
            var = words[2]
            instr = Instruction(OpCode.LOAD, reg, var)
        elif opcode_str == "LOADI":
            # LOADI r%d #%d
            reg = int(words[1][1:])  # Skip 'r'
            imm = int(words[2][1:])  # Skip '#'
            instr = Instruction(OpCode.LOADI, reg, imm)
        elif opcode_str == "STORE":
            # STORE %c r%d
            var = words[1]
            reg = int(words[2][1:])  # Skip 'r'
            instr = Instruction(OpCode.STORE, var, reg)
        elif opcode_str in ["ADD", "SUB", "MUL", "AND", "OR"]:
            # ADD r%d r%d r%d (same format for SUB, MUL, AND, OR)
            reg1 = int(words[1][1:])  # Skip 'r'
            reg2 = int(words[2][1:])  # Skip 'r'
            reg3 = int(words[3][1:])  # Skip 'r'
            instr = Instruction(OpCode[opcode_str], reg1, reg2, reg3)
        elif opcode_str in ["READ", "WRITE"]:
            # READ %c or WRITE %c
            var = words[1]
            instr = Instruction(OpCode[opcode_str], var)
        else:  # Unreachable
            return None
    else:
        # Unknown instruction
        print(f"Unknown Instruction: {opcode_str}")
        return None

    return instr


def read_instruction(infile_path):
    """Reads first instruction from file at infile_path

    Args:
        infile_path (str): path to file to read instruction from

    Raises:
        ValueError: Invalid file (does not exist for reading)

    Returns:
        Instruction: parsed instruction from first line of infile
    """
    instr = None

    try:
        with open(infile_path, "r") as infile:
            line = infile.readline().strip()
            if not line:
                return None
            return parse_instruction_string(line)

    except IOError:
        raise ValueError("File error")


def read_instruction_list(infile_path):
    head = tail = None

    try:
        with open(infile_path, "r") as infile:
            for line in infile:  # Iterate over each line in the file
                line = line.strip()
                if not line:  # Skip empty lines
                    continue
                instr = parse_instruction_string(
                    line
                )  # Parse the instruction from the line
                if not instr:
                    continue  # Skip lines that don't parse into instructions

                if not head:
                    head = tail = (
                        instr  # Initialize the list with the first instruction
                    )
                else:
                    tail.next = instr  # Link the new instruction at the end of the list
                    instr.prev = tail  # Set the previous instruction link
                    tail = instr  # Update the tail to the new last instruction
    except IOError:
        raise ValueError("File error")

    return head
