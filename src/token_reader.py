#!/usr/bin/python

# 一个Token流。由Lexer生成。Parser可以从中获取Token。
class TokenReader():
    # 返回Token流中下一个Token，并从流中取出。 如果流已经为空，返回null;
    def read(self):
        pass

    # 返回Token流中下一个Token，但不从流中取出。 如果流已经为空，返回null;
    def peek(self):
        pass

    # Token流回退一步。恢复原来的Token。
    def unread(self):
        pass

    # 获取Token流当前的读取位置。
    def get_position(self):
        pass

    # 设置Token流当前的读取位置
    def set_position(self):
        pass


class SimpleTokenReader(TokenReader):
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    
    def read(self):
        if self.pos < len(self.tokens):
            token = self.tokens[self.pos]
            self.pos += 1
            return token
        return None


    def peek():
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    
    def unread(self):
        if self.pos > 0:
            self.pos -= 1


    def get_position(self):
        return self.pos
    
    
    def set_position(self, position):
        if 0 <= position < len(self.tokens):
            self.pos = position

    def dump(self):
        print('text\ttype')
        # print(self.tokens, len(self.tokens), 'aaa')
        token = self.read()
        print(token, type(token), 'aaaaa')
        while token:
            # print('{}\t\t{}'.format(token.get_text(), token.get_type()))
            print('{}\t\t{} '.format(token.text, token.type))
            token = self.read()
