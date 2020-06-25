#!/usr/bin/env python
# -*- coding=utf-8 -*-

import sys
from simple_parser import SimpleParser
from ast_node import ASTNode
from ast_node_type import ASTNodeType


# /**
#  * 一个简单的脚本解释器。
#  * 所支持的语法，请参见SimpleParser.java
#  *
#  * 运行脚本：
#  * 在命令行下，键入：java SimpleScript
#  * 则进入一个REPL界面。你可以依次敲入命令。比如：
#  * > 2+3;
#  * > int age = 10;
#  * > int b;
#  * > b = 10*2;
#  * > age = age + b;
#  * > exit();  //退出REPL界面。
#  *
#  * 你还可以使用一个参数 -v，让每次执行脚本的时候，都输出AST和整个计算过程。
#  *
#  */

class SimpleScript:
    def __init__(self):
        self.variables = dict()
        self.verbose = False

    
    def start(self):
        # print "This is the name of the script: ", sys.argv[0]
        # print "Number of arguments: ", len(sys.argv)
        # print "The arguments are: " , str(sys.argv)
        if len(sys.argv) > 1 and sys.argv[1] == '-v':
            self.verbose = True
            print('verbose mode')
        
        print('Simple script language')

        parser = SimpleParser()
        script = SimpleScript()

        script_text = ''
        # print('\n>') # 提示符

        while True:
            try:
                line = input("\n>") 
                line = line.strip()
                if line == 'exit();':
                    print('Good bye!')
                    break
                script_text += line + '\n'
                if line.endswith(';'):
                    tree = parser.parse(script_text)
                    if (self.verbose):
                        tree.dump_ast('')
                    script.evaluate(tree, '')
                    script_text = ''
            except Exception as e:
                print(e)
                script_text = ''


    def evaluate(self, node, indent):
        """[遍历AST，计算值]

        Args:
            node ([ASTNode]): [description]
            indent ([str]): [description]
        """
        result = None
        node_type = node.node_type
        if self.verbose:
            print(indent + 'Calculating: ' + node_type)
        
        if node_type == ASTNodeType.Programm:
            # print(node, len(node.children), 'ssss')
            for child in node.children:
                result = self.evaluate(child, indent)
                # print(result, 'aaaa')
        elif node_type == ASTNodeType.Additive:
            child1 = node.children[0]
            value1 = self.evaluate(child1, indent + '\t')
            child2 = node.children[1]
            value2 = self.evaluate(child2, indent + '\t')

            if node.text == '+':
                result = value1 + value2
            else:
                result = value1 - value2
        elif node_type == ASTNodeType.Multiplicative:
            child1 = node.children[0]
            value1 = self.evaluate(child1, indent + '\t')
            child2 = node.children[1]
            value2 = self.evaluate(child2, indent + '\t')

            if node.text == '*':
                result = value1 * value2
            else:
                result = value1 / value2
        elif node_type == ASTNodeType.IntLiteral:
            result = int(node.text)
        elif node_type == ASTNodeType.Identifier:
            var_name = node.text
            if var_name in self.variables:
                value = self.variables[var_name]
                if value:
                    result = int(value)
                else:
                    raise Exception('variable' + var_name + 'has not been set any value')
            else:
                raise Exception('unknown variable: ' + var_name)
        elif node_type == ASTNodeType.AssignmentStmt:
            var_name = node.text
            if var_name not in self.variables:
                raise Exception('unknown variable: ' + var_name)
            var_value = None
            if node.children:
                child = node.children[0]
                result = self.evaluate(child, indent + "\t")
                var_value = int(result)
            self.variables[var_name] = var_value
        elif node_type == ASTNodeType.IntDeclaration:
            var_name = node.text
            var_value = None
            if node.children:
                child = node.children[0]
                result = self.evaluate(child, indent + "\t")
                var_value = int(result)
            self.variables[var_name] = var_value
        
        if self.verbose:
            print(indent + "Result: " + result)
        elif indent == "":
            if node.node_type == ASTNodeType.IntDeclaration or node.node_type == ASTNodeType.AssignmentStmt:
                print(node.text + ': ', result)
            elif node.node_type != ASTNodeType.Programm:
                print(result)
        
        return result
        


        # Python program showing  
# a use of raw_input() 
  
# g = raw_input("Enter your name : ") 
# print g 

