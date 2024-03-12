import unittest
import os
from Instruction import read_instruction_list, Instruction, OpCode


class TestReadInstructionList(unittest.TestCase):
    def setUp(self):
        # Setup a temporary file for testing
        self.test_file_name = "test_instruction_list.txt"

    def tearDown(self):
        # Clean up the file after each test
        os.remove(self.test_file_name)

    def write_instructions_to_file(self, instructions):
        # Helper method to write multiple instructions to the file
        with open(self.test_file_name, "w") as file:
            for instruction in instructions:
                file.write(instruction + "\n")
        print("finished writing instructions")

    def test_read_single_instruction_load(self):
        # Example instruction: LOAD r1 A
        instruction_line = "LOAD r1 A"
        expected_opcode = OpCode.LOAD
        expected_field1 = 1
        expected_field2 = "A"
        expected_field3 = None  # Assuming LOAD does not use field3

        # Write the single instruction to the file
        self.write_instructions_to_file([instruction_line])

        # Read the instruction list, which should contain only this one instruction
        head = read_instruction_list(self.test_file_name)

        # Verify that the instruction is correctly parsed
        self.assertIsNotNone(head, "Instruction should not be None")
        self.assertEqual(head.opcode, expected_opcode, "Opcode mismatch")
        self.assertEqual(head.field1, expected_field1, "Field1 mismatch")
        self.assertEqual(head.field2, expected_field2, "Field2 mismatch")
        self.assertEqual(
            head.field3, expected_field3, "Field3 should be None for LOAD instruction"
        )
        self.assertIsNone(head.next, "Next should be None for a single instruction")
        self.assertIsNone(head.prev, "Prev should be None for a single instruction")

    def test_read_multiple_instructions(self):
        # Instruction lines and their expected parsed values
        instructions = [
            ("LOAD r1 A", OpCode.LOAD, 1, "A", None),
            ("LOADI r2 #10", OpCode.LOADI, 2, 10, None),
            ("STORE A r3", OpCode.STORE, "A", 3, None),
            ("ADD r4 r5 r6", OpCode.ADD, 4, 5, 6),
            ("WRITE B", OpCode.WRITE, "B", None, None),
        ]
        # Write the instructions to the file, only the instruction text part
        self.write_instructions_to_file([inst[0] for inst in instructions])

        head = read_instruction_list(self.test_file_name)

        # Verify that each instruction is correctly parsed
        current = head
        for i, (
            instruction_text,
            expected_opcode,
            expected_field1,
            expected_field2,
            expected_field3,
        ) in enumerate(instructions, start=1):
            self.assertIsNotNone(
                current, f"Instruction {i} ({instruction_text}) should not be None"
            )
            self.assertEqual(
                current.opcode, expected_opcode, f"Instruction {i} opcode mismatch"
            )
            self.assertEqual(
                current.field1, expected_field1, f"Instruction {i} field1 mismatch"
            )
            self.assertEqual(
                current.field2, expected_field2, f"Instruction {i} field2 mismatch"
            )
            self.assertEqual(
                current.field3, expected_field3, f"Instruction {i} field3 mismatch"
            )

            if current.next:
                self.assertEqual(
                    current.next.prev,
                    current,
                    f"Instruction {i+1} prev should link back to instruction {i}",
                )
            else:
                self.assertIsNone(current.next, "Last instruction should have no next")
            current = current.next


def last_instruction(instr):
    """Gets the reference to the last instruction in the Instructions linked list

    Args:
        instr (Instruction): head of Instructions linked list

    Raises:
        ValueError: No instructions found (head was None or empty)

    Returns:
        Instruction: reference to last instruction in Instructions linked list
    """
    if not instr:
        raise ValueError("No instructions")

    while instr.next:
        instr = instr.next

    return instr


if __name__ == "__main__":
    unittest.main()
