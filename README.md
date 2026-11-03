# password-vault: Encrypted Command-Line Password Manager

A local, command-line password manager written in Python. It stores credentials in an encrypted vault on your own machine, using Argon2id to turn a master password into an encryption key and AES-256-GCM to encrypt the vault contents.

> **Based on the open-source [Password Manager](https://github.com/CarterPerez-dev/Cybersecurity-Projects/tree/main/PROJECTS/foundations/password-manager) project by CarterPerez-dev** (AGPL-3.0-or-later). Used here as a college cybersecurity training project.

---

## Features

According to the project description in `pyproject.toml`, this is a beginner-friendly encrypted password manager built on **Argon2id** and **AES-256-GCM**.

- **Key derivation:** the master password is turned into an encryption key with Argon2id (`argon2-cffi`).
- **Authenticated encryption:** vault contents are encrypted with AES-256-GCM (`cryptography`), so tampering is detected when decrypting.
- **Command-line interface:** built with [Typer](https://typer.tiangolo.com/), with terminal formatting from [Rich](https://rich.readthedocs.io/).
- **Typed and tested code:** the project is configured for `pytest`, `ruff`, `mypy` and `pylint`, and requires type annotations on every function.

---

## Requirements

- **Python 3.13 or newer**
- Runtime dependencies (declared in `pyproject.toml`):

| Package | Minimum version | Purpose |
|:--|:--|:--|
| `argon2-cffi` | 25.1.0 | Argon2id key derivation |
| `cryptography` | 48.0.0 | AES-256-GCM encryption |
| `typer` | 0.25.1 | Command-line interface |
| `rich` | 15.0.0 | Colored output, tables and panels |

- Development dependencies (optional extra `dev`): `pytest`, `pytest-cov`, `ruff`, `mypy`, `pylint`, `yapf`.

---

## Installation

There is **no `requirements.txt`** in this repository. Dependencies are declared in `pyproject.toml`, and the package is built with `hatchling`.

### Option 1: pip

```bash
git clone https://github.com/harshillvashisht/password_manager.git
cd password_manager
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e .
```

To include the development tools:

```bash
pip install -e ".[dev]"
```

### Option 2: uv

```bash
uv sync                # runtime dependencies
uv sync --extra dev    # add development tools
```

### About `install.sh`

`install.sh` checks for Python 3.13+, installs `uv` and `just` if they are missing, and then runs `just setup`. That command needs a `Justfile`, which is **not included in this repository**, so the script will stop at that step unless a `Justfile` is added. Use Option 1 or 2 above instead.

---

## Usage

Installing the package creates two equivalent commands, `pv` and `password-vault`. The module can also be run directly:

```bash
pv --help
python -m password_manager --help
```

Commands confirmed in the project files:

```bash
pv init            # create a new vault
pv add github      # add a credential named "github"
pv get github      # retrieve a credential
pv list            # list stored entries
pv check           # rate a password without displaying it
```

`pv check` prompts for the password with hidden input and calculates a
local weak, fair, or strong rating from length, character variety, and
estimated entropy. When adding an entry, weak passwords produce a warning
and require confirmation; they are not rejected automatically.

Run `pv --help` to see the complete, current list of commands and options.

---

## Testing and code quality

```bash
pytest                      # run the test suite in tests/
pytest --cov                # with coverage (needs the dev extra)
ruff check src
mypy src
```

---

## Repository structure

```
.
├── src/
│   └── password_manager/   # application source code
├── tests/                  # pytest test suite
├── .gitignore
├── install.sh              # helper script (needs a Justfile, see above)
├── pyproject.toml          # metadata, dependencies, tool configuration
└── README.md
```

---

## Security notes

- Argon2id and AES-256-GCM are standard, well-reviewed choices, but this project is a learning project and has **not been independently audited**. Do not rely on it for real, high-value secrets.
- The strength of the vault still depends on the strength of the master password.
- Losing the master password means the vault cannot be recovered.

---

## License

Licensed under **AGPL-3.0-or-later**, as is the original project. See the `LICENSE` file. Original copyright notices are kept in the source files.