import subprocess
import sys
import re


def run_cli(args):
    """Helper to run CLI with arguments and return stdout."""
    result = subprocess.run(
        [sys.executable, "main.py"] + args,
        capture_output=True, text=True
    )
    return result.stdout


def test_generate_username_only():
    output = run_cli(["--userlen", "7"])
    assert "Generated random username:" in output


def test_generate_username_with_flags():
    output = run_cli(["--userlen", "8", "--userstyle", "readable"])
    assert "Generated human-readable username:" in output
    assert "Generated Password:" not in output
    assert "Generated PIN:" not in output


def test_generate_password_only():
    output = run_cli(["--passlen", "12"])
    assert "Generated Password:" in output
    assert re.search(r"Generated Password:\s+[!-~]{12}", output)


def test_generate_pin_only():
    output = run_cli(["--pinlen", "4"])
    assert "Generated PIN:" in output
    assert re.search(r"Generated PIN:\s+\d{4}", output)


def test_generate_all():
    output = run_cli(["--userlen", "6", "--passlen", "10", "--pinlen", "4"])
    assert "Generated random username:" in output
    assert "Generated Password:" in output
    assert "Generated PIN:" in output


def test_help_flag():
    output = run_cli(["--help"])
    assert "--userlen" in output
    assert "Credential Generator" in output
