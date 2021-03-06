"""
Copyright: (c) 2021, Moritz Eilfort
GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
This module contains helper functions and classes for the tests
"""
import pytest

from britz import cli

# ----------------------------------------------------------------------------
# CLI Helpers
# ----------------------------------------------------------------------------


class MockArgs:
    def __init__(
        self,
        dirname=None,
        version=False,
        debug=False,
        prettify=False,
        output=None,
        graph=False,
        parse=False,
        **kwargs,
    ):
        self.dirname = dirname
        self.version = version
        self.debug = debug
        self.prettify = prettify
        self.output = output
        self.graph = graph
        self.parse = parse


@pytest.fixture
def get_parse_args():
    def parse_args(args=[]):
        return cli.parse_args(cli.parser.parse_args(args))

    return parse_args
