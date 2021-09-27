from lx import lexer

data = '''
 int _ab + - * / 9;
 '''


# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
