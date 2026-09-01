# test_blockforgeelite.py
"""
Tests for BlockForgeElite module.
"""

import unittest
from blockforgeelite import BlockForgeElite

class TestBlockForgeElite(unittest.TestCase):
    """Test cases for BlockForgeElite class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockForgeElite()
        self.assertIsInstance(instance, BlockForgeElite)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockForgeElite()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
