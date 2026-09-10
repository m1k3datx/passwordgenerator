import string
import unittest
from unittest.mock import patch

from generate_password import generate_password, main


class GeneratePasswordTests(unittest.TestCase):
    def test_default_length_and_character_groups(self):
        password = generate_password()

        self.assertEqual(len(password), 12)
        allowed = string.ascii_letters + string.digits + string.punctuation
        self.assertTrue(all(character in allowed for character in password))

    def test_character_options_are_respected(self):
        password = generate_password(
            100,
            use_uppercase=False,
            use_lowercase=False,
            use_symbols=False,
        )

        self.assertTrue(password.isdigit())

    def test_invalid_length_is_rejected(self):
        for length in (0, -1, True, "12"):
            with self.subTest(length=length):
                with self.assertRaises(ValueError):
                    generate_password(length)

    def test_at_least_one_character_group_is_required(self):
        with self.assertRaises(ValueError):
            generate_password(
                use_uppercase=False,
                use_lowercase=False,
                use_digits=False,
                use_symbols=False,
            )

    @patch("generate_password.secrets.choice", return_value="x")
    def test_uses_secrets_for_selection(self, secure_choice):
        self.assertEqual(generate_password(4), "xxxx")
        self.assertEqual(secure_choice.call_count, 4)

    def test_cli_accepts_length_and_options(self):
        with patch("builtins.print") as print_mock:
            main(["--length", "8", "--no-symbols"])

        output = print_mock.call_args.args[1]
        self.assertEqual(len(output), 8)
        self.assertTrue(all(character not in string.punctuation for character in output))


if __name__ == "__main__":
    unittest.main()
