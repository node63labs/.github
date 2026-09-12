#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REQUIRED_H1 = "# NODE63 Labs"

REQUIRED_SECTIONS = (
    "## Open Developer Ecosystem",
    "## Repository Visibility Model",
    "## Security",
    "## Licensing",
)

FORBIDDEN_TEXT = (
    "node63labs-owner",
)


def validate_profile(root):
    path = root / "profile" / "README.md"

    if not path.is_file():
        return [
            "profile/README.md: "
            "required organization profile missing"
        ]

    data = path.read_bytes()
    errors = []

    if b"\r" in data:
        errors.append(
            "profile/README.md: "
            "CR/CRLF line ending detected"
        )

    try:
        text = data.decode("utf-8")

    except UnicodeDecodeError:
        return errors + [
            "profile/README.md: "
            "content is not valid UTF-8"
        ]

    lines = text.splitlines()

    if not lines or lines[0] != REQUIRED_H1:
        errors.append(
            "profile/README.md: first line must be {!r}".format(
                REQUIRED_H1
            )
        )

    for number, line in enumerate(
        lines,
        start=1,
    ):
        if line.endswith((" ", "\t")):
            errors.append(
                "profile/README.md: "
                "line {}: trailing horizontal whitespace".format(
                    number
                )
            )

    for section in REQUIRED_SECTIONS:
        if section not in lines:
            errors.append(
                "profile/README.md: "
                "missing required section {!r}".format(
                    section
                )
            )

    for forbidden in FORBIDDEN_TEXT:
        if forbidden in text:
            errors.append(
                "profile/README.md: "
                "forbidden legacy namespace {!r}".format(
                    forbidden
                )
            )

    return errors


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--root",
        default=".",
    )

    args = parser.parse_args()

    root = Path(args.root).resolve()
    errors = validate_profile(root)

    if errors:
        for error in errors:
            print(
                "PROFILE_VALIDATION_FAIL={}".format(
                    error
                ),
                file=sys.stderr,
            )

        return 1

    print("PROFILE_VALIDATION=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
