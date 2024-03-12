import unittest
import os
from Instruction import read_instruction, Instruction, OpCode


class TestReadInstruction(unittest.TestCase):
    def setUp(self):
        # Set up a temporary file for testing
        self.test_file_name = "test_instruction.txt"

    def tearDown(self):
        # Clean up the file after each test
        if os.path.exists(self.test_file_name):
            os.remove(self.test_file_name)

    def write_instruction_to_file(self, instruction_str):
        # Helper method to write an instruction to the file
        with open(self.test_file_name, "w") as file:
            file.write(instruction_str)

    def test_read_load_instruction(self):
        self.write_instruction_to_file("LOAD r1 A")
        instr = read_instruction(self.test_file_name)
        self.assertEqual(instr.opcode, OpCode.LOAD)
        self.assertEqual(instr.field1, 1)
        self.assertEqual(instr.field2, "A")

    def test_read_loadi_instruction(self):
        self.write_instruction_to_file("LOADI r2 #10")
        instr = read_instruction(self.test_file_name)
        self.assertEqual(instr.opcode, OpCode.LOADI)
        self.assertEqual(instr.field1, 2)
        self.assertEqual(instr.field2, 10)

    def test_read_store_instruction(self):
        self.write_instruction_to_file("STORE A r3")
        instr = read_instruction(self.test_file_name)
        self.assertEqual(instr.opcode, OpCode.STORE)
        self.assertEqual(instr.field1, "A")
        self.assertEqual(instr.field2, 3)

    def test_read_add_instruction(self):
        self.write_instruction_to_file("ADD r1 r2 r3")
        instr = read_instruction(self.test_file_name)
        self.assertEqual(instr.opcode, OpCode.ADD)
        self.assertEqual(instr.field1, 1)
        self.assertEqual(instr.field2, 2)
        self.assertEqual(instr.field3, 3)

    def test_read_sub_instruction(self):
        self.write_instruction_to_file("SUB r4 r5 r6")
        instr = read_instruction(self.test_file_name)
        self.assertEqual(instr.opcode, OpCode.SUB)
        self.assertEqual(instr.field1, 4)
        self.assertEqual(instr.field2, 5)
        self.assertEqual(instr.field3, 6)

    def test_read_mul_instruction(self):
        self.write_instruction_to_file("MUL r7 r8 r9")
        instr = read_instruction(self.test_file_name)
        self.assertEqual(instr.opcode, OpCode.MUL)
        self.assertEqual(instr.field1, 7)
        self.assertEqual(instr.field2, 8)
        self.assertEqual(instr.field3, 9)

    def test_read_read_instruction(self):
        self.write_instruction_to_file("READ A")
        instr = read_instruction(self.test_file_name)
        self.assertEqual(instr.opcode, OpCode.READ)
        self.assertEqual(instr.field1, "A")

    def test_read_write_instruction(self):
        self.write_instruction_to_file("WRITE B")
        instr = read_instruction(self.test_file_name)
        self.assertEqual(instr.opcode, OpCode.WRITE)
        self.assertEqual(instr.field1, "B")

    def test_read_and_instruction(self):
        self.write_instruction_to_file("AND r10 r11 r12")
        instr = read_instruction(self.test_file_name)
        self.assertEqual(instr.opcode, OpCode.AND)
        self.assertEqual(instr.field1, 10)
        self.assertEqual(instr.field2, 11)
        self.assertEqual(instr.field3, 12)

    def test_read_or_instruction(self):
        self.write_instruction_to_file("OR r13 r14 r15")
        instr = read_instruction(self.test_file_name)
        self.assertEqual(instr.opcode, OpCode.OR)
        self.assertEqual(instr.field1, 13)
        self.assertEqual(instr.field2, 14)
        self.assertEqual(instr.field3, 15)


if __name__ == "__main__":
    unittest.main()
