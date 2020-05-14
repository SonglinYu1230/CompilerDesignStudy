from simple_lexer import SimpleLexer
from simple_calculator import SimpleCalculator


def lexter_test():
    script = "int age = 45;"
    print("parse :" + script)
    token_reader = SimpleLexer().tokenize(script)
    token_reader.dump()

    print('*' * 30)
    script = "inta age = 45;"
    print("parse :" + script)
    token_reader = SimpleLexer().tokenize(script)
    token_reader.dump()

    print('*' * 30)
    script = "in age = 45;"
    print("parse :" + script)
    token_reader = SimpleLexer().tokenize(script)
    token_reader.dump()

    print('*' * 30)
    script = "age >= 45;"
    print("parse :" + script)
    token_reader = SimpleLexer().tokenize(script)
    token_reader.dump()

    print('*' * 30)
    script = "age > 45;"
    print("parse :" + script)
    token_reader = SimpleLexer().tokenize(script)
    token_reader.dump()


def dump(code, token_reader):
    print('*' * 10 + ' ' + code + ' ' + '*' * 10)
    token_reader.dump()
    print('*' * 50)


def calculator_test():
    calculator = SimpleCalculator()

    script = "int a = b+3;"
    print("解析变量声明语句: " + script)
    lexer = SimpleLexer()
    token_reader = lexer.tokenize(script)
    dump(script, token_reader)

    try:
        node = calculator.int_declare(token_reader)
        node.dump_ast("")
    except Exception as e:
        print('something wrong: ', e)

    print('*****************************************************\n\n')

    script = "2+3*5";
    print("计算: " + script + "，看上去一切正常。")
    calculator.evaluate(script)


if __name__ == '__main__':
    # lexter_test()
    calculator_test()
    