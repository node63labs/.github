from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = (
    Path(__file__).resolve().parents[2]
    / "scripts"
    / "ci"
    / "validate-profile.py"
)

SPEC = importlib.util.spec_from_file_location(
    "node63_validate_profile",
    SCRIPT,
)

assert SPEC is not None
assert SPEC.loader is not None

module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


VALID = """# NODE63 Labs

## Open Developer Ecosystem

Public surface.

## Repository Visibility Model

Visibility.

## Security

Security.

## Licensing

Licensing.
"""


class ProfileValidatorTests(unittest.TestCase):

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

        (
            self.root
            / "profile"
        ).mkdir()

    def tearDown(self):
        self.temp.cleanup()

    def write(self, text):
        (
            self.root
            / "profile"
            / "README.md"
        ).write_bytes(
            text.encode("utf-8")
        )

    def test_valid_profile(self):
        self.write(VALID)

        self.assertEqual(
            module.validate_profile(
                self.root
            ),
            [],
        )

    def test_missing_required_section_fails(self):
        self.write(
            VALID.replace(
                "## Security\n\nSecurity.\n\n",
                "",
            )
        )

        errors = module.validate_profile(
            self.root
        )

        self.assertTrue(
            any(
                "missing required section"
                in error
                for error in errors
            )
        )

    def test_legacy_owner_namespace_fails(self):
        self.write(
            VALID
            + "\nnode63labs-owner\n"
        )

        errors = module.validate_profile(
            self.root
        )

        self.assertTrue(
            any(
                "forbidden legacy namespace"
                in error
                for error in errors
            )
        )

    def test_trailing_whitespace_fails(self):
        self.write(
            VALID.replace(
                "# NODE63 Labs",
                "# NODE63 Labs ",
            )
        )

        errors = module.validate_profile(
            self.root
        )

        self.assertTrue(
            any(
                "trailing horizontal whitespace"
                in error
                for error in errors
            )
        )


if __name__ == "__main__":
    unittest.main()
