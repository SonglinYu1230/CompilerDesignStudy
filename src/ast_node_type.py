#!/usr/bin/python
# -*- coding: utf-8 -*-

from enum import Enum

class ASTNodeType(Enum):
    Programm = 0          # 程序入口，根节点
    
    IntDeclaration = 1    # 整型变量声明
    ExpressionStmt = 2    # 表达式语句，即表达式后面跟个分号
    AssignmentStmt = 3    # 赋值语句

    Primary = 11          # 基础表达式
    Multiplicative = 12   # 乘法表达式
    Additive = 13         # 加法表达式

    Identifier = 21       # 标识符
    IntLiteral = 22       # 整型字面量
