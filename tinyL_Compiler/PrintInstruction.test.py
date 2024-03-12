import os
import unittest
from Instruction import Instruction, OpCode, print_instruction


class RunPrintInstructionUnitTests(unittest.TestCase):
    def __init__(self, methodName: str = "RunPrintInstructionUnitTests") -> None:
        super().__init__(methodName)

    def setUp(self):
        # Setup runs before each test method
        self.test_file_path = "test_instructions.txt"
        # Clear the file content before each test
        open(self.test_file_path, "w").close()

    def tearDown(self):
        # Clean up runs after each test method
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_print_load_instruction(self):
        instr = Instruction(OpCode.LOAD, 1, "A")
        print_instruction(self.test_file_path, instr)
        with open(self.test_file_path, "r") as f:
            content = f.read().strip()
        self.assertEqual(content, "LOAD r1 A")

    def test_print_loadi_instruction(self):
        instr = Instruction(OpCode.LOADI, 1, 2, 0)
        print_instruction(self.test_file_path, instr)
        with open(self.test_file_path, "r") as f:
            content = f.read().strip()
        self.assertEqual(content, "LOADI r1 #2")

    def test_print_store_instruction(self):
        instr = Instruction(OpCode.STORE, "A", 1, 0)
        print_instruction(self.test_file_path, instr)
        with open(self.test_file_path, "r") as f:
            content = f.read().strip()
        self.assertEqual(content, "STORE A r1")

    def test_print_add_instruction(self):
        instr = Instruction(OpCode.ADD, 1, 2, 3)
        print_instruction(self.test_file_path, instr)
        with open(self.test_file_path, "r") as f:
            content = f.read().strip()
        self.assertEqual(content, "ADD r1 r2 r3")

    def test_print_sub_instruction(self):
        instr = Instruction(OpCode.SUB, 1, 2, 3)
        print_instruction(self.test_file_path, instr)
        with open(self.test_file_path, "r") as f:
            content = f.read().strip()
        self.assertEqual(content, "SUB r1 r2 r3")

    def test_print_mul_instruction(self):
        instr = Instruction(OpCode.MUL, 1, 2, 3)
        print_instruction(self.test_file_path, instr)
        with open(self.test_file_path, "r") as f:
            content = f.read().strip()
        self.assertEqual(content, "MUL r1 r2 r3")

    def test_print_read_instruction(self):
        instr = Instruction(OpCode.READ, "A", 0, 0)
        print_instruction(self.test_file_path, instr)
        with open(self.test_file_path, "r") as f:
            content = f.read().strip()
        self.assertEqual(content, "READ A")

    def test_print_write_instruction(self):
        instr = Instruction(OpCode.WRITE, "A", 0, 0)
        print_instruction(self.test_file_path, instr)
        with open(self.test_file_path, "r") as f:
            content = f.read().strip()
        self.assertEqual(content, "WRITE A")

    def test_print_and_instruction(self):
        instr = Instruction(OpCode.AND, 1, 2, 3)
        print_instruction(self.test_file_path, instr)
        with open(self.test_file_path, "r") as f:
            content = f.read().strip()
        self.assertEqual(content, "AND r1 r2 r3")

    def test_print_or_instruction(self):
        instr = Instruction(OpCode.OR, 1, 2, 3)
        print_instruction(self.test_file_path, instr)
        with open(self.test_file_path, "r") as f:
            content = f.read().strip()
        self.assertEqual(content, "OR r1 r2 r3")

    def test_illegal_instruction(self):
        # This depends on how you handle illegal instructions
        # Here, I assume an exception is raised for an illegal opcode
        with self.assertRaises(ValueError):
            instr = Instruction(None, 0, 0, 0)  # This should raise Value Error
            print_instruction(self.test_file_path, instr)

    def test_file_not_found(self):
        # This test assumes print_instruction raises an exception if the file cannot be opened
        non_existent_path = "/nonexistentdir/test.txt"
        instr = Instruction(OpCode.WRITE, "B", 0, 0)
        with self.assertRaises(
            Exception
        ):  # Replace Exception with the specific exception type you are raising
            print_instruction(non_existent_path, instr)


if __name__ == "__main__":
    unittest.main()
