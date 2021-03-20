from hello_pp import cli
from hello_pp.__version__ import __version__


def test_cli_main_prints_version(capsys):
    cli.main()
    captured_stdout= capsys.readouterr()
    assert __version__ in captured_stdout.out
