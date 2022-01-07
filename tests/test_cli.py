from click.testing import CliRunner
from erbach.cli import cli
from erbach.cli import Environment

def test_cli_environment():
	"""verify that the environment is set"""
	env = Environment()
	assert not env.debug

def test_cli_help_option():
    """test cli help option"""
    runner = CliRunner()
    result = runner.invoke(cli, ['--help'])
    assert result.exit_code == 0
    assert "Usage" in result.output

# test individual commands

def test_deps_cmd():
    runner = CliRunner()
    result = runner.invoke(cli, ['deps'])
    assert result.exit_code == 0
    assert "mmf" in result.output
