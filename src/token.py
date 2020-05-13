#!/usr/bin/python
from abc import abstractmethod
from .token_type import TokenType

class Token:
    """docstring for Token."""

    @abstractmethod
    def get_type(self):
        raise NotImplementedError

    @abstractmethod
    def get_text(self):
        raise NotImplementedError


class SimpleToken(Token):
    """docstring for SimpleToken."""
    def __init__(self):
        super(Token, self).__init__()
        self.type = None
        self.text = ''

        def get_type(self):
            return self.type

        def get_text(self):
            self.text
        