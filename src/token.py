#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import abstractmethod
from token_type import TokenType

class Token:
    """docstring for Token."""

    # @abstractmethod
    def get_type(self):
        print('executed.....')
        pass
        # raise NotImplementedError

    # @abstractmethod
    def get_text(self):
        pass
        # raise NotImplementedError


class SimpleToken(Token):
    """docstring for SimpleToken."""
    def __init__(self, type=None, text=''):
        # super(Token, self).__init__()
        self.type = type
        self.text = text

        # def get_type(self):
        #     print('executedaaaaaaaa')
        #     return self.type

        # def get_text(self):
        #     print('executedaaaaaaaa')
        #     self.text
    def __str__(self):
        return "<SimpleToken> type={} text={}".format(self.type, self.text)