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
    not compensate for this (for example, by adding additional print-statements).
    """
    self.skip_white_space()
    # find the longest prefix of input_string that matches a token
    token, longest = None, ''
    for (t, r) in Token.token_regexp:
        match = re.match(r, self.input_string[self.current_char_index:])
        if match and match.end() > len(longest):
            token, longest = t, match.group()
        if token is None and self.current_char_index < len(self.input_string):
            self.no_token()
        self.skip_white_space()
    # consume the token by moving the index to the end of the matched part
    self.current_char_index += len(longest)
    return (token, longest)