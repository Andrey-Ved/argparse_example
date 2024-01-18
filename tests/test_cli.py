import pytest

from argparse_demo.cli import cli_logic


def test_cli():
    assert cli_logic(['--ram', ]) == 0
    assert cli_logic(['--ip', ]) == 0
    assert cli_logic(['--cpu', '--int', '56', ]) == 0

    with pytest.raises(SystemExit):
        cli_logic(['--cpu', '--int', '56.1', ])

    with pytest.raises(SystemExit):
        cli_logic(['--cpu', 'True', ])
