import sys
from Instruction import (
    Instruction,
    OpCode,
    read_instruction_list,
)

MAX_REG_NUM = 1000


def main():
    if len(sys.argv) != 3:
        sys.stderr.write("Use of command:\n  run <RISC code file>\n")
        print(sys.argv)
        sys.exit(1)

    # Variables stored here, tinyL supports variables a-e
    Memory = [0] * 6
    RegisterFile = [0] * MAX_REG_NUM
    instrCounter = 0  # counts number of executed instructions

    try:
        head = read_instruction_list(sys.argv[2])
    except IOError as e:
        sys.stderr.write(f'Cannot open input file "{sys.argv[2]}"\n')
        sys.exit(1)

    instr = head
    while instr:
        if instr.opcode == OpCode.LOAD:
            RegisterFile[instr.field1] = Memory[ord(instr.field2) - ord("a")]
        elif instr.opcode == OpCode.LOADI:
            RegisterFile[instr.field1] = instr.field2
        elif instr.opcode == OpCode.STORE:
            Memory[ord(instr.field1) - ord("a")] = RegisterFile[instr.field2]
        elif instr.opcode in [
            OpCode.ADD,
            OpCode.SUB,
            OpCode.MUL,
            OpCode.AND,
            OpCode.OR,
        ]:
            operation = {
                OpCode.ADD: lambda x, y: x + y,
                OpCode.SUB: lambda x, y: x - y,
                OpCode.MUL: lambda x, y: x * y,
                OpCode.AND: lambda x, y: x & y,
                OpCode.OR: lambda x, y: x | y,
            }[instr.opcode]
            RegisterFile[instr.field1] = operation(
                RegisterFile[instr.field2], RegisterFile[instr.field3]
            )
        elif instr.opcode == OpCode.READ:
            input_value = int(input(f'tinyL>> enter value for "{instr.field1}": '))
            Memory[ord(instr.field1) - ord("a")] = input_value
        elif instr.opcode == OpCode.WRITE:
            print(f"tinyL>> {instr.field1} = {Memory[ord(instr.field1) - ord('a')]}")
        else:
            sys.stderr.write("Illegal instructions\n")
            sys.exit(1)

        instrCounter += 1
        instr = instr.next


if __name__ == "__main__":
    main()
