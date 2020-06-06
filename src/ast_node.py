#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import abstractmethod


class ASTNode:

    @abstractmethod
    def get_parent(self):
        pass
    
    @abstractmethod
    def get_children(self):
        pass

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_text(self):
        pass


class SimpleASTNode(ASTNode):
    def __init__(self, node_type=None, text=''):
        self.parent = None
        self.children = []
        self.readonly_children = self.children.copy()
        self.node_type = node_type
        self.text = text

    def get_children(self):
        return self.readonly_children
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    
    def dump_ast(self, indent):
        print('{}{} {}'.format(indent, self.node_type, self.text))
        for child in self.children:
            child.dump_ast(indent + '\t')