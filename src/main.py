from simple_lexer import SimpleLexer


def main():
    script = "int age = 45;"
    print("parse :" + script)
    token_reader = SimpleLexer().tokenize(script)
    token_reader.dump()

if __name__ == '__main__':
    main()
    