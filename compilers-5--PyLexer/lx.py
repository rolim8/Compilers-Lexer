import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'EQUALS',  # EQUALS
    'SEMICOLON',  # SEMICOLON END
    'LETTER'  # INDETIFIER
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# EQUALS TOKEN
t_EQUAL = r'='

# SEMICOLON TOKEN
t_SEMICOLON = r';'

# IDENTIFIER TOKEN
t_LETTER = r'\w+'


# DECIMAL TOKEN#
def t_NUMBER(t):
    r'(\d*\.\d+)|(\d+\.\d*)'
    t.value = float(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
