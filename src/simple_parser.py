#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from simple_lexer import SimpleLexer
from ast_node import SimpleASTNode
from token_reader import TokenReader
from ast_node_type import ASTNodeType
from token_type import TokenType

# /**
#  * 一个简单的语法解析器。
#  * 能够解析简单的表达式、变量声明和初始化语句、赋值语句。
#  * 它支持的语法规则为：
#  *
#  * programm -> intDeclare | expressionStatement | assignmentStatement
#  * intDeclare -> 'int' Id ( = additive) ';'
#  * expressionStatement -> addtive ';'
#  * addtive -> multiplicative ( (+ | -) multiplicative)*
#  * multiplicative -> primary ( (* | /) primary)*
#  * primary -> IntLiteral | Id | (additive)
#  */
class SimpleParser:
    def __init__(self):
        pass


    def parse(self, script):
        lexer = SimpleLexer()
        token_reader = lexer.tokenize(script)
        return self.prog(token_reader)


    def prog(self, token_reader):
        node = SimpleASTNode(ASTNodeType.Programm, 'pwc')
        while token_reader.peek():
            child = self.int_declare(token_reader)
            if not child:
                child = self.expression_statement(token_reader)
            
            if not child:
                child = self.assignment_statement(token_reader)
            
            if child:
                node.add_child(child)
            else:
                raise Exception('unknown statement')
        return node

    # int a;
    # int b = 2 * 3;
    def int_declare(self, token_reader):
        node = None
        token = token_reader.peek()
        print(token, type(token))
        if token and token.type == TokenType.Int:
            token = token_reader.read()
            if token_reader.peek().type == TokenType.Identifier:
                token = token_reader.read()
                node = SimpleASTNode(ASTNodeType.IntDeclaration, token.text)
                token = token_reader.peek()
                if token and token.type == TokenType.Assignment:
                    token_reader.read()
                    child = self.additive(token_reader)
                    if not child:
                        raise Exception('invalid variable initialization, expecting an expression')
                    else:
                        node.add_child(child)
            else:
                raise Exception('variable name expected')
            
            if node:
                token = token_reader.peek()
                if token and token.type == TokenType.SemiColon:
                    token_reader.read()
                else:
                    raise Exception('invalid statement, expecting semicolon')
        return node


    def expression_statement(self, token_reader):
        pos = token_reader.get_position()
        node = self.additive(token_reader)
        if node:
            token = token_reader.peek()
            if token and token.type == TokenType.SemiColon:
                token_reader.read()
            else:
                node = None
                token_reader.set_position(pos)
        return node

    # age = 10 * 2;
    def assignment_statement(self, token_reader):
        node = None
        token = token_reader.peek()
        if token and token.type == TokenType.Identifier:
            token = token_reader.read()
            node = SimpleASTNode(ASTNodeType.AssignmentStmt, token.text)
            token = token_reader.peek()
            if token and token.type == TokenType.Assignment:
                token_reader.read()
                child = self.additive(token_reader)
                if not child:
                    raise Exception('invalide assignment statement, expecting an expression')
                else:
                    node.add_child(child)
                    token = token_reader.peek()
                    if token and token.type == TokenType.SemiColon:
                        token_reader.read()
                    else:
                        raise Exception("invalid statement, expecting semicolon")
            else:
                token_reader.unread()
                node = None
        return node



    def additive(self, token_reader):
        child1 = self.multiplicative(token_reader)
        node = child1
        if child1:
            while True:
                token = token_reader.peek()
                if token and (token.type == TokenType.Plus or token.type == TokenType.Minus):
                    token = token_reader.read()
                    child2 = self.multiplicative(token_reader)
                    if child2:
                        node = SimpleASTNode(ASTNodeType.Additive, token.text)
                        node.add_child(child1)
                        node.add_child(child2)
                    else:
                        raise Exception('invalid additive expression, expecting the right part.')
                else:
                    break
        return node


    def multiplicative(self, token_reader):
        child1 = self.primary(token_reader)
        node = child1

        while True:
            token = token_reader.peek()
            if token and (token.type == TokenType.Star or token.type == TokenType.Slash):
                token = token_reader.read()
                child2 = self.primary(token_reader)
                if child2:
                    node = SimpleASTNode(ASTNodeType.Multiplicative, token.text)
                    node.add_child(child1)
                    node.add_child(child2)
                    child1 = node
                else:
                    raise Exception("invalid multiplicative expression, expecting the right part.")
            else:
                break
        return node


    def primary(self, token_reader):
        node = None
        token = token_reader.peek()
        if token:
            if token.type == TokenType.IntLiteral:
                token = token_reader.read()
                node = SimpleASTNode(ASTNodeType.IntLiteral, token.text)
            elif token.type == TokenType.Identifier:
                token = token_reader.read()
                node = SimpleASTNode(ASTNodeType.Identifier, token.text)
            elif token.type == TokenType.LeftParen:
                token_reader.read
                node = self.additive(token_reader)
                if node:
                    token = token_reader.peek()
                    if token and token.type == TokenType.RightParen:
                        token_reader.read()
                    else:
                        raise Exception('expecting right parentesis')
                else:
                    raise Exception('expecting and additive expression inside parenthesis')
        return node







        
        
    # def dump_AST(self, node, in)
        

        
        