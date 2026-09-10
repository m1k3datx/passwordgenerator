import argparse
import secrets
import string


def generate_password(
    length=12,
    *,
    use_uppercase=True,
    use_lowercase=True,
    use_digits=True,
    use_symbols=True,
):
    """Generate a password using a cryptographically secure random source."""
    if not isinstance(length, int) or isinstance(length, bool) or length < 1:
        raise ValueError("length must be a positive integer")

    character_groups = []
    if use_uppercase:
        character_groups.append(string.ascii_uppercase)
    if use_lowercase:
        character_groups.append(string.ascii_lowercase)
    if use_digits:
        character_groups.append(string.digits)
    if use_symbols:
        character_groups.append(string.punctuation)

    if not character_groups:
        raise ValueError("at least one character group must be enabled")

    characters = "".join(character_groups)
    return "".join(secrets.choice(characters) for _ in range(length))


def parse_args(args=None):
    parser = argparse.ArgumentParser(description="Generate a secure random password.")
    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=12,
        help="password length (default: 12)",
    )
    parser.add_argument(
        "--no-uppercase",
        action="store_false",
        dest="use_uppercase",
        help="exclude uppercase letters",
    )
    parser.add_argument(
        "--no-lowercase",
        action="store_false",
        dest="use_lowercase",
        help="exclude lowercase letters",
    )
    parser.add_argument(
        "--no-digits",
        action="store_false",
        dest="use_digits",
        help="exclude digits",
    )
    parser.add_argument(
        "--no-symbols",
        action="store_false",
        dest="use_symbols",
        help="exclude punctuation symbols",
    )
    return parser.parse_args(args)


def main(args=None):
    options = parse_args(args)
    try:
        password = generate_password(
            options.length,
            use_uppercase=options.use_uppercase,
            use_lowercase=options.use_lowercase,
            use_digits=options.use_digits,
            use_symbols=options.use_symbols,
        )
    except ValueError as error:
        raise SystemExit(f"error: {error}") from error

    print("Generated password:", password)


if __name__ == "__main__":
    main()
