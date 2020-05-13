from enum import Enum

class DfaState(Enum):
    Initial = 1

    If = 11
    Id_if1 = 12
    Id_if2 = 13
    Else = 14
    Id_else1 = 15
    Id_else2 = 16
    Id_else3 = 17
    Id_else4 = 18
    Int = 19
    Id_int1 = 20
    Id_int2 = 21
    Id_int3 = 22
    Id = 23
    GT = 24
    GE = 25

    Assignment = 31

    Plus = 41
    Minus = 42
    Star = 43
    Slash = 44

    SemiColon = 51
    LeftParen = 52
    RightParen = 53

    IntLiteral = 61