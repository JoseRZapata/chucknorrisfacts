#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `chucknorrisfacts` package."""

import pytest

from click.testing import CliRunner

from chucknorrisfacts import chucknorrisfacts
from chucknorrisfacts import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "*** Chuck Norris Facts ***" in result.output
    #help_result = runner.invoke(cli.main, ['--help'])
    cli_result = runner.invoke(cli.main)
    assert cli_result.exit_code == 0
    #assert '--help  Show this message and exit.' in help_result.output
    

 
def test_cnfacts(capsys):
    """We use the capsys argument to capture printing to stdout."""
    assert chucknorrisfacts.cnfacts() == None
  
    # Capture the result of the pyrobo.hablame() function call.
    captured = capsys.readouterr()

    # If we check captured, we can see that the ingredients have been printed.
    assert "*** Chuck Norris Facts ***" in captured.out




