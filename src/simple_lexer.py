from .token import Token, SimpleToken
from .token_reader import SimpleTokenReader
from .dfa_state import DfaState
from .token_type import TokenType


class SimpleLexer:
    """docstring for SimpleLexer."""
    def __init__(self):
        self.token_text = ''  # 临时保存token的文本
        self.tokens = []      # 保存解析出来的Token
        self.token = SimpleToken()     # 当前正在解析的Token
    
    def is_alpha(self, ch):
        return 'a' <= ch <= 'z' or 'A' <= ch <= 'Z'
    
    def is_digit(self, ch):
        return '0' <= ch <= '9'

    def is_blank(self, ch):
        return ch in [' ', '\t', '\n']
        
    # 有限状态机进入初始状态。
    # 这个初始状态其实并不做停留，它马上进入其他状态。
    # 开始解析的时候，进入初始状态；某个Token解析完毕，也进入初始状态，在这里把Token记下来，然后建立一个新的Token。
    def init_token(self, ch):
        if self.token_text:
            self.token.text = self.token_text
            self.tokens.append(self.token)

            self.token_text = ''
            self.token = SimpleToken()

        new_state = DfaState.Initial
        if self.is_alpha(ch):
            if ch == 'i':
                new_state = DfaState.Id_int1
            else:
                new_state = DfaState.Id
        elif self.is_digit(ch):
            new_state = DfaState.IntLiteral
            self.token.type = TokenType.IntLiteral
            self.token_text += ch
        elif ch == '>':
            new_state = DfaState.GT
            self.token.type = TokenType.GT
            self.token_text += ch
        elif ch == '+':
            new_state = DfaState.Plus
            self.token.type = TokenType.Plus
            self.token_text += ch
        elif ch == '-':
            new_state = DfaState.Minus
            self.token.type = TokenType.Minus
            self.token_text += ch
        elif ch == '*':
            new_state = DfaState.Star
            self.token.type = TokenType.Star
            self.token_text += ch
        elif ch == '/':
            new_state = DfaState.Slash
            self.token.type = TokenType.Slash
            self.token_text += ch
        elif ch == ';':
            new_state = DfaState.SemiColon
            self.token.type = TokenType.SemiColon
            self.token_text += ch
        elif ch == '(':
            new_state = DfaState.LeftParen
            self.token.type = TokenType.LeftParen
            self.token_text += ch
        elif ch == ')':
            new_state = DfaState.RightParen
            self.token.type = TokenType.RightParen
            self.token_text += ch
        elif ch == '=':
            new_state = DfaState.Assignment
            self.token.type = TokenType.Assignment
            self.token_text += ch
        else:
            new_state = DfaState.Initial
        
        return new_state


    # 解析字符串，形成Token。
    # 这是一个有限状态自动机，在不同的状态中迁移。
    def tokenize(self, code):
        self.tokens = []
        self.token_text = ''
        self.token = SimpleToken()

    

    @staticmethod
    def dump(token_reader):
        print('text\ttype')
        token = token_reader.read()
        while token:
            print(token.get_text() + '\t\t' + token.get_type())
            token = token_reader.read()

