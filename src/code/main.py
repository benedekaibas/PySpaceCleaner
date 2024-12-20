"""Main file of the project containing all the functions."""

import os
import re
import argparse
from rich.console import Console

console = Console()

class RemoveWhiteSpace():
    """Main class of the project containing all the necessary functions. """

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path


    def open_file(self):
        """Opening files from input."""
        with open(self.file_path, "r", encoding = "utf-8") as file:
            content = file.read()

        return content


    def remove_whitespace(self, content: str):
        """Removing whitespace from a file."""
        # remove whitespace between string characters
        def keep_backticks(match):
            return match.group(0)
        # remove whitespace between string characters
        content = re.sub(r'(`[^`]*`)| +', lambda m: keep_backticks(m) if m.group(1) else ' ', content)

        # remove whitespaces from blank lines
        content = re.sub(r'^\s*$', '', content, flags=re.MULTILINE)
        # remove whitespaces from lines that end with whitespaces
        content = re.sub(r' +\n', '\n', content)

        return content


    def save_modified_files(self, content: str) -> str:
        """Save the modified file for the user."""
        with open(self.file_path, 'w', encoding = "utf-8") as file:
            file.write(content)
            console.print(f"[green]File '{self.file_path}' has been processed and saved.[/green]")


    def not_valid_file(self) -> bool:
        """Check if file is valid and exists"""
        if not os.path.isfile(self.file_path):
            console.print(f"[red]Error: '{self.file_path}' is not a valid file.[/red]")
            return False
        return True


def main():
    """Main function to execute the program."""
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Remove whitespace from a file.")
    parser.add_argument("file_path", help="Path to the file to process")
    args = parser.parse_args()

    # Initialize RemoveWhiteSpace class and process the file
    remover = RemoveWhiteSpace(args.file_path)

    if remover.not_valid_file():  # Correctly calls validate_file
        content = remover.open_file()
        modified_content = remover.remove_whitespace(content)
        remover.save_modified_files(modified_content)


if __name__ == "__main__":
    main()
