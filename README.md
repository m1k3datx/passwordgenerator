# Password Generator

A small, dependency-free command-line password generator for Python 3.8+.

## Usage

Generate a 12-character password with uppercase and lowercase letters, digits,
and symbols:

```console
$ python generate_password.py
Generated password: u8^Qm2!zR4@p
```

Choose a length with `--length` (or `-l`) and disable character groups when a
system has stricter requirements:

```console
$ python generate_password.py --length 24 --no-symbols
Generated password: ...

$ python generate_password.py -l 16 --no-uppercase --no-digits
Generated password: ...
```

At least one character group must remain enabled. Invalid lengths and an
all-disabled configuration produce a clear command-line error.

The generator can also be imported:

```python
from generate_password import generate_password

password = generate_password(20, use_symbols=False)
```

## Security notes

- Password characters are selected with Python's `secrets` module, which is
  intended for security-sensitive randomness.
- Passwords are printed to standard output by the CLI. Avoid saving terminal
  history or output where passwords could be exposed.
- The default is a convenience, not a policy recommendation. Use a length and
  character set compatible with the service where the password will be used.

## Testing

Run the focused, standard-library test suite from the repository root:

```console
$ python -m unittest -v
```

No third-party packages are required.
