import pytest

from argparse_demo.cli import cli_logic


def test_cli():
    assert cli_logic(['--ram', 'True']) == 0
    assert cli_logic(['--ip', '1']) == 0
    assert cli_logic(['--cpu', '1', '--int', '56']) == 0

    with pytest.raises(SystemExit):
        cli_logic(['--int', '56.1'])
