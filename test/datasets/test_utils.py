"""Test utils loading datasets."""

import unittest

import toponetx.datasets.utils as data_utils


class TestUtils(unittest.TestCase):
    """Test datasets utils."""

    def test_load_ppi(self):
        """Test that the ppi dataset loads correctly."""
        G = data_utils.load_ppi()
        assert len(G.nodes) == 20
        assert len(G.edges) == 102
