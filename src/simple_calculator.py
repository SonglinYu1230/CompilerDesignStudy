#/usr/bin/python
from ast_node import SimpleASTNode
from token_type import TokenType
from ast_node_type import ASTNodeType
from simple_lexer import SimpleLexer


class SimpleCalculator:

    def evaluate(self, script):
        tree = self.parse(script)
        tree.dump_ast("")
        self.__evaluate(tree, "")


    def parse(self, code):
        lexer = SimpleLexer()
        token_reader = lexer.tokenize(code)

        root_node = self.prog(token_reader)
        return root_node


    # 对某个AST节点求值，并打印求值过程。
    def __evaluate(self, node, indent):
        result, node_type = 0, node.node_type
        print('{}Calculating: {}'.format(indent, node_type))

        if node_type == ASTNodeType.Programm:
            for child in node.children:
                result = self.__evaluate(child, indent + '\t')
        elif node_type == ASTNodeType.Additive:
            child1 = node.children[0]
            value1 = self.__evaluate(child1, indent + '\t')
            child2 = node.children[1]
            value2 = self.__evaluate(child2, indent + '\t')
            
            if node.text == '+':
                result = value1 + value2
            else:
                result = value1 - value2
        elif node_type == ASTNodeType.Multiplicative:
            child1 = node.children[0]
            value1 = self.__evaluate(child1, indent + '\t')
            child2 = node.children[1]
            value2 = self.__evaluate(child2, indent + '\t')
            
            if node.text == '*':
                result = value1 * value2
            else:
                result = value1 / value2
        elif node_type == ASTNodeType.IntLiteral:
            result = int(node.text)
        
        print(indent + 'Result: ' + str(result))
        return result        



    # 语法解析：根节点
    def prog(self, token_reader):
        node = SimpleASTNode(ASTNodeType.Programm, 'Calculator')
        child = self.additive(token_reader)
        if child:
            node.add_child(child)
        return node


    # 整型变量声明语句，如：
    # int a;
    # int b = 2*3;
    def int_declare(self, token_reader):
        print('int_declare', len(token_reader.tokens),'aaa')
        node = None
        token = token_reader.peek()
        if token and token.type == TokenType.Int:
            token = token_reader.read()
            if token_reader.peek().type == TokenType.Identifier:
                token = token_reader.read()
                print(token, 'zzzz')
                # 创建当前节点，并把变量名记到AST节点的文本值中，这里新建一个变量子节点也是可以的
                node = SimpleASTNode(ASTNodeType.IntDeclaration, token.text)
                token = token_reader.peek()
                if token and token.type == TokenType.Assignment:
                    token_reader.read()
                    child = self.additive(token_reader)
                    if not child:
                        raise Exception('invalide variable initialization, expecting an expression')
                    else:
                        node.add_child(child)
            else:
                raise Exception('variable name expected')
            
            if node:
                token = token_reader.peek()
                print(token, 'tttttt')
                if token and token.type == TokenType.SemiColon:
                    token_reader.read()
                else:
                    raise Exception('invalid statement, expecting semicolon')
        return node


    # 语法解析：加法表达式
    def additive(self, token_reader):
        child1 = self.multiplicative(token_reader)
        node = child1

        token = token_reader.peek()
        
        if child1 and token:
            if token.type == TokenType.Plus or token.type == TokenType.Minus:
                token = token_reader.read()
                child2 = self.additive(token_reader)
                if child2:
                    node = SimpleASTNode(ASTNodeType.Additive, token.text)
                    node.add_child(child1)
                    node.add_child(child2)
                else:
                    raise Exception('invalid additive expression, expecting the right part.')
        return node


    # 语法解析：乘法表达式
    def multiplicative(self, token_reader):
        child1 = self.primary(token_reader)
        node = child1

        token = token_reader.peek()
        if child1 and token:
            if token.type == TokenType.Star or token.type == TokenType.Slash:
                token = token_reader.read()
                child2 = self.multiplicative(token_reader)
                if child2:
                    node = SimpleASTNode(ASTNodeType.Multiplicative, token.text)
                    node.add_child(child1)
                    node.add_child(child2)
                else:
                    raise Exception('invalid multiplicative expression, expecting the right part.')
        return node


    # 语法解析：基础表达式
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
                token_reader.read()
                node = additive(token_reader)
                if node:
                    token = token_reader.peek()
                    if token and token.type == TokenType.RightParen:
                        token_reader.read()
                    else:
                        raise Exception('expecting right parenthesis')
                else:
                    raise Exception('expecting an additive expression inside parenthesis')

        return node