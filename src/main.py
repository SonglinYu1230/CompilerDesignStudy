from simple_lexer import SimpleLexer


def main():
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



if __name__ == '__main__':
    main()
    