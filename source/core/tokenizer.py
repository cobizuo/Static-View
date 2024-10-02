#tokenizer.py

import tokenize
from io import BytesIO
from typing import List, Tuple, Union

class CodeTokenizer:
    """
    This class tokenizes the input code and standardizes it
    Prepares the tokens for further analysis and AST parsing
    Supports Python code tokenization by default
    """

    def __init__(self, file_path: str):
        """
        Initialize the class
        
        Args:
            file_path (str): the source code filepath to be tokenized
        """

        self.code = self.read_from_file(file_path)
        self.tokens = []

    def read_from_file(self, file_path: str) -> str:
        """
        Reads code from the given file and returns it as a string.
        
        Args:
            file_path (str): the provided file path to be read
            
        Returns:
            str: The content of the file as a string
        """

        with open(file_path, 'r') as file:
            return file.read()
        
    def tokenize_code(self) -> List[Tuple[int, str]]:
        """
        Tokenize the input code
        
        Returns:
            List[Tuple[int, str]]: A list of tokens with their token type and string value
        """

        token_stream = tokenize.tokenize(BytesIO(self.code.encode('utf-8')).readline)
        for token in token_stream:
            token_type = tokenize.tok_name[token.type]
            token_value = token.string
            self.tokens.append((token_type, token_value))

        return self.tokens

    def standardized_tokens(self) -> List[str]:
        """
        Conver the tokens into a standardized list of only token values.
        Removing whitespace, comments, and other irrelevant tokens for further analysis.
        
        Returns:
            List[str]: A standardizd list of tokens
        """

        standardized = []
        for token_type, token_value in self.tokens:
            if token_type not in ['COMMENT', 'NL', 'NEWLINE', 'INDENT', 'DEDENT']:
                standardized.append(token_value)

        return standardized
    
    def display_tokens(self):
        """
        Display the tokens in a readable formant for debugging purposes
        """

        for token_type, token_value in self.tokens:
            print(f"Token Type: {token_type}, Token Vlaue: {token_value}")


if __name__ == "__main__":
    

    file_path = "C:\\Users\\cobiz\\OneDrive - Bowie State\\Documents\\GitHub\\Static-View\\test.py"
    
    # Initialize tokenizer with the file path
    tokenizer = CodeTokenizer(file_path)
    
    # Tokenize the code
    tokenizer.tokenize_code()
    
    # Display all tokens
    print("Tokens from file input:")
    tokenizer.display_tokens()
    
    # Standardized tokens
    standardized = tokenizer.standardized_tokens()
    print("\nStandardized Tokens:")
    print(standardized)