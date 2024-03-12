import os
import unittest
from Instruction import print_instruction_list, Instruction, OpCode


class InstructionListTests(unittest.TestCase):
    def setUp(self):
        self.test_file_path = "test_instruction_list.txt"
        # Ensure the file is empty before each test
        open(self.test_file_path, "w").close()

    def tearDown(self):
        # Remove the test file after each test
        os.remove(self.test_file_path)

    def create_instruction_list(self):
        # Helper function to create a linked list of instructions
        instr1 = Instruction(OpCode.LOAD, 1, "A", 0)
        instr2 = Instruction(OpCode.ADD, 1, 2, 3)
        instr1.next = instr2  # Link instructions
        return instr1

    def test_print_empty_instruction_list(self):
        with self.assertRaises(ValueError):
            print_instruction_list(self.test_file_path, None)

    def test_print_single_instruction(self):
        instr = Instruction(OpCode.LOAD, 1, "A", 0)
        print_instruction_list(self.test_file_path, instr)
        with open(self.test_file_path, "r") as f:
            content = f.read().strip()
        expected_output = "LOAD r1 A"  # Adjust based on your format
        self.assertEqual(content, expected_output)

    def test_print_multiple_instructions(self):
        instr1 = self.create_instruction_list()  # Create a list of instructions
        print_instruction_list(self.test_file_path, instr1)
        with open(self.test_file_path, "r") as f:
            content = f.read().strip().split("\n")
        expected_output = ["LOAD r1 A", "ADD r1 r2 r3"]  # Adjust based on your format
        self.assertEqual(content, expected_output)


if __name__ == "__main__":
    unittest.main()
