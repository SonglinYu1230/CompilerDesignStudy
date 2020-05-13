from enum import Enum

class TokenType(Enum):
    Plus = 1  # +
    Minus = 2  # -
    Star = 3   # *
    Slash = 4  # /

    GE = 11     # >=
    GT = 12     # >
    EQ = 13     # ==
    LE = 14     # <=
    LT = 15     # <

    SemiColon = 21 # ;
    LeftParen = 22 # (
    RightParen = 23  # )

    Assignment = 31 # =

    If = 41
    Else = 42
    
    Int = 51

    Identifier = 61     # 标识符

    IntLiteral = 71     # 整型字面量
    StringLiteral = 72   # 字符串字面量
