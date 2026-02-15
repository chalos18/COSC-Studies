""" Scanner template for COSC261 Assignment
    ## WARNING ## Your code should be derived from this template 
                  by modifying only the parts mentioned in the requirements; 
                  other changes are at your own risk. 
                  Feel free, however, to experiment during the development.
"""

import re
import sys


class Scanner:
    """The interface comprises the methods lookahead and consume.
    Other methods should not be called from outside of this class.
    """

    def __init__(self, input_file):
        """Reads the whole input_file to input_string, which remains constant.
        current_char_index counts how many characters of input_string have
        been consumed.
        next_token holds the most recently found token and the
        corresponding part of input_string.
        """
        # source code of the program to be compiled
        self.input_string = input_file.read()
        # index where the unprocessed part of input_string starts
        self.current_char_index = 0
        # a pair (most recently read token, matched substring of input_string)
        self.next_token = self.get_token()

    def skip_white_space(self):
        """Consumes white-space characters in input_string up to the
        next non-white-space character.
        Note that white-space includes spaces, tabs, and newline characters.
        """
        while (
            self.current_char_index < len(self.input_string)
            and self.input_string[self.current_char_index].isspace()
        ):
            self.current_char_index += 1

    def no_token(self):
        """Stop execution if the input cannot be matched to a token."""
        print(
            "lexical error: no token found at the start of "
            + self.input_string[self.current_char_index :]
        )
        sys.exit()

    def get_token(self):
        """Returns the next token and the part of input_string it matched.
        The returned token is None if there is no next token.
        The characters up to the end of the token are consumed.
        TODO:
        Call no_token() if the input contains extra characters that
        do not match any token (and are not white-space).
        Extend the method Scanner.get_token to check if the input contains extra non-white-space
        characters that do not match any token (see the docstring of this method for more detail).
        In case of a lexical error, the program will output all recognised tokens before the error except the
        last recognised token (which is the next_token when the error occurs);
        Do not compensate for this (for example, by adding additional print-statements).
        """
        self.skip_white_space()
        # find the longest prefix of input_string that matches a token
        token, longest = None, ""
        for t, r in Token.token_regexp:
            match = re.match(r, self.input_string[self.current_char_index :])
            if match and match.end() > len(longest):
                token, longest = t, match.group()
        # Check for lexical error
        if token is None and self.current_char_index < len(self.input_string):
            self.no_token()
        # consume the token by moving the index to the end of the matched part
        self.current_char_index += len(longest)
        return (token, longest)

    def lookahead(self):
        """Returns the next token without consuming it.
        Returns None if there is no next token.
        """
        return self.next_token[0]

    def unexpected_token(self, found_token, expected_tokens):
        """Stop execution because an unexpected token was found.
        found_token contains just the token, not its value.
        expected_tokens is a sequence of tokens.
        """
        print(
            "syntax error: token in "
            + repr(sorted(expected_tokens))
            + " expected but "
            + repr(found_token)
            + " found"
        )
        sys.exit()

    def consume(self, *expected_tokens):
        """Returns the next token and consumes it, if it is in
        expected_tokens. Calls unexpected_token(...) otherwise.

        If the token is a number or an identifier, not just the
        token but a pair of the token and its value is returned.

        The only attribute you need to access in Scanner.consume is next_token.
        Scanner.consume should not modify the current character index directly;
        instead, it should use get_token.
        """
        token, value = self.next_token

        # Check if the next token is in the list of expected tokens
        if token in expected_tokens:
            # Consume the token by updating next_token
            self.next_token = self.get_token()

            # If the token is a number or an identifier, return a pair of token and value
            if token in [Token.NUM, Token.ID]:
                return (token, value)
            # If the token is not a number or an identifier, return the token itself
            return token
        else:
            # If the next token is not in the list of expected tokens, call unexpected_token method
            self.unexpected_token(token, expected_tokens)


class Token:
    # The following enumerates all tokens.
    DO = "DO"
    ELSE = "ELSE"
    END = "END"
    IF = "IF"
    THEN = "THEN"
    WHILE = "WHILE"
    SEM = "SEM"
    BEC = "BEC"
    LESS = "LESS"
    EQ = "EQ"
    GRTR = "GRTR"
    LEQ = "LEQ"
    NEQ = "NEQ"
    GEQ = "GEQ"
    ADD = "ADD"
    SUB = "SUB"
    MUL = "MUL"
    DIV = "DIV"
    LPAR = "LPAR"
    RPAR = "RPAR"
    NUM = "NUM"
    ID = "ID"
    READ = "READ"  # New token for 'read'
    WRITE = "WRITE"  # New token for 'write'

    # The following list gives the regular expression to match a token.
    # The order in the list matters for mimicking Flex behaviour.
    # Longer matches are preferred over shorter ones.
    # For same-length matches, the first in the list is preferred.
    token_regexp = [
        (DO, "do"),
        (ELSE, "else"),
        (END, "end"),
        (IF, "if"),
        (THEN, "then"),
        (WHILE, "while"),
        (READ, "read"),  # New token for 'read'
        (WRITE, "write"),  # New token for 'write'
        (SEM, ";"),
        (BEC, ":="),
        (LESS, "<"),
        (EQ, "="),
        (GRTR, ">"),
        (LEQ, "<="),
        (GEQ, ">="),
        (NEQ, "!="),  # New token for '!='
        (ADD, "\\+"),  # + is special in regular expressions
        (SUB, "-"),
        (MUL, "\\*"),  # New token for multiplication
        (DIV, "/"),  # New token for division
        (LPAR, "\\("),  # ( is special in regular expressions
        (RPAR, "\\)"),  # ) is special in regular expressions
        (ID, "[a-z]+"),
        (NUM, "\\d+"),  # Regular expression for numbers (one or more digits)
    ]


# Initialise scanner.

scanner = Scanner(sys.stdin)

# Show all tokens in the input.

token = scanner.lookahead()
while token != None:
    if token in [Token.NUM, Token.ID]:
        token, value = scanner.consume(token)
        print(token, value)
    else:
        print(scanner.consume(token))
    token = scanner.lookahead()
