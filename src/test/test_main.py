import unittest
from unittest.mock import mock_open, patch
from code.main import RemoveWhiteSpace

class TestRemoveWhiteSpace(unittest.TestCase):
    """Test cases for the main.py file. """
    @patch("builtins.open", new_callable=mock_open, read_data="This is a test file.\n\nWith some whitespace.  \n")
    def test_open_file(self, mock_file):
        rws = RemoveWhiteSpace("dummy_path")
        content = rws.open_file()
        self.assertEqual(content, "This is a test file.\n\nWith some whitespace.  \n")
        mock_file.assert_called_once_with("dummy_path", "r", encoding="utf-8")


    def test_remove_whitespace(self):
        rws = RemoveWhiteSpace("dummy_path")
        content = "This is a test file.\n\nWith some whitespace.  \n"
        expected_content = "This is a test file.\n\nWith some whitespace.\n"
        modified_content = rws.remove_whitespace(content)
        self.assertEqual(modified_content, expected_content)


    @patch("builtins.open", new_callable=mock_open)
    def test_save_modified_files(self, mock_file):
        rws = RemoveWhiteSpace("dummy_path")
        content = "This is a test file.\n\nWith some whitespace.\n"
        rws.save_modified_files(content)
        mock_file().write.assert_called_once_with(content)


if __name__ == "__main__":
    unittest.main()
