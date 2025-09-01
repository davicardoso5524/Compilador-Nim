import ply.lex as lex

reservadas = {
    'if': 'IF', 
    'elif':'ELIF', 
    'else': 'ELSE', 
    'while': 'WHILE', 
    'for': 'FOR',
    'proc': 'PROC', 
    'var': 'VAR', 
    'type': 'TYPE',
    'return': 'RETURN', 
    'import': 'IMPORT',
    'echo': 'ECHO',    
}

tokens = [
    'ID', 'INDENT', 'DEDENT', 'NEWLINE','INTNUMBER','FLOATNUMBER','HEX_INTNUMBER','BIN_INTNUMBER','OCT_INTNUMBER', 'STRING','CHAR',
    'SOMA', 'SUB', 'MUL', 'DIV', 'MOD', 'EXP',
    'ATRIB', 'ADICIGUAL', 'SUBIGUAL',
    'PV', 'VIRG', 'LPAREN', 'RPAREN',
    'LCHAV', 'RCHAV', 'LCOLCH', 'RCOLCH', 'DOISPONTOS','EQ',
    'GT', 'LT', 'GE', 'LE'
] + list(reservadas.values())

t_GE         = r'>='
t_LE         = r'<='
t_EQ         = r'=='
t_ADICIGUAL  = r'\+='
t_SUBIGUAL   = r'-='
t_GT         = r'>'
t_LT         = r'<'
t_SOMA       = r'\+'
t_SUB        = r'-'
t_MUL        = r'\*'
t_DIV        = r'/'
t_MOD        = r'\bmod\b'
t_EXP        = r'\^'
t_ATRIB      = r'='
t_PV         = r';'
t_VIRG       = r','
t_LPAREN     = r'\('
t_RPAREN     = r'\)'
t_LCHAV      = r'\{'
t_RCHAV      = r'\}'
t_LCOLCH     = r'\['
t_RCOLCH     = r'\]'
t_DOISPONTOS = r':'

def t_ID(t):
    r'`?[a-zA-Z][a-zA-Z_0-9]*`?'
    lexema = t.value.strip('`')
    if lexema in reservadas and not (t.value.startswith('`') and t.value.endswith('`')):
        t.type = reservadas[lexema]
    else:
        t.type = 'ID'
        t.value = lexema
    return t


underscore_digits = r'(?:[0-9]|_)+'

def _clean_underscores(s):
    return s.replace('_', '')


def t_HEX_INTNUMBER(t):
    r'0[xX](?:[0-9a-fA-F]|_)+'
    raw = t.value
    t.value = int(_clean_underscores(raw[2:]), 16)
    return t


def t_BIN_INTNUMBER(t):
    r'0[bB][01_]+'
    raw = t.value
    t.value = int(_clean_underscores(raw[2:]), 2)
    return t


def t_OCT_INTNUMBER(t):
    r'0[oO][0-7_]+'
    raw = t.value
    t.value = int(_clean_underscores(raw[2:]), 8)
    return t


def t_FLOATNUMBER(t):
    r'\d+(?:_\d+)*\.\d+(?:_\d+)*(?:[eE][+-]?\d+(?:_\d+)*)?'
    raw = t.value
    t.value = float(_clean_underscores(raw))
    return t


def t_INTNUMBER(t):
    r'\d+(?:_\d+)*'
    raw = t.value
    t.value = int(_clean_underscores(raw))
    return t

def t_STRING(t):
    r'(\"\"\"(.|\n)*?\"\"\"|\"(\\.|[^\\"])*\")'
    t.value = t.value[1:-1]
    return t

def t_comment_multiline(t):
    r'\#\[(.|\n)*?\]\#'
    pass

def t_comment_line(t):
    r'\#.*'
    pass

indent_pilha = [0]

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')
    t.type = 'NEWLINE'
    t.value = None
    return t

def lexer_tokens(lexer):
    buffer = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        if tok.type == 'NEWLINE':
            cont_linha = lexer.lexdata[lexer.lexpos:]
            espacos = 0
            for c in cont_linha:
                if c == ' ':
                    espacos += 1
                elif c == '\t':
                    espacos += 4
                else:
                    break
            lexer.lexpos += espacos

            buffer.append(tok)
            if espacos > indent_pilha[-1]:
                indent_pilha.append(espacos)
                indent_token = lex.LexToken()
                indent_token.type = 'INDENT'
                indent_token.value = espacos
                indent_token.lineno = tok.lineno
                indent_token.lexpos = lexer.lexpos
                buffer.append(indent_token)
            elif espacos < indent_pilha[-1]:
                while indent_pilha and espacos < indent_pilha[-1]:
                    indent_pilha.pop()
                    dedent_token = lex.LexToken()
                    dedent_token.type = 'DEDENT'
                    dedent_token.value = espacos
                    dedent_token.lineno = tok.lineno
                    dedent_token.lexpos = lexer.lexpos
                    buffer.append(dedent_token)
            for t in buffer:
                yield t
            buffer.clear()
        else:
            yield tok
    while len(indent_pilha) > 1:
        indent_pilha.pop()
        dedent_token = lex.LexToken()
        dedent_token.type = 'DEDENT'
        dedent_token.value = 0
        dedent_token.lineno = lexer.lineno
        dedent_token.lexpos = lexer.lexpos
        yield dedent_token

t_ignore = ' \t\r'

def t_error(t):
    print(f"Caractere ilegal: '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)

if __name__ == "__main__":
    with open("input.nim", "r") as f:
        entrada = f.read()
    lexer = lex.lex()
    lexer.input(entrada)
    for tok in lexer_tokens(lexer):
        print(tok.type, tok.value, tok.lineno, tok.lexpos)
