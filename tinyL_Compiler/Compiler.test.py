import Compiler
import unittest


class RunCompilerUnitTests(unittest.TestCase):
    def __init__(self, methodName: str = "RunCompilerUnitTests") -> None:
        super().__init__(methodName)
        self.invalid_digits = [-5, -3, 10, 11, 35]
        self.valid_identifiers = "abcdef"
        self.invalid_identifiers = "ghijklmnopqrstuvwxyz"

    def test_is_identifier(self):
        for c in self.valid_identifiers:
            self.assertTrue(
                Compiler.is_identifier(c),
                msg=f"is_identifier({c}) should be True, but it returned False",
            )

        for c in self.invalid_identifiers:
            self.assertFalse(
                Compiler.is_identifier(c),
                msg=f"is_identifier({c}) should be False, but it returned True",
            )

        # Couple other edge cases
        for c in ["ab", "cd", "1", "2", "efg"]:
            self.assertFalse(
                Compiler.is_identifier(c),
                msg=f"is_identifier({c}) should be False, but it returned True",
            )

    def test_is_digit(self):
        for i in range(10):
            self.assertTrue(
                Compiler.is_digit(str(i)),
                msg=f"is_digit({i}) should be True, but it returned False",
            )

        for i in self.invalid_digits:
            self.assertFalse(
                Compiler.is_digit(str(i)),
                msg=f"is_digit({i}) should be False, but it returned True",
            )

    def test_to_digit(self):
        for i in range(10):
            result = Compiler.to_digit(str(i))
            self.assertEqual(
                result, i, msg=f"to_digit({i}) should be {i}, but it returned {result}"
            )

        for i in self.invalid_digits:
            with self.assertRaises(
                Exception, msg=f"to_digit({i}) should throw but it did not"
            ):
                Compiler.to_digit(str(i))

    def test_next_register(self):
        self.assertEqual(Compiler.regnum, 1, msg=f"regnum should begin at 1")
        for i in range(1, 100):
            Compiler.next_register()
            self.assertEqual(
                Compiler.regnum,
                i + 1,
                msg=f"regnum should be {i+1} but was {Compiler.regnum}",
            )

    def test_read_input(self):
        expected = "?f;?a;?c;c=*ac;b=*a4;a=*3+ab;%f;%a!"
        actual = Compiler.read_input("./tinyL_tests/comp01.tinyL")
        self.assertEqual(actual, expected)

    def test_next_token(self):
        expected = "?f;?a;?c;c=*ac;b=*a4;a=*3+ab;%f;%a!"
        Compiler.read_input("./tinyL_tests/comp01.tinyL")
        for i, c in enumerate(expected):
            self.assertEqual(
                Compiler.token, c, msg=f"token should be {c} but was {Compiler.token}"
            )
            self.assertEqual(
                Compiler.token_idx,
                i,
                msg=f"token_idx should be {i} but was {Compiler.token_idx}",
            )
            Compiler.next_token()


if __name__ == "__main__":
    unittest.main()
